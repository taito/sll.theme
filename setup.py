from setuptools import find_packages
from setuptools import setup


setup(
    name='sll.theme',
    version='0.4',
    description="SLL Theme",
    long_description=open("README.rst").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
    ],
    keywords='',
    author='INICIE, Inc.',
    author_email='taito.horiuchi@inicie.net',
    url='',
    license='None-free',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['sll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'hexagonit.testing',
        'plone.app.contentlisting',
        'plone.app.theming',
        'plone.browserlayer',
        'setuptools',
        'zope.i18nmessageid',
    ],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,
)
