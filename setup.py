from setuptools import setup

setup(
    name='cinemascore.py',
    author='jhumms',
    author_email='git@xenonnsmb.com',
    version='0.1',
    packages=['cinemascore',],
    license=open('LICENSE').read(),
    summary='A Python library for getting the unoffical Cinemascore movie titles, grades, and year.',
    url='https://github.com/jhumms/Cinemascore/',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.18.4",
        "lxml >= 4.1.1",
        "requests >= 2.26.0",
        "beautifulsoup4 >= 4.9.3",
        "base64",
        "json",
    ],
)
