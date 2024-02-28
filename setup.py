from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:    #function will be given an input as file path in string form and it will return as a list output.
    requirement=[]   # Initialize an empty list to store requirements
    with open(file_path) as file_obj:    # Open this requirement.txt
        requirements=file_obj.readlines()  # Read all lines from the file and store them in a list
        requirements=[req.replace("\n","") for req in requirements]   # Remove newline characters from each line

        if HYPEN_E_DOT in requirements:    # Check if a specific string, HYPEN_E_DOT, is present in the requirements list
            requirements.remove(HYPEN_E_DOT) # Remove HYPEN_E_DOT from the requirements list if it exists

    return requirements    # Return the list of requirements


setup(
    name='RegressorProject',
    version='0.0.1',
    author='bhopinder',
    author_email='bhopinder92@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
    )