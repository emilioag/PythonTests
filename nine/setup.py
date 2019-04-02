from setuptools import setup, find_packages

setup(
    name='csv',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Click',
        'pdfkit',
        'jinja2'
    ],
    entry_points='''
        [console_scripts]
        csv=script.main:main
    ''',
)
