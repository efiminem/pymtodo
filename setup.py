from setuptools import setup


with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
     name='pymtodo',  
     version='0.2',
     author="Efim Mazhnik",
     author_email="efimmazhnik@gmail.com",
     description="Unofficial Microsoft To-Do python library",
     long_description=long_description,
     long_description_content_type="text/x-rst",
     url="https://github.com/efiminem/pymtodo",
     download_url="https://github.com/efiminem/pymtodo/archive/v0.2.zip",
     packages=["pymtodo"],
     package_dir={"pymtodo": "src"},
     classifiers=[
         "Development Status :: 2 - Pre-Alpha",
         "License :: OSI Approved :: MIT License",
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
