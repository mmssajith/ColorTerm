from setuptools import setup, find_packages

# Read the contents of README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="terminal-colorize",
    version="2.0.1",
    author="Mmohamed Sajith",
    author_email="mmssajith@gmail.com",
    description="A comprehensive library for colored terminal output, progress bars, tables, and shapes using ANSI escape codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmssajith/colorterm",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="terminal color ansi cli colored output styling",
    project_urls={
        "Bug Reports": "https://github.com/mmssajith/colorterm/issues",
        "Source": "https://github.com/mmssajith/colorterm",
    },
)
