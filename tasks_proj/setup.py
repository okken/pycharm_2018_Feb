"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='tasks',
    version='0.1.2',
    license='MIT',
    description='Minimal Project Task Management',

    author='Brian Okken',
    author_email='Please use pythontesting.net contact form.',
    url='http://pythontesting.net',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click', 'tinydb', 'pytest-runner', 'attrs', 'pytest'],

    entry_points={
        'console_scripts': [
            'tasks = tasks.cli:tasks_cli',
        ]
    },
)
