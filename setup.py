from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ngprocesstxt",
    version=0.1,
    author="Retin",
    description="A small text cleaning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ng-retin/ngprocesstxt",
    project_urls={
        "Bug Tracker": "https://github.com/ng-retin/ngprocesstxt/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    download_url="https://github.com/ng-retin/ngprocesstxt/archive/refs/tags/0.1.tar.gz"
)