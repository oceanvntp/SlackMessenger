from setuptools import setup, find_packages

setup(
    name='SlackMessenger',
    version='0.1',
    author='Hiromi Matsumoto',
    author_email='ocean.vntp@gmail.com',
    description='python package for sending slack messages',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oceanvntp/SlackMessenger.git',
    packages=find_packages(),
    install_requires=[
        'requests',
        'PyYAML'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
