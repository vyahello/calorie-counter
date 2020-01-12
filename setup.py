from typing import IO, Sequence
from setuptools import setup, find_packages


def _description() -> str:
    """Returns project description."""
    with open("README.md", "r") as readme:  # type: IO[str]
        return readme.read()


def _requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt", "r") as requirements:  # type: IO[str]
        return tuple(map(str.strip, requirements.readlines()))


setup(
    name="calorie-counter",
    version="0.1.2",
    author="Volodymyr Yahello",
    author_email="vyahello@gmail.com",
    description="This project represents simple web app to calculate calories based on given food type.",
    long_description=_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vyahello/calorie-counter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=_requirements(),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.6",
)
