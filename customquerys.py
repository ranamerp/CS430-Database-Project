

patientqueries = {'Get All Unique Patients': 'sql.dist_pat()', 'List All Patients and Patient Prescriptions': 'sql.list_patient_prescriptions()', 'Add Doctor': '', 'List All Doctors': "sql.exec_custom_query('select * from doctor')",  'Delete Doctor': '', 'Add Prescription': '', 'List All Prescriptions': "sql.exec_custom_query('''select * from prescription''')", 'Delete Prescription': ''}

prescriptionqueries = {'List all Unprocessed Prescriptions': 'sql.un_processed()', 'List Pharmaceutical Companies Producing The Most Expensive Drugs': 'sql.most_expensive()', 'List all Ready Prescriptions Not Picked Up': "sql.exec_custom_query('''SELECT * from prescription WHERE pick_up_time = NULL AND status= 'ready' ''')", 'Add Drug': ' ', 'List Drugs Sold in Other Pharmacies': "sql.exec_custom_query('''SELECT sells.trade_name, sells.pharm_id, sells.counts, pharmacy.phone from\n(SELECT trade_name, pharm_id, count(trade_name) as counts from sell GROUP by trade_name ORDER BY counts DESC) as sells , pharmacy\nwhere counts > 1\nand sells.pharm_id = pharmacy.pharm_id;\n''')", "Delete Drug": ''}

contractqueries = {}

chooser = {'patient': patientqueries, 'prescription': prescriptionqueries, 'contract': contractqueries}

chooser_name = {"patient": 'patientqueries', "prescription": 'prescriptionqueries', "contract": 'contractqueries'}

add_chooser = {"Add Patient": "pri_phy_patient","Add Drug": "make_drug","Add Contract": "contract", "Add Doctor":  "doctor", "Add Prescription": "prescription", "Add Listing": "sell"}

del_chooser = {"Delete Patient": "pri_phy_patient","Delete Listing":  "SELL","Delete Contract": "contract", "Delete Doctor": "doctor", "Delete Prescription": "prescription", "Delete Drug": "make_drug"}

edit_chooser = {"Get Patient Prescription": 'self.get_patient_inquiry()',"List of Drugs": "self.get_make_list()","Edit Contract": "self.edit_items()"}
