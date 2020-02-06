from setuptools import setup

def readme():
    with open('README.md', 'r', encoding = 'utf-8') as f:
        README = f.read()
    return README


setup(
    name="Bangla-stemmer",
    version="1.0",
    description="A Python package to get stem of any inflected Bangla words.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Fatick-DevStudio/Bangla-stemmer",
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
    packages=["bangla_stemmer"],
    include_package_data=True,
    keywords=('bengali', 'bangla', 'stemmer', 'bengali stemmer', 'bangla stemmer')
)
