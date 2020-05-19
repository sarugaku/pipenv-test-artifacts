import os

from setuptools import find_packages, setup

thisdir = os.path.abspath(os.path.dirname(__file__))
version = "1.0.0"

setup(
    name="pep508_package",
    version=version,
    description="Pep 508 test package",
    long_description="This is a package",
    install_requires=[
        "six",
        "sibling_package @ git+https://github.com/sarugaku/pipenv-test-fixtures.git@master#subdirectory=fixtures/parent_folder/sibling_package",
    ],
    extras_require={"testing": ["coverage", "flaky"], "dev": ["parver", "invoke", "wheel"]},
    package_dir={"": "src"},
    packages=["pep508_package"],
    include_package_data=True,
    zip_safe=True,
)
