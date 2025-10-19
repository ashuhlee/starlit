from setuptools import setup, find_packages

setup(
    name='starlit',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'python-dotenv',
        'requests',
        'rich',
        'terminaltexteffects',
        'rich-gradient'
    ],
    entry_points={
        'console_scripts': [
            'starlit=main:main',
        ],
    },
)