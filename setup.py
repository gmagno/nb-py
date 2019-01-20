from setuptools import setup, find_packages

version = '0.1.3'


# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Get requirements from requirements.txt file
with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().replace('==', '>=').splitlines()

# Get requirements from requirements-dev.txt file
with open(path.join(here, 'requirements-dev.txt')) as f:
    requirements_dev = f.read().replace('==', '>=').splitlines()
    print('requirements_dev: {}'.format(requirements_dev))

setup(
    name='nb_py',
    version=version,
    description='Newton Basins implementation in Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gmagno/nb-py',
    author='gmagno',
    author_email='goncalo.magno@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
    ],
    keywords='newton basins',
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        'dev': requirements_dev,
    },
        data_files=[(
        '.', [
            'requirements.txt',
            'requirements-dev.txt',
        ]
    )],
    project_urls={
        'Bug Reports': 'https://github.com/gmagno/np-py/issues',
        'Source': 'https://github.com/gmagno/nb-py',
    },
)
