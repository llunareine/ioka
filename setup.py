from setuptools import setup, find_packages

setup(
    name='ioka_lib',
    version='0.1',
    author='Aiganym',
    author_email='llunareine@gmail.com',
    packages=find_packages(),
    url='https://github.com/llunareine/ioka_library',
    description='library for ioka api',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 2.31.0",
        "python-dotenv >= 1.0.1"
    ],
    python_requires='>=3.10',
)