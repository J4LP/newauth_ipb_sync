"""
NewAuth IPB Sync
===================

Providing more informations to the IPB 3 LDAP authentication module.
"""
from setuptools import setup

setup(
    name='NewAuth IPB Sync',
    version='0.0.1',
    author='@adrien-f',
    author_email='vadrin_hegirin@j4lp.com',
    description='Helping IPB 3 LDAP authentication module.',
    long_description=__doc__,
    packages=['newauth_ipb_sync'],
    zip_safe=True,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ]
)
