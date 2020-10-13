from typing import IO, Sequence
from setuptools import setup, find_packages
from counter import __author__, __email__, __package_name__, __version__


def _description() -> str:
    """Returns project description."""
    with open("README.md") as readme:  # type: IO[str]
        return readme.read()


def _requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with open("requirements.txt") as requirements:  # type: IO[str]
        return tuple(map(str.strip, requirements.readlines()))


if __name__ == "__main__":
    setup(
        name=__package_name__,
        version=__version__,
        author=__author__,
        author_email=__email__,
        description=(
            "This project represents a simple web app to "
            "calculate calories based on given food type."
        ),
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
