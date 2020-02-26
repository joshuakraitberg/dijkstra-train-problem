from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))


setup(
    name='bmo_trains_problem',
    version='1.0.0',
    description='Trains problem from BMO',
    author='Joshua Kraitberg',
    author_email='joshua.kraitberg@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    test_suite='trains_problem.tests',
    entry_points={
        'console_scripts': [
            'bmo_trains_problem=trains_problem.cli:main',
        ],
    },
)