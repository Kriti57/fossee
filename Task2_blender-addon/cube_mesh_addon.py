bl_info = {
    "name": "Cube Distribution and Mesh Merger",
    "author": "Kriti Gupta",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Task Panel",
    "description": "Distribute cubes in a grid and merge meshes",
    "category": "Object",
}

import bpy
import math
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import IntProperty, PointerProperty


# PROPERTIES
class TaskProperties(PropertyGroup):
    num_cubes: IntProperty(
        name="Number of Cubes",
        description="Number of cubes to distribute (N < 20)",
        default=4,
        min=1,
        max=50
    )


# UI PANEL
class VIEW3D_PT_task_panel(Panel):
    bl_label = "Task 1"
    bl_idname = "VIEW3D_PT_task_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Task'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        task_props = scene.task_properties
        
        layout.prop(task_props, "num_cubes")
        layout.operator("object.distribute_cubes", text="Distribute Cubes")
        layout.operator("object.delete_cubes", text="Delete Cubes")
        layout.separator()
        layout.operator("object.compose_mesh", text="Compose Mesh")


# OPERATORS
class OBJECT_OT_distribute_cubes(Operator):
    bl_idname = "object.distribute_cubes"
    bl_label = "Distribute Cubes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        scene = context.scene
        task_props = scene.task_properties
        N = task_props.num_cubes
        
        # Check if N > 20
        if N > 20:
            self.report({'ERROR'}, "The number is out of range")
            return {'CANCELLED'}
        
        # Calculate grid dimensions
        m = math.ceil(math.sqrt(N))
        n = math.ceil(N / m)
        
        # Create collection
        collection_name = "Distributed Cubes"
        if collection_name in bpy.data.collections:
            collection = bpy.data.collections[collection_name]
        else:
            collection = bpy.data.collections.new(collection_name)
            context.scene.collection.children.link(collection)
        
        # Create cubes
        spacing = 1.5
        cube_count = 0
        
        for i in range(m):
            for j in range(n):
                if cube_count >= N:
                    break
                
                x = i * spacing
                y = j * spacing
                z = 0
                
                bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, z))
                cube = context.active_object
                
                # Move to collection
                for col in cube.users_collection:
                    col.objects.unlink(cube)
                collection.objects.link(cube)
                
                cube_count += 1
            
            if cube_count >= N:
                break
        
        self.report({'INFO'}, f"Created {N} cubes in {m}x{n} grid")
        return {'FINISHED'}


class OBJECT_OT_delete_cubes(Operator):
    bl_idname = "object.delete_cubes"
    bl_label = "Delete Selected Cubes"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selected_objects = context.selected_objects
        
        if not selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}
        
        deleted_count = 0
        for obj in selected_objects:
            if obj.type == 'MESH':
                bpy.data.objects.remove(obj, do_unlink=True)
                deleted_count += 1
        
        self.report({'INFO'}, f"Deleted {deleted_count} object(s)")
        return {'FINISHED'}


class OBJECT_OT_compose_mesh(Operator):
    bl_idname = "object.compose_mesh"
    bl_label = "Compose Mesh"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        selected_objects = context.selected_objects
        
        if len(selected_objects) < 2:
            self.report({'WARNING'}, "Select at least 2 mesh objects")
            return {'CANCELLED'}
        
        # Filter only mesh objects
        mesh_objects = [obj for obj in selected_objects if obj.type == 'MESH']
        
        if len(mesh_objects) < 2:
            self.report({'WARNING'}, "Select at least 2 mesh objects")
            return {'CANCELLED'}
        
        # Check if meshes share a common face
        has_common_face = self.check_common_faces(mesh_objects)
        
        if not has_common_face:
            self.report({'WARNING'}, "Selected meshes do not share a common face")
            return {'CANCELLED'}
        
        # Join the meshes
        context.view_layer.objects.active = mesh_objects[0]
        bpy.ops.object.join()
        
        # Remove duplicate vertices (this merges common vertices and removes internal faces)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles(threshold=0.0001)
        
        # Remove internal faces
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_interior_faces()
        bpy.ops.mesh.delete(type='FACE')
        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        self.report({'INFO'}, "Meshes composed successfully")
        return {'FINISHED'}
    
    def check_common_faces(self, mesh_objects):
        """Check if two mesh objects share at least one common face"""
        if len(mesh_objects) < 2:
            return False
        
        # Get faces from first two objects
        obj1 = mesh_objects[0]
        obj2 = mesh_objects[1]
        
        # Get world coordinates of all face vertices
        faces1 = self.get_face_data(obj1)
        faces2 = self.get_face_data(obj2)
        
        # Check if any faces match
        tolerance = 0.001
        for face1_verts in faces1:
            for face2_verts in faces2:
                if self.faces_match(face1_verts, face2_verts, tolerance):
                    return True
        
        return False
    
    def get_face_data(self, obj):
        """Get world coordinates of all vertices for each face"""
        faces_data = []
        mesh = obj.data
        
        for face in mesh.polygons:
            face_verts = []
            for vert_idx in face.vertices:
                # Convert to world coordinates
                world_co = obj.matrix_world @ mesh.vertices[vert_idx].co
                face_verts.append(world_co.copy())
            faces_data.append(face_verts)
        
        return faces_data
    
    def faces_match(self, verts1, verts2, tolerance):
        """Check if two faces have the same vertices (regardless of order)"""
        if len(verts1) != len(verts2):
            return False
        
        # Check if all vertices from face1 exist in face2
        for v1 in verts1:
            found = False
            for v2 in verts2:
                if (v1 - v2).length < tolerance:
                    found = True
                    break
            if not found:
                return False
        
        return True


# REGISTRATION
classes = (
    TaskProperties,
    OBJECT_OT_distribute_cubes,
    OBJECT_OT_delete_cubes,
    OBJECT_OT_compose_mesh,
    VIEW3D_PT_task_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.task_properties = PointerProperty(type=TaskProperties)
    print("Addon Registered")

def unregister():
    del bpy.types.Scene.task_properties
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("Addon Unregistered")

if __name__ == "__main__":
    register()