from setuptools import setup, find_packages

setup(
    name="word helper",
    version="0.0.1",
    author="Peter Popov",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        "Click",
        "prettytable"
    ], 
    
    entry_points ={
        "console_scripts": {
            "wordy = wordy.word_helper:word_helper",
        },
    },
)