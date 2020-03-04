import io

from setuptools import find_packages, setup

with io.open('README', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='flaskr',
    version='1.0',
    url='http://flask.pocoo.org/docs/tutorial/',
    license='BSD',
    maintainer='Pallets team',
    maintainer_email='contact@palletsprojects.com',
    description='The basic blog app built in the Flask tutorial.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask>=1.0',
        'flask-babel>=0.12',
        'flask-sqlalchemy>=2.4',
        'flask-WTF>=0.14',
        'wtforms-components>=0.10',
        'bootstrap-flask>=1.2',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
