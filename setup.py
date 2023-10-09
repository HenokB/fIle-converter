from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="file_converter",
    version="0.1.0",
    author="Henok Biadglign Ademtew",
    author_email="henokb2124@gmail.com",
    description="A simple and efficient file converter for various data file types.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HenokB/file-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas>=1.2.0",
        # Other dependencies...
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
            # Other development dependencies...
        ],
    },
    entry_points={
        "console_scripts": [
            "file_converter=file_converter:main",
        ],
    },
    include_package_data=True,
)
