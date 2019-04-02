from setuptools import setup, find_packages

setup(
    name='twitter',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'rethinkdb',
        'fpdf',
        'jinja2',
        'pdfkit'
    ],
    entry_points='''
        [console_scripts]
        twitter=script.main:main
    ''',
)
