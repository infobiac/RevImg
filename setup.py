import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-your-username",
    version="0.0.1",
    author="Christophe Rimann",
    author_email="infobiac1@gmail.com",
    description="A package to interact with the google reverse image search service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/infobiac/RevImg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)