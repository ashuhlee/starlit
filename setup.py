from setuptools import setup, find_packages

setup(
    name='weather-cli',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'rich',
        'terminaltexteffects',
        'requests',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'weather-cli=main:main',
        ],
    },
)