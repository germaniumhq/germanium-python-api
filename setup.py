from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='germanium',
    version='1.7.7',
    description='The germanium project: Selenium WebDriver testing API that doesn\'t disappoint.',
    long_description = readme,
    author='Bogdan Mustiata',
    author_email='bogdan.mustiata@gmail.com',
    license='BSD',

    install_requires=['selenium==2.53.2', 'cssselect==0.9.1', 'webcolors==1.5'],
    packages=['germanium',
              'germanium.impl',
              'germanium.locators',
              'germanium.selectors',
              'germanium.static',
              'germanium.util'],
    package_data={'germanium': ['*.js']}
)
