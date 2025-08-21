from setuptools import setup, find_packages

def get_requirements()->list[str]:
    requirements_list=list[str]=[]
    return requirements_list



setup(
    name="sensor",  
    version="0.1.0",
    author="vandana",
    author_email="svandana56@gmail.com",
    packages=find_packages(),
    install_requires=["pymongo"]
    
        
)
