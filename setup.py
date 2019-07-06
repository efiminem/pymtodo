from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='pymtodo',  
     version='0.1',
     author="Efim Mazhnik",
     author_email="efimmazhnik@gmail.com",
     description="Unofficial Microsoft To-Do python library",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/efiminem/pymtodo",
     packages=["pymtodo"],
     package_dir={"pymtodo": "src"},
     classifiers=[
	     "Development Status :: 2 - Pre-Alpha",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
