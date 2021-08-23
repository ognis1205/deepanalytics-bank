# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="deepanalytics",
    version="1.0.0",
    description="Deepanalytics Bank",
    author="ognis1205",
    python_requires=">=3.7",
    install_requires=[
        "numpy", 
        "scipy", 
        "pandas", 
        "sklearn",
        "xgboost",
        "matplotlib",
        "statsmodels",
        "patsy",
        "seaborn",
        "jupyter"],
    packages=find_packages(exclude=["test", "test.*"]),
    test_suite="test")

