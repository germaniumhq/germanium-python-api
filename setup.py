from setuptools import setup, find_packages

setup(
    name='germanium',
    version='1.3.7',
    description='The germanium project.',
    long_description = 'The germanium project: Selenium WebDriver testing API that doesn\'t suck.',
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',

    install_requires=['selenium'],
    packages=['germanium'],
    package_data={'germanium': ['*.js']}
)
