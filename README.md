# MongoDB Flask Application 

This is a flask based web application used to normalizes company names and export the data to a MongoDB database.It takes an SQL database, reads and updates it with normalized company names. Then it takes the company data and writes it to a MongoDB database. Finally it reads the MongoDB database and displays it in a html table.


## Getting Started

Before importing this project to your Python workspace, it is necessary we make sure the prerequisite steps are properly done in your development environment. The installation procedure described in this documentation will assume you already have Python installed on your computer.

#### Prerequisites

+ A Python Editor of your choice
For this project, the [PyCharm](https://www.jetbrains.com/pycharm/) IDE and but the same is not required to correctly deploy the application itself.

+ Install the virtual environment package
Virtual Environment (virtualenv) is a tool to create isolated Python environments. The virtualenv command creates a folder that contains all the necessary executables to use the packages that a Python project would need. The same can be installed as described in [this link](http://docs.python-guide.org/en/latest/dev/virtualenvs/) through the following command:


```bash
python -m pip install --user virtualenv
```
---
#### Installing

The incoming steps below will guide you through the project installation.
The following commands should be executed in your computer console in the project folder:

+ Clone the project to your local repository workspace
+ Create a virtual environment for the imported application through the following command:
---
> Mac command:

```
python3 -m venv venv
```
---
+ Activate your virtual environment with the command

> Mac command:

```
source venv/bin/activate
```

+ With the virtual environment properly activated, install the plugins available in the requirements.txt file through the command:

```
pip install -r requirements.txt
```
This process should enable your application to be deployed on a local server for test purposes.


## Deployment

With the webapp.py file and the virtual environment activated, the python application should run through the following command:

>Mac command:

```
python webapp.py

```
The same will enable the project to be accessed by your web browser through a URL displayed by the mentioned command execution.

## Technologies Used

### Languages

+ [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - build up the 
+ [Python](https://www.python.org/) - to build back-end functionalities handling data and database interaction.

### Programs and Tools

+ [Py Charm]( https://www.jetbrains.com/pycharm/) - the code editor being used to build the project.
+ [Git](https://git-scm.com/) - the built-in Git feature in VS Code was used for version control and push to GitHub.
+ [Github](https://github.com/) - GitHub is used to store project code remotely.
+ [SQLite3](https://sqlite.org/) - the database used to clean the data into plain text.
+ [MongoDB](https://www.mongodb.com/) - the database being used to store encrypted data and queries.

### Frameworks and Libraries

+ [Bootstrap v5.1](https://getbootstrap.com/) - the responsive front-end framework to build the layout and style the app.
+ [jQuery](https://jquery.com/) - a JavaScript library used for the simplicity of traversing HTML documents and manipulation, event handling, and Ajax.
+ [Flask](https://palletsprojects.com/p/flask/) - a micro web framework written in Python which is the barebone of this stock management app.
+ [PyMongo](https://pymongo.readthedocs.io/en/stable/) - Python distribution containing tools for working with MongoDB.
+ [Pandas](https://pandas.pydata.org/) - Python library used to work with the SQLite3 database.
+ [Cleanco](https://pypi.org/project/cleanco/) - Python package that processes company names, providing cleaned versions of the names.


## Contact

Stefani Kuzmanovska - stefanikuzmanovska@hotmail.com

Project Link: https://github.com/Stefi28/MongoDB-Flask-application


