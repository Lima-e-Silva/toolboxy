from setuptools import setup, find_packages

NAME = 'toolboxy'
VERSION = '0.1.2'
AUTHOR = 'Lima & Silva'
EMAIL = 'luizpaulo@protonmail.com'
DESCRIPTION = 'This repository is a collection of tools for developers to easily access relevant solutions for development in order to accelerate their workflow. It provides a variety of resources that are constantly used.'

setup(
    name=NAME,
    version=VERSION,
    url='https://github.com/Lima-e-Silva/toolboxy',
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4', 'loguru', 'openai', 'pipreqs', 'pyperclip',
        'python-dotenv', 'requests', 'setuptools', 'snakeviz', 'winotify'
    ],
    keywords=['python', 'tools', 'programming', 'devs'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Microsoft :: Windows",
    ])