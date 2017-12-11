"""
Task-One Setup file

"""

from setuptools import setup


setup(
    name='app',
    version='0.1.8',
    url='https://github.com/varshaaraman/flask_app_one',
    license='',
    author='Varshaa M',
    author_email='varshrsman93@gmail.com',
    maintainer='Varshaa M',
    maintainer_email='varshrsman93@gmail.com',
    description='Heroku for Flask',
    long_description=__doc__,
    py_modules=['app'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)