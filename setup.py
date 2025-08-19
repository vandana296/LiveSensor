from setuptools import setup, find_packages

def get_requirements()->list[str]:
    requirements_list = list[str] = []
    return requirements_list









setup(
    name="LiveSensor", 
    version="0.1.0",    
    author="Vandana Singh",
    author_email="vandana@example.com",  
    packages=find_packages(),  
    install_requires = get_requirements(),
    
    
)