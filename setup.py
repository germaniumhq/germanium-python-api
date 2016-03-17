from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='germanium',
    version='1.6.5',
    description='The germanium project: Selenium WebDriver testing API that doesn\'t disappoint.',
    long_description = readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',

    install_requires=['selenium==2.52.0'],
    packages=['germanium', 'germanium.locators', 'germanium.selectors', 'germanium.static', 'germanium.util'],
    package_data={'germanium': ['*.js']}
)
