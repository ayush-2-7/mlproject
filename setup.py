from setuptools import find_packages
from setuptools import setup
from typing import List

hyphen_edot='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n"," ") for req in requirements]
        if hyphen_edot in requirements:
            requirements.remove(hyphen_edot)
    return requirements



setup(
    name= 'mlproject',
    version='0.1',
    author='Ayush',
    author_email='ayushrawat2345@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements('requirements.txt')
)