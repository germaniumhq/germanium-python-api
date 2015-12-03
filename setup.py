from setuptools import setup, find_packages

setup(
    name='germanium',
    version='1.1.1',
    description='The germanium project',
    long_description = 'The germanium project',
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',

    install_requires=['selenium'],
    packages=['germanium'],
    package_data={'germanium': ['*.js']}
)
