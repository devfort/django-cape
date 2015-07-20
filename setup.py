# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

PACKAGE = 'django_cape'
VERSION = '1.0'

package_data = {
        'django_cape': [ 'templates/cape/*.html' ],
}

setup(
    name=PACKAGE, version=VERSION,
    description="Django app that provides CAPE templates for progressive enhancement.",
    packages=[
        'django_cape',
    ],
    package_data=package_data,
    license='MIT',
    author='James Aylett and Mark Norman Francis',
    author_email='contact@devfort.com',
    install_requires=[
        'Django>=1.6.0',
    ],
    url = 'https://github.com/devfort/django-cape',
    classifiers = [
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
