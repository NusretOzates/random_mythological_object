from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()


setup(
    name="random-mythological-name",
    packages=find_packages(include=["random-mythological-names"]),
    version="1.0.0",
    description="Random Mythological Name Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=["random", "mythology"],
    author="Nusret Ozates",
    license="MIT",
    install_requires=[],
)
