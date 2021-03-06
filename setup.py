"""Package definition for PyPI."""
import os

from setuptools import setup

PACKAGE_NAME = 'mbed-targets'
SOURCE_DIR = 'mbed_targets'
__version__ = None

repository_dir = os.path.dirname(__file__)

# Read package version, this will set the variable `__version__` to the current version.
with open(os.path.join(repository_dir, SOURCE_DIR, '_version.py')) as fh:
    exec(fh.read())

# Use readme needed as long description in PyPI
with open(os.path.join(repository_dir, 'README.md')) as fh:
    long_description = fh.read()

setup(
    author='Graham Hammond',
    author_email='support@mbed.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Embedded Systems',
    ],
    description='Mbed Tools: Target information for building Mbed OS',
    keywords='Arm Mbed OS MbedOS build target platform board module',
    include_package_data=True,
    install_requires=[
        'requests>=2.20',
        'python-dotenv',
        'Click~=7.0',
    ],
    license='Apache 2.0',
    long_description_content_type='text/markdown',
    long_description=long_description,
    name=PACKAGE_NAME,
    packages=[SOURCE_DIR],
    python_requires='>=3.6,<4',
    url=f'https://github.com/ARMmbed/{PACKAGE_NAME}',
    version=__version__,
)
