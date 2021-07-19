import os
import sys

from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel

PY3 = sys.version_info[0] >= 3
if not PY3:
    from pathlib2 import Path
else:
    from pathlib import Path

if os.path.isdir("clipboard.js") and not os.path.islink(
    "sphinx_copybutton/_static/clipboard.min.js"
):
    raise SystemExit("Error: Support for symbolic links is required")

if os.path.isdir("clipboard.js") and not os.path.isfile(
    "clipboard.js/dist/clipboard.min.js"
):
    raise SystemExit(
        """Error: clipboard.js submodule not available, run

        git submodule update --init
        """
    )

with open("./README.md") as ff:
    readme_text = ff.read()

# Parse version
init = Path(__file__).parent.joinpath("sphinx_copybutton", "__init__.py")
for line in init.read_text().split("\n"):
    if line.startswith("__version__ ="):
        break
version = line.split(" = ")[-1].strip('"')

setup(
    name="sphinx-copybutton",
    version=version,
    description="Add a copy button to each of your code cells.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Executable Book Project",
    url="https://github.com/executablebooks/sphinx-copybutton",
    license="MIT License",
    packages=find_packages(),
    package_data={
        "sphinx_copybutton": [
            "_static/copybutton.css",
            "_static/copybutton_funcs.js",
            "_static/copybutton.js_t",
            "_static/copy-button.svg",
            "_static/check-solid.svg",
            "_static/clipboard.min.js",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Sphinx :: Extension",
        "Framework :: Sphinx",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    #install_requires=["sphinx>=1.8"],
    #extras_require={
    #    "code_style": ["pre-commit==2.12.1"],
    #},
)
