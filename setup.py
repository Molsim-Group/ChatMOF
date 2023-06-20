import re
from setuptools import setup, find_packages


with open("requirements.txt", "r") as f:
    install_requires = f.readlines()

with open("README.md", "r") as f:
    long_description = f.read()

extras_require = {"docs": ["sphinx", "livereload", "myst-parser"]}

with open("chatmof/__init__.py") as f:
    version = re.search(r"__version__ = [\'\"](?P<version>.+)[\.\"]", f.read()).group("version")


setup(
    name="chatmof",
    version=version,
    description="chatmof",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yeonghun Kang",
    author_email="dudgns1675@kaist.ac.kr",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    scripts=[],
    #url="https://hspark1212.github.io/MOFTransformer/",
    #download_url="https://github.com/hspark1212/MOFTransformer",
    #entry_points={"console_scripts": ["moftransformer=moftransformer.cli.main:main"]},
    python_requires=">=3.9",
)
