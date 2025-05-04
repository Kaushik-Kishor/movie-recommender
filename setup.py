from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_descripton = fh.read()

AUTHOR_NAME = 'Kaushik'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name= SRC_REPO,
    version= '0.0.1',
    author= AUTHOR_NAME,
    author_email='',
    description='A package for Movie Recc system',
    long_description= long_descripton,
    long_description_content_type= 'text/markdown',
    package= [SRC_REPO],
    python_requires= '>=3.7',
    install_requires= LIST_OF_REQUIREMENTS,
)