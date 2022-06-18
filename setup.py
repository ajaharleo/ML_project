from setuptools import find_packages, setup
from typing import List


# declaring variables for setup functions
Project_name = 'housing-predictor'
Version = '0.0.1'
Author = 'Azhar'
Description = 'First full ML project: hosing prediction'
Packages = ['housing']
Requirement_file_name = 'requirements.txt'

def get_requirements_list()->List[str]:
    '''
    Description: this function is going to return list of requirements
    mention in requirements.txt

    return: a list which contain name of libraries mentioned in requirements.txt file
    '''
    with open(Requirement_file_name) as requirement_file:
        return requirement_file.readlines().remove('-e.')


setup(
name=Project_name,
version=Version,
author=Author,
description=Description,
packages=find_packages(),#['housing']
install_requires = get_requirements_list())

if __name__ == '__main__':
    print(get_requirements_list)