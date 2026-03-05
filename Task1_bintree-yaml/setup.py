from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bintree-yaml",
    version="1.0.0",
    author="Kriti Gupta",
    author_email="kriti.gupta20004@gmail.com",
    description="A binary tree implementation with YAML integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kriti57/bintree-yaml",
    packages=find_packages(),
    py_modules=["main"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "PyYAML>=5.1",
    ],
)