CREATE TABLE Pri_Phy_Patient (ssn CHAR(11) PRIMARY KEY,
name CHAR(20),
birth_date DATE,
address CHAR(50),
phy_ssn CHAR(11),
FOREIGN KEY (phy_ssn) REFERENCES Doctor(ssn));

CREATE TABLE Prescription (
pre_id INT(10) AUTO_INCREMENT, 
status CHAR(20),
drop_off_time TIMESTAMP, 
pick_up_time TIMESTAMP,
ssn CHAR(11),
phy_ssn CHAR(11), 
pre_date DATE,
quantity INTEGER,
trade_name CHAR(20),
pharm_co_name CHAR(30),
PRIMARY KEY (pre_id),
FOREIGN KEY (ssn) REFERENCES Pri_Phy_Patient(ssn),
FOREIGN KEY (phy_ssn) REFERENCES Doctor(ssn),
FOREIGN KEY (trade_name, pharm_co_name)
REFERENCES Make_Drug(trade_name, pharm_co_name));

CREATE TABLE Doctor ( 
ssn CHAR(11) PRIMARY KEY,
name CHAR(30),
specialty CHAR(30),
yearsOfExperience INT);

CREATE TABLE Pharmacy ( 
pharm_id CHAR(11) PRIMARY KEY,
name CHAR(30),
address CHAR(30),
phone INTEGER
);

CREATE TABLE Pharm_co (
name CHAR(30) PRIMARY KEY,
phone INTEGER
);

CREATE TABLE Make_Drug (
trade_name CHAR(20),
pharm_co_name CHAR(30),
formula VARCHAR(100),
PRIMARY KEY (trade_name, pharm_co_name),
FOREIGN KEY (pharm_co_name) REFERENCES Pharm_co(name));

CREATE TABLE Sell ( 
price INTEGER,
pharm_id CHAR(11),
trade_name CHAR(20),
pharm_co_name CHAR(30),
PRIMARY KEY (pharm_id, trade_name, pharm_co_name),
FOREIGN KEY (pharm_id) REFERENCES Pharmacy(pharm_id),
FOREIGN KEY (trade_name, pharm_co_name)
REFERENCES Make_Drug(trade_name, pharm_co_name));

CREATE TABLE Contract ( pharm_id CHAR(11),
start_date DATE,
end_date DATE,
text VARCHAR(4000),
supervisor CHAR(20),
pharm_co_name CHAR(30),
PRIMARY KEY (pharm_id, pharm_co_name),
FOREIGN KEY (pharm_id) REFERENCES Pharmacy(pharm_id),
FOREIGN KEY (pharm_co_name) REFERENCES Pharm_co(name));


CREATE TRIGGER deletePatientData 
BEFORE DELETE ON pri_phy_patient
FOR EACH ROW
delete from prescription WHERE prescription.ssn = old.ssn; 

CREATE TRIGGER updateDoctor
BEFORE DELETE ON doctor
FOR EACH ROW
update pri_phy_patient
SET phy_ssn = NULL
WHERE phy_ssn = old.ssn;

CREATE TRIGGER deleteDoctor
BEFORE DELETE ON doctor
FOR EACH ROW
delete from prescription WHERE phy_ssn = old.ssn;