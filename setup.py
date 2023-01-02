from setuptools import setup, find_packages

NAME = 'DevTools'
VERSION = '0.1.0'
AUTHOR = 'Lima & Silva'
EMAIL = 'luizpaulo@protonmail.com'
DESCRIPTION = 'This repository is a collection of tools for developers to easily access relevant solutions for development in order to accelerate their workflow. It provides a variety of resources that are constantly used.'

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=['beautifulsoup4', 'loguru', 'pipreqs', 'requests', 'setuptools', 'snakeviz', 'winotify'],
    keywords=['python', 'tools', 'programming'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)