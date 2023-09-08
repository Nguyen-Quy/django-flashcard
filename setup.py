# from distutils.core import setup
import py2exe
from setuptools import setup

setup(
    name="test",
    version="1.0",
    description="A useful module",
    license="MIT",
    author="Quy Nguyen",
    install_requires=["django", "pendulum", "supermemo2", "pywebview", "psycopg2"],
    console=["gui.py"],
)
