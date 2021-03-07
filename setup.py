import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyresx",
    version="0.1.1",
    author="cola314",
    author_email='ubj020314@gmail.com',
    description='.resx file writer for python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cola314/pyresx',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)