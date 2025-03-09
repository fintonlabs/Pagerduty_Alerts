from setuptools import setup, find_packages

setup(
    name='incident-fetcher',
    version='0.1.0',
    description='Fetches incidents from a RESTful API and prints them to the console.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)