from setuptools import setup, find_packages
import os

# Read the long description from README.md (ensure it exists in the project root)
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='paper_summarizer',
    version='0.1.1',
    description='A library for summarizing and explaining academic papers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Harsh Chitaliya',
    author_email='haarshchitaliya193@gmail.com',
    url='https://github.com/harshchi19/Paper-Summarizer-Library.git',  # Update with your repo URL
    packages=find_packages(),  # This requires an __init__.py in the package directory
    install_requires=[
        'azure-ai-inference>=0.1.0',
        'PyPDF2>=3.0.0',
        'graphviz>=0.20.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
