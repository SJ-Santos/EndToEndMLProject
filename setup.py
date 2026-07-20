from setuptools import setup, find_packages
from typing import List 

HYPEN_AND_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    this function return a list of requirements that will be used in the project
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] 
        #this part is to replace the \n that will be read, when we try to read the strings and replace they for a blank space
        if HYPEN_AND_DOT in requirements:
            requirements.remove(HYPEN_AND_DOT)
    return requirements
    

setup(
    name="EndToEndMLProject",
    version="0.0.1",
    author="SJ-Santos",
    author_email="samueljsantos20@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt")  
)