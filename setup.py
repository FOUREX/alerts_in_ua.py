from setuptools import setup

from alerts_in_ua import __version__


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r", encoding="utf-8") as file:
    requires = file.read().splitlines()


setup(
    name="alerts_in_ua.py",
    version=__version__,
    description="Бібліотека для використання API сайту alerts.in.ua",
    long_description=long_description,
    author='FOUREX, SladkayaDoza',
    author_email="Foxtrotserega@gmail.com",
    url="https://github.com/FOUREX/alerts_in_ua.py",
    license="MIT",
    install_requires=requires,
)
