from setuptools import setup, find_packages

setup(
    name='incident_processor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'incident_processor=incident_processor:main',
        ],
    },
)