from setuptools import find_packages, setup

setup(
    name='daz',
    packages=find_packages(),
    version='0.0.1',
    description='A python library with multiple utilities.',
    author='Juan Manuel Mejía Botero',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)