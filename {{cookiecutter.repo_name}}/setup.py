from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="{{cookiecutter.repo_name}}",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["{{cookiecutter.repo_name}}"],
    install_requires=[],
)
