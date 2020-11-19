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

From here, the window will look blank. You can click on one of the 3 boxes to load a default database. This data is directly from the interface. 

#### Adding a Row
There are multiple options to add rows to certain tables. You can either click on one of the "Add" buttons, or use some of the custom queries. When adding, the item will only be added **to that specific table**. For example: if I click "Add Patient", then the pop up will get columns from that specific table. 

#### Deleting a Row
To delete a row, you must select the row in the database. For example, to delete a doctor, you can click on "List All Doctors" in the custom query, and then select a doctor row, then click "Delete Doctor" from the custom query. This process is similar to the Add Row, in that it only deletes rows from **specific tables**. 

#### Custom Queries
This program allows you to run custom sql queries. You can click "Add New Custom Query", and then run normal SQL code. This query will then be saved and will be able to be loaded up at later times. 


## Important Notes
The text boxes used throughout this program do not support keyboard functions (so you cannout use Tab to switch between boxes, nor use Enter to submit a query). Furthermore, the "Add Item" box does not automatically resize based on how many items are in it, meaning you will have to manually resize each time. 

The code works under the pretense that all items are named according to the database design (found in the batch_create.sql file). Any changes to this design will most likely break the code. 

### If you have any questions, please contact me at prem.rana@siu.edu
