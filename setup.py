from setuptools import setup, find_packages

setup(
    name='contrail-api-cli-howto',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'contrail-api-cli'
    ],
    entry_points={
        'contrail_api_cli.command': [
            'hello = howto:Hello'
        ]
    }
)
