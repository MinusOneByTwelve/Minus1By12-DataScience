import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Minus1By12DataScience",
    version="1.0.1",
    author="MinusOneByTwelve Solutions LLP",
    author_email="Contact@Minus1By12.com",
    description="BigData, CoreML & DeepLearning Assistance Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MinusOneByTwelve/Minus1By12DataScience",
    download_url = "https://github.com/MinusOneByTwelve/Minus1By12DataScience/archive/1.0.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

