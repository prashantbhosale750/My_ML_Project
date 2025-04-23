#able to build entire ML package 
#building our model as a package
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """this function will return the list of requirements"""
    requrirements=[]
    with open(file_path) as file_obj:
        requrirements=file_obj.readlines()
        requrirements=[req.replace("\n","")for req in requrirements]
        if HYPEN_E_DOT in requrirements:
            requrirements.remove(HYPEN_E_DOT)
    return requrirements
        
        
        
        
setup(
name='mlproject',
version='0.0.1',
author='Prashant',
author_email='prashantbhosale750@gmail.com',
packages=find_packages(),
install_requires=get_requirements('Requirement.txt')
)
