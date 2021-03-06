import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="excel-dates",
    author="Bart-Jan Hulsman",
    author_email="hulsmanbj@gmail.com",
    description="Convert excel dates to datetime in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AutoActuary/excel-dates",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    use_scm_version={
        "write_to": "excel_dates/version.py",
    },
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "locate~=1.0",
    ],
)
