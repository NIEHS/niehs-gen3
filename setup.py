from setuptools import setup, find_packages

setup(
    name='gen3dictionary',
    version='0.0.0',
    description="Gen3 generic data dictionary",
    license="Apache",
    packages=find_packages(),
    install_requires=[
        'dictionaryutils==3.4.2',
        'requests==2.26.0'
    ],
    dependency_links=[],
    package_data={
        "gdcdictionary": [
            "schemas/*.yaml",
            "schemas/projects/*.yaml",
            "schemas/projects/*/*.yaml",
        ]
    },
)
