import mysql.connector

user = ''
pw = ''

class sql():
    def dist_pat(self):
        items = []
        self.data.execute("SELECT DISTINCT(name) FROM pri_phy_patient")
        for item in self.data:
            items.append(item)
        return items

    def list_all_patients(self):
        items = []
        self.data.execute("SELECT Patient.name, Patient.birth_date, Patient.address, doctor.name AS doctor_name FROM pri_phy_patient AS Patient, doctor WHERE doctor.ssn = Patient.phy_ssn")
        for item in self.data:
            items.append(item)
        return items

    def list_patient_prescriptions(self):
        items = []
        self.data.execute("""
        SELECT Patient.name, Patient.birth_date, Prescription.pre_id, Prescription.trade_name, 
        Prescription.pharm_co_name, Prescription.status, Prescription.drop_off_time, Prescription.pick_up_time, Prescription.quantity
        FROM Prescription, pri_phy_patient AS Patient
        WHERE Patient.ssn = Prescription.ssn;
        """)
        for item in self.data:
            items.append(item)
        return items


    def ready_but_not_picked(self):
        items = []
        self.data.execute("select * from prescription where status = 'ready' and pick_up = NULL")
        for item in self.data:
            items.append(item[0])
        return items

    def most_expensive(self):
        items = []
        self.data.execute("SELECT pharm_co_name, AVG(price)  from Sell GROUP BY pharm_co_name ORDER BY AVG(price) desc")
        for item in self.data:
            items.append(item)
        return items

    def other_pharmacy(self):
        items = []
        self.data.execute("SELECT sells.trade_name, sells.pharm_id, sells.counts, pharmacy.phone from (SELECT trade_name, pharm_id, count(trade_name) as counts from sell GROUP by trade_name ORDER BY counts DESC) as sells , pharmacy where counts > 1 and sells.pharm_id = pharmacy.pharm_id;")
        for item in self.data:
            items.append(item)
        return items

    def un_processed(self):
        items = []
        self.data.execute("select prescription.* from prescription where status = 'pending';")
        for item in self.data:
            items.append(item)
        return items

    def list_contracts(self):
        items = []
        self.data.execute("select contract.start_date, contract.end_date, contract.supervisor, pharmacy.name as pharm_name, pharm_co.phone as pharm_co_phone, contract.text from contract, pharmacy, pharm_co where contract.pharm_id = pharmacy.pharm_id and contract.pharm_co_name = pharm_co.name;")
        for item in self.data:
            items.append(item)
        return items

    def add_contract(self, newcontract):
        self.data.execute("INSERT INTO contract (pharm_id, start_date, end_date, text, supervisor, pharm_co_name) VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(newcontract[0], newcontract[1], newcontract[2], newcontract[3],newcontract[4],newcontract[5]))

    def get_cursor_columns(self):
        return self.data.column_names

    def all_pharm_listings(self):
        items = []
        self.data.execute("Select p.pharm_co_name, p.trade_name, p.price, pharmacy.name as pharmacy from sell as p, pharmacy where p.pharm_id = pharmacy.pharm_id")
        for item in self.data:
            items.append(item)
        return items

    def get_patient_cursor(self):
        self.data.execute("SELECT * from pri_phy_patient")
        return self.data.column_names

    def get_drug_cursor(self):
        self.data.execute("SELECT * from make_drug")
        return self.data.column_names

    def get_contract_cursor(self):
        self.data.execute("SELECT * from contract")
        return self.data.column_names

    def get_cursor(self, table):
        self.data.execute("SELECT * from {}".format(table))
        return self.data.column_names

    def insert_items(self, table, headers, items):
        try:
            self.data.execute("INSERT INTO {} {} VALUES {}".format(table, str(headers).replace("'", ""), tuple(items)))
            self.db.commit()
            return "Successfully Added!"
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return str(e)


    def delete_items(self, table, headers, items):
        try:
            initstr = "DELETE FROM {} WHERE".format(table)
            for i in range(3):
                string = " {} = '{}' AND".format(headers[i], items[i].text())
                initstr = initstr + string
            self.data.execute(initstr[:-3])
            self.db.commit()
            return "Succesfully Deleted"
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return str(e)

    def get_patient_enquiry(self, name, birthday):
        items = []
        self.data.execute("SELECT patient.name, patient.birth_date, prescription.* from prescription, pri_phy_patient AS patient where patient.name='{}' AND patient.birth_date='{}' AND patient.ssn=prescription.ssn".format(name, birthday))
        for i in self.data:
            items.append(i)
        return items

    def make_list(self):
        items = []
        self.data.execute("select * from make_drug")
        for i in self.data:
            items.append(i)
        return items

    def exec_custom_query(self, text):
        items = []
        try:
            self.data.execute(text)
            for i in self.data:
                items.append(i)
            return items
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return str(e)

    def set_login_info(self, name, password):
        user = name
        pw= password

        try:
            self.db = mysql.connector.connect(user=user, password=pw,
                                        host='localhost',
                                        database='pharmacy')

            self.data = self.db.cursor(buffered=True)
            print("Connected!")
            return True
        except (mysql.connector.Error, mysql.connector.Warning) as e:
            return str(e)