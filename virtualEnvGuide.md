To create a virtual environment:

ensure virtualenv is installed:
    pip install virtualenv

create a new project folder, navigate to that folder in CMD

run:
     python<version> -m venv <virtual-environment-name>
     (this creates a virtual environment called env - it could be named anything)

e.g.
    python3.10 -m venv env 

this will create a directory called "env". to use the virtual enviornment you need to activate it


navigate to: 
    env/Scripts 

and run: 
    activate.bat

to ensure virtual environment is activated run:
    pip list

when virtual env is first created pip list will display only two packages - setuptools and pip. As packages are installed the result of pip list will grow

add env/ directory to .gitignore file

*********************

To install libraries in a virtual env use pip install
to see all installed libraries run:
    pip list

to create a text file listing all project dependencies run:
    pip freeze > requirements.txt

if recreating virtualenv somewhere else, to install all dependencies you can then run:
    pip install -r requirements.txt

*********************

To deactivate your virtualenv run the following code:
     deactivate

*********************
Source:
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/

*********************

When running code in IDE (I am using vscode), make sure to select the correct kernel that corresponds to the python version in the virtual environment

*********************