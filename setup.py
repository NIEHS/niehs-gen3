from setuptools import setup, find_packages

setup(
    name='gen3dictionary',
    version='0.0.0',
    description="Gen3 generic data dictionary",
    license="Apache",
    packages=find_packages(),
    install_requires=[
        'dictionaryutils',
    ],
    dependency_links=[
       "git+https://github.com/uc-cdis/dictionaryutils.git@2.0.4#egg=dictionaryutils",
    ],
    package_data={
        "gdcdictionary": [
            "schemas/*.yaml",
            "schemas/projects/*.yaml",
            "schemas/projects/*/*.yaml",
        ]
    },
)
