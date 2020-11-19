# CS430-Database-Project
This was our project for CS430 where we had to create a database and a GUI to interface with it.


## Requirements
#### Python Requirements:
  -Python 3.8
  -Pip
  -PyQt5
  -MySQL Connector

#### Other Requirements:
  -Working MySQL database. This project is primarily a GUI interface to a MySQL database, and will not run properally without one operating. You can download MySQL here: https://www.mysql.com/downloads/
  

## Installation

To install the required pip modules, you can run `pip install -r requirements.txt` to install the rest of the required modules. 

You can follow this guide to install MySQL: https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/

## Running the program.

In order to run the program, you must have a MySQL instance running. Make sure all python files are in the same folder, and you can do `python ui_database.py` to run the program. The first window that will showup is the login box. Please use the same credentials that you would use to access your MySQL instance. (Note: If your host ip is not run locally, you will need to go into `sqlitems.py` and change the self.db host to the ip that your MySQL instance is running on. This can be found in def_set_login_info (at the bottom of the script). 

From here, the window will look blank. You can click on one of the 3 boxes to load a default database. 
