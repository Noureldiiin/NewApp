from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in madkour_filling_request/__init__.py
from madkour_filling_request import __version__ as version

setup(
	name="madkour_filling_request",
	version=version,
	description="Madkour Filling Request",
	author="Noureldin@madkour",
	author_email="noureldin.mohamed@madkour.com.eg",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
