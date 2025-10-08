from setuptools import find_packages, setup

# Read the contents of README file
with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="terminal-colorize",
    version="2.0.2",
    author="Mohamed Sajith",
    author_email="mmssajith@gmail.com",
    description="A comprehensive library for colored terminal output, progress bars, tables, and shapes using ANSI escape codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mmssajith/colorterm",
    packages=find_packages(exclude=["tests", "tests.*", "examples"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Terminals",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Environment :: Console",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No dependencies - pure Python implementation
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "ascii": [
            "numpy>=1.19.0",
            "Pillow>=8.0.0",
        ],
    },
    keywords=[
        "terminal",
        "color",
        "ansi",
        "cli",
        "colored",
        "output",
        "styling",
        "progress",
        "progressbar",
        "table",
        "shapes",
        "ascii-art",
        "console",
        "terminal-colors",
        "terminal-styling",
        "text-formatting",
        "dashboard",
    ],
    project_urls={
        "Homepage": "https://github.com/mmssajith/colorterm",
        "Bug Reports": "https://github.com/mmssajith/colorterm/issues",
        "Source": "https://github.com/mmssajith/colorterm",
        "Documentation": "https://github.com/mmssajith/colorterm#readme",
        "Changelog": "https://github.com/mmssajith/colorterm/blob/main/CHANGELOG.md",
    },
    zip_safe=False,
)
