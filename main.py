from PyQt5 import QtCore, QtGui, QtWidgets
import sqlitems as sql1
import customquerys as querylist

from addform import Ui_Form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.itemclicked = ""
        MainWindow.setObjectName("Data")
        MainWindow.resize(818, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.patient_button = QtWidgets.QPushButton(self.centralwidget)
        self.patient_button.setGeometry(QtCore.QRect(120, 50, 111, 41))
        self.patient_button.setObjectName("patient_button")

        self.pharmacy_button = QtWidgets.QPushButton(self.centralwidget)
        self.pharmacy_button.setGeometry(QtCore.QRect(330, 50, 111, 41))
        self.pharmacy_button.setObjectName("pharmacy_button")

        self.contract_button = QtWidgets.QPushButton(self.centralwidget)
        self.contract_button.setGeometry(QtCore.QRect(540, 50, 111, 41))
        self.contract_button.setObjectName("contract_button")

        self.maindata = QtWidgets.QTableWidget(self.centralwidget)
        self.maindata.setGeometry(QtCore.QRect(110, 120, 531, 311))
        self.maindata.setSizeIncrement(QtCore.QSize(10, 10))
        self.maindata.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.maindata.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.maindata.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.maindata.setObjectName("maindata")
        self.maindata.setColumnCount(0)
        self.maindata.setRowCount(0)
        self.maindata.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.add_item = QtWidgets.QPushButton(self.centralwidget)
        self.add_item.setEnabled(True)
        self.add_item.setGeometry(QtCore.QRect(120, 440, 111, 41))
        self.add_item.setObjectName("add_item")
        self.add_item.hide()

        self.edit_item = QtWidgets.QPushButton(self.centralwidget)
        self.edit_item.setGeometry(QtCore.QRect(330, 440, 111, 41))
        self.edit_item.setObjectName("edit_item")
        self.edit_item.hide()

        self.delete_item = QtWidgets.QPushButton(self.centralwidget)
        self.delete_item.setGeometry(QtCore.QRect(540, 440, 111, 41))
        self.delete_item.setObjectName("delete_item")
        self.delete_item.hide()

        self.custom_queries = QtWidgets.QComboBox(self.centralwidget)
        self.custom_queries.setGeometry(QtCore.QRect(120, 500, 531, 22))
        self.custom_queries.setEditable(False)
        self.custom_queries.setObjectName("custom_queries")
        self.custom_queries.hide()

        self.submit_query = QtWidgets.QPushButton(self.centralwidget)
        self.submit_query.setGeometry(QtCore.QRect(330, 530, 111, 41))
        self.submit_query.setObjectName("submit_query")
        self.submit_query.hide()

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #clicked items
        self.patient_button.clicked.connect(lambda: self.show_button(self.add_item, "Add Patient"))
        self.patient_button.clicked.connect(lambda: self.show_button(self.edit_item, "Get Patient Prescription"))
        self.patient_button.clicked.connect(lambda: self.show_button(self.delete_item, "Delete Patient"))
        self.patient_button.clicked.connect(lambda: self.populate_table(sql.list_all_patients()))
        self.patient_button.clicked.connect(lambda: self.custom_query("patient"))


        self.pharmacy_button.clicked.connect(lambda: self.show_button(self.add_item, "Add Listing"))
        self.pharmacy_button.clicked.connect(lambda: self.show_button(self.edit_item, "List of Drugs"))
        self.pharmacy_button.clicked.connect(lambda: self.show_button(self.delete_item, "Delete Listing"))
        self.pharmacy_button.clicked.connect(lambda: self.populate_table(sql.all_pharm_listings()))
        self.pharmacy_button.clicked.connect(lambda: self.custom_query("prescription"))

        self.contract_button.clicked.connect(lambda: self.show_button(self.add_item, "Add Contract"))
        self.contract_button.clicked.connect(lambda: self.hide_button(self.edit_item))
        self.contract_button.clicked.connect(lambda: self.show_button(self.delete_item, "Delete Contract"))
        self.contract_button.clicked.connect(lambda: self.populate_table(sql.list_contracts()))
        self.contract_button.clicked.connect(lambda: self.custom_query("contracts"))

        self.add_item.clicked.connect(lambda: self.add_form(sql.get_cursor(querylist.add_chooser.get(self.add_item.text())), querylist.add_chooser.get(self.add_item.text())))
        self.edit_item.clicked.connect(lambda: eval(querylist.edit_chooser.get(self.edit_item.text())))
        self.delete_item.clicked.connect(lambda: self.delete_check([self.maindata.horizontalHeaderItem(i).text() for i in range(self.maindata.columnCount())], querylist.del_chooser.get(self.delete_item.text())))
        self.submit_query.clicked.connect(self.submitted_query)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pharmacy Database"))
        self.patient_button.setText(_translate("MainWindow", "Patients"))
        self.pharmacy_button.setText(_translate("MainWindow", "Pharmacy"))
        self.contract_button.setText(_translate("MainWindow", "Contract"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.add_item.setText(_translate("MainWindow", "Add Patient"))
        self.edit_item.setText(_translate("MainWindow", "Edit Patient"))
        self.delete_item.setText(_translate("MainWindow", "Delete Patient"))
        self.custom_queries.setCurrentText(_translate("MainWindow", "Test"))
        self.submit_query.setText(_translate("MainWindow", "Submit Query"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def show_button(self, button, text):
        button.show()
        _translate = QtCore.QCoreApplication.translate
        button.setText(_translate("MainWindow", text))

    def hide_button(self, button):
        button.hide()

    def populate_table(self, items):
        if len(items) == 0:
            self.maindata.setRowCount(0)
            self.maindata.setColumnCount(0)
        else:
            self.maindata.setRowCount(len(items))
            self.maindata.setColumnCount(len(items[0]))
            self.maindata.setHorizontalHeaderLabels(sql.get_cursor_columns())
            for rowindex, row in enumerate(items):
                for colindex, col in enumerate(row):
                    ui.maindata.setItem(rowindex, colindex, QtWidgets.QTableWidgetItem(str(col)))
    
    def custom_query(self, button):
        self.itemclicked = button
        self.custom_queries.clear()
        self.custom_queries.addItem("Add New Custom Query")
        self.custom_queries.show()
        self.submit_query.show()
        items = querylist.chooser.get(button)
        try:
            for i in items:
                self.custom_queries.addItem(i)
        except TypeError:
            pass
           
    def submitted_query(self):
        currenttext = self.custom_queries.currentText()
        if currenttext == "Add New Custom Query":
            self.add_custom_query()
        elif "Add" in currenttext:
            self.add_form(sql.get_cursor(querylist.add_chooser.get(currenttext)), querylist.add_chooser.get(currenttext))
        elif "Delete" in currenttext:
            self.delete_check(sql.get_cursor(querylist.del_chooser.get(self.custom_queries.currentText())), querylist.del_chooser.get(self.custom_queries.currentText()))
        else:
            items = querylist.chooser.get(self.itemclicked)
            for i in items:
                if i == currenttext:
                    functions = items[i]
            items = eval(functions)
            if type(items) is not list:
                self.error_message(items)
            else:
                self.populate_table(items)

    def add_form(self, headers, tables):
        self.my_form = addForm()
        self.my_form.create_text_boxes(len(headers), headers, tables)
        self.my_form.show()

    def delete_row(self, headers, table):
        items = self.maindata.selectedItems()
        check = sql.delete_items(table, headers, items)
        self.error_message(check)
    
    def delete_check(self, headers, table):
        msg = QtWidgets.QMessageBox()
        msg.setText("Are you sure you want to delete this row?")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg.setDefaultButton(QtWidgets.QMessageBox.No)
        msg.buttonClicked.connect(self.confirm_check)
        msg.buttonClicked.connect(lambda: self.confirm(self.choice, "self.delete_row({}, '{}')".format(headers, table)))
        x = msg.exec_()

    def confirm_check(self, i):
        self.choice = i.text()

    def confirm(self, choice, func):
        if choice[1:] == "Yes":
            eval(func)
        else:
            pass

    def get_patient_inquiry(self):
        FormPatient = QtWidgets.QWidget()
        p = patient_enquiry()
        p.setupUi(FormPatient)
        FormPatient.show()

    def get_make_list(self):
        items = sql.make_list()
        self.populate_table(items)

    def add_custom_query(self):
        FormCustom = QtWidgets.QWidget()
        self.custom = custom_sql_query()
        self.custom.setupUi(FormCustom)
        FormCustom.show()
    
    def error_message(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setText(str(text))
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msg.exec_()


class addForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self, sql)
    
    def create_text_boxes(self, num, texts, tables):
        self.ui.create_text_boxes(self, num, texts, tables)

    def closeEvent(self, event):
        self.ui.closeEvent(event)
        event.accept()

class patient_enquiry(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form")
        Form1.resize(527, 221)
        self.label = QtWidgets.QLabel(Form1)
        self.label.setGeometry(QtCore.QRect(220, 10, 161, 21))
        self.label.setObjectName("label")
        self.submit = QtWidgets.QPushButton(Form1)
        self.submit.setGeometry(QtCore.QRect(240, 170, 111, 41))
        self.submit.setObjectName("submit")
        self.plainTextEditName = QtWidgets.QPlainTextEdit(Form1)
        self.plainTextEditName.setGeometry(QtCore.QRect(140, 110, 91, 20))
        self.plainTextEditName.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEditName.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEditName.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditName.setObjectName("plainTextEditName")
        self.name = QtWidgets.QLabel(Form1)
        self.name.setGeometry(QtCore.QRect(160, 80, 47, 13))
        self.name.setScaledContents(True)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.plainTextEditBday = QtWidgets.QPlainTextEdit(Form1)
        self.plainTextEditBday.setGeometry(QtCore.QRect(330, 110, 91, 20))
        self.plainTextEditBday.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditBday.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditBday.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEditBday.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEditBday.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditBday.setObjectName("plainTextEditBday")
        self.birthday = QtWidgets.QLabel(Form1)
        self.birthday.setGeometry(QtCore.QRect(350, 80, 47, 13))
        self.birthday.setScaledContents(True)
        self.birthday.setAlignment(QtCore.Qt.AlignCenter)
        self.birthday.setObjectName("birthday")

        self.submit.clicked.connect(lambda: self.submit_text(Form1))

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter the following information:"))
        self.name.setText(_translate("Form", "Name"))
        self.submit.setText(_translate("Form", "Submit"))
        self.birthday.setText(_translate("Form", "Birthday"))

    def submit_text(self, Form):
        name = self.plainTextEditName.toPlainText()
        birthday = self.plainTextEditBday.toPlainText()
        items = sql.get_patient_enquiry(name, birthday)
        ui.populate_table(items)
        Form.close()

class custom_sql_query(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(504, 196)
        self.label_query = QtWidgets.QLabel(Frame)
        self.label_query.setGeometry(QtCore.QRect(180, 80, 131, 31))
        self.label_query.setAlignment(QtCore.Qt.AlignCenter)
        self.label_query.setObjectName("label_query")
        self.plainTextEditQuery = QtWidgets.QPlainTextEdit(Frame)
        self.plainTextEditQuery.setGeometry(QtCore.QRect(50, 120, 401, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditQuery.sizePolicy().hasHeightForWidth())
        self.plainTextEditQuery.setSizePolicy(sizePolicy)
        self.plainTextEditQuery.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditQuery.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditQuery.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEditQuery.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEditQuery.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditQuery.setObjectName("plainTextEditQuery")
        self.submit_2 = QtWidgets.QPushButton(Frame)
        self.submit_2.setGeometry(QtCore.QRect(190, 150, 111, 41))
        self.submit_2.setObjectName("submit_2")
        self.label_name = QtWidgets.QLabel(Frame)
        self.label_name.setGeometry(QtCore.QRect(180, 10, 131, 31))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.plainTextEditName = QtWidgets.QPlainTextEdit(Frame)
        self.plainTextEditName.setGeometry(QtCore.QRect(50, 50, 401, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditName.sizePolicy().hasHeightForWidth())
        self.plainTextEditName.setSizePolicy(sizePolicy)
        self.plainTextEditName.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEditName.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEditName.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditName.setObjectName("plainTextEditName")


        self.submit_2.clicked.connect(lambda: self.submit_text(Frame))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_query.setText(_translate("Frame", "Enter the Query"))
        self.submit_2.setText(_translate("Frame", "Submit"))
        self.label_name.setText(_translate("Frame", "Enter Formal Name"))

    def submit_text(self, Form):
        query = self.plainTextEditQuery.toPlainText()
        name = self.plainTextEditName.toPlainText()
        chosen_dict = querylist.chooser.get(ui.itemclicked)
        chosen_name = querylist.chooser_name.get((ui.itemclicked))
        dict_append = "{} = {}".format(chosen_name, chosen_dict)

        ui.custom_query(ui.itemclicked)
        items = sql.exec_custom_query(query)
        if type(items) is not list:
            ui.error_message(items)
            Form.close()
        else:
            ui.populate_table(items)
            try:
                fin = open("customquerys.py", "r")
                updated_dict = ""
                for line in fin:
                    newline = line.strip()
                    if dict_append == newline:
                        chosen_dict.update({name:"sql.exec_custom_query('''{}''')".format(query)})
                        dict_new = "{} = {}".format(chosen_name, chosen_dict)
                        newline = newline.replace(dict_append, dict_new)
                    updated_dict += newline + "\n"
                fin.close()
                fout = open("customquerys.py", "w")
                fout.write(updated_dict)
                fout.close()
            except FileNotFoundError as e:
                ui.error_message(e)

            Form.close()

class log_in(object):
    check = ""
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(504, 196)
        self.label_password = QtWidgets.QLabel(Frame)
        self.label_password.setGeometry(QtCore.QRect(180, 80, 131, 31))
        self.label_password.setAlignment(QtCore.Qt.AlignCenter)
        self.label_password.setObjectName("label_password")
        self.plainTextEditPassword = QtWidgets.QPlainTextEdit(Frame)
        self.plainTextEditPassword.setGeometry(QtCore.QRect(50, 120, 401, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditPassword.sizePolicy().hasHeightForWidth())
        self.plainTextEditPassword.setSizePolicy(sizePolicy)
        self.plainTextEditPassword.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditPassword.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditPassword.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEditPassword.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEditPassword.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditPassword.setObjectName("plainTextEditQuery")
        self.submit_2 = QtWidgets.QPushButton(Frame)
        self.submit_2.setGeometry(QtCore.QRect(190, 150, 111, 41))
        self.submit_2.setObjectName("submit_2")
        self.label_name = QtWidgets.QLabel(Frame)
        self.label_name.setGeometry(QtCore.QRect(180, 10, 131, 31))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.plainTextEditName = QtWidgets.QPlainTextEdit(Frame)
        self.plainTextEditName.setGeometry(QtCore.QRect(50, 50, 401, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEditName.sizePolicy().hasHeightForWidth())
        self.plainTextEditName.setSizePolicy(sizePolicy)
        self.plainTextEditName.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEditName.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEditName.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEditName.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEditName.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEditName.setObjectName("plainTextEditName")


        self.submit_2.clicked.connect(lambda: self.submit_text(Frame))

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Log In"))
        self.label_password.setText(_translate("Frame", "Enter Database Password"))
        self.submit_2.setText(_translate("Frame", "Submit"))
        self.label_name.setText(_translate("Frame", "Enter Database Username"))

    def submit_text(self, Form):
        password = self.plainTextEditPassword.toPlainText()
        name = self.plainTextEditName.toPlainText()
        self.check = sql.set_login_info(name, password)
        if self.check is not True:
            msg = QtWidgets.QMessageBox()
            msg.setText(self.check)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            x = msg.exec_()
            sys.exit(1)
        else:
            ui.setupUi(MainWindow)
            MainWindow.show()
        Form.close()
    

if __name__ == "__main__":
    import sys
    sql = sql1.sql()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    Login = QtWidgets.QWidget()
    lg = log_in()
    lg.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())


