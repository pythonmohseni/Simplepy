import setuptools 

with open("README.md", "r") as fh: 
	description = fh.read() 

setuptools.setup( 
	name="test-package", 
	version="1.0.0", 
	author="Code your future team",
	packages=["Simplepy"], 
	description="""
	Hello, im arsalan, from code your future team. this is a python package to use the python easier to use

    Docs are in development
    If it finish, we put link here
""", 
	long_description=description, 
	long_description_content_type="text/markdown", 
	url="https://github.com/pythonmohseni/Simplepy", 
	license='MIT', 
	python_requires='>=3.12', 
	install_requires=[] 
) 
