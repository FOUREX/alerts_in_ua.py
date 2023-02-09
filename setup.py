from setuptools import setup

requirements = []
with open('.alerts_in_ua.requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='alerts_in_ua.py',
    author='FOUREX',
    url='https://github.com/FOUREX/alerts_in_ua.py',
    install_requires=requirements,
)
