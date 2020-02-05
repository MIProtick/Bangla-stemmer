from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="fatick-stemmer",
    version="1.0.0",
    description="A Python package to get stem of any inflected words.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Fatick-DevStudio/fatick-stemmer",
    author="Mezbaul Islam Protick",
    author_email="mezbaulislamprotick@gmail.com",
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["fatick_stemmer"],
    include_package_data=True,
    keywords=('bengali', 'bangla', 'stemmer', 'bengali stemmer')
)
