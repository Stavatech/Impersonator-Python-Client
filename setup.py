from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='impersonator',
    version='0.1.1',
    description='A Python client for the Impersonator service',
    long_description=long_description,
    url='https://github.com/Stavatech/Impersonator-Python-Client',
    author='David Brown',
    author_email='davidbrownza@outlook.com',
    license='GPLv3',
    packages=['impersonator'],
    install_requires=[
        'requests',
        'mock'
    ],
    zip_safe=False
)