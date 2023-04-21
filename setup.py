import os

from setuptools import setup, find_packages

NAME = "tonplay-sdk"
VERSION = None
DESCRIPTION = (
    "This is a lightweight library that works as a connector to TON Play public API"
)

about = {}
root = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(os.path.dirname(__file__), "requirements/common.txt"), "r"
) as fh:
    requirements = fh.readlines()

with open("README.md", "r") as fh:
    about["long_description"] = fh.read()

if not VERSION:
    with open(os.path.join(root, "tonplay", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    license='MIT',
    author="TON Play",
    packages=find_packages(exclude=("tests",)),
    keywords=["TON Play", "Ton Play API", "Tonplay API", "ton sdk", "ton"],
    install_requires=[req for req in requirements],
    python_requires=">=3.11.1",
)
