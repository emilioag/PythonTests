from setuptools import setup, find_packages

setup(
    name='gdrive',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'google-api-python-client',
        'google-auth-oauthlib'
    ],
    entry_points='''
        [console_scripts]
        gdrive=script.main:main
    ''',
)
