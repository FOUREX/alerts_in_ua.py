from setuptools import setup


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

requires = [
    "aiohttp~=3.8.3",
    "requests~=2.28.1",
    "svglib~=1.5.1",
    "reportlab~=3.6.12"
]


setup(
    name="alerts_in_ua.py",
    version="1.2.4",
    description="Бібліотека для використання API сайту alerts.in.ua",
    long_description=long_description,
    author='FOUREX, SladkayaDoza',
    author_email="Foxtrotserega@gmail.com",
    url="https://github.com/FOUREX/alerts_in_ua.py",
    license="MIT",
    install_requires=requires,
)
