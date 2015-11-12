""" Setup file """

from setuptools import setup, find_packages

REQUIREMENTS = []

TEST_REQUIREMENTS = [
    'tox',
    'pytest',
    'coverage',
    'flake8'
]

if __name__ == "__main__":
    setup(
        name='converter',
        version='0.0.0',
        author='Josh Bailey and Joe Cross',
        url='https://github.com/binkocd/converter',
        license='MIT',
        platforms='any',
        include_package_data=True,
        packages=find_packages(exclude=('tests',)),
        install_requires=REQUIREMENTS,
        tests_require=REQUIREMENTS + TEST_REQUIREMENTS,
    )
