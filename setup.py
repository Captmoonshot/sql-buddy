import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


setup(
	name="sql-buddy",
    version="1.0.4",
    description="SQL study aid for the command line built with Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Captmoonshot/sql-buddy",
    author="Sammy Lee",
    author_email="sam@gygantor.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["sql_buddy"],
    include_package_data=True,
    install_requires=["prompt-toolkit==3.0.7", "Pygments==2.7.1", "sqlalchemy==1.3.19", "sqlalchemy-utils==0.36.6"],
    entry_points={
        "console_scripts": [
            "sql_buddy=sql_buddy.__main__:main",
        ]
    },
)


