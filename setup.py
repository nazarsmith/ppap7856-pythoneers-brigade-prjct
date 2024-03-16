import setuptools

with open("README.md", "r") as description:
    global info
    info = description.read()

setuptools.setup(
    name="py_brigade_personal_assistant",
    version="0.0.4",
    description="A personal assistant.",
    long_description=info,
    long_description_content_type="text/markdown",
    url="https://github.com/nazarsmith/ppap7856-pythoneers-brigade-prjct",
    author="Nazar Stakhovskyi",
    author_email="nazarstahovsky@gmail.com",
    license="MIT",
    packages=setuptools.find_namespace_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=[],
    entry_points={"console_scripts": ["get-started = personal_assistant.main:main"]},
    include_package_data=True,  # include non-.py files
    package_data={"": ["*.txt", "*.md"]},
)  ## python setup.py bdist_wheel ## install twine ## twine upload dist/* ## pip install -e - install from local dist
