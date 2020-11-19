from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    textboxes = []
    labels = []
    def setupUi(self, Form, sql):
        self.sql =  sql
        Form.setObjectName("Form")
        Form.resize(527, 221)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 10, 161, 21))
        self.label.setObjectName("label")
        self.submit1 = QtWidgets.QPushButton(Form)
        self.submit1.setGeometry(QtCore.QRect(170, 170, 111, 41))
        self.submit1.setObjectName("submit1")

        self.submit1.clicked.connect(lambda: self.submit_text(Form))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Enter the following information:"))
        self.submit1.setText(_translate("Form", "Submit"))

    def create_text_boxes(self, Form, numColumns, listOfHeaders, tables):
        self.currentdb = tables
        self.headerItems = listOfHeaders
        lastx = 0
        for i in range(numColumns):
            self.textbox = QtWidgets.QPlainTextEdit(Form)
            self.newLabel = QtWidgets.QLabel(Form)
            if i == 0:
                lastx = 20
                numsep= -100
            else:
                numsep = (Form.width() - 40) / (91 * numColumns)
                lastx = self.textboxes[i-1].geometry().getRect()[0]
            make_label(self.newLabel, lastx, numsep, listOfHeaders[i], i+1)
            make_text(self.textbox, lastx, numsep, i+1)
            self.textboxes.append(self.textbox)
            self.labels.append(self.newLabel)
    
    def submit_text(self, Form):
        self.finalrow = []
        for item in self.textboxes:
            self.finalrow.append(item.toPlainText())
        flag = self.sql.insert_items(self.currentdb, self.headerItems, self.finalrow)
        msg = QtWidgets.QMessageBox()
        msg.setText(flag)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        x = msg.exec_()
        Form.close()
    
    def closeEvent(self,event):
        self.label.destroy()
        self.textbox.destroy()
        self.newLabel.destroy()
        self.textboxes.clear()
        event.accept()
        

def make_text(item, lastx, numsep, i):
    item.setGeometry(QtCore.QRect(lastx+numsep+110, 110, 91, 20))
    item.setFrameShape(QtWidgets.QFrame.Box)
    item.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    item.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    item.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
    item.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
    item.setObjectName("plainTextEdit_{}".format(i))

def make_label(item, lastx, numsep, text, i): 
    item.setObjectName("label_{}".format(i))
    if i==1:
        item.setGeometry(QtCore.QRect(50, 80, 47, 13))
        lastx=50
    else:
        item.setGeometry(QtCore.QRect(lastx+numsep+20+110, 80, 47, 13))
    item.setAlignment(QtCore.Qt.AlignCenter)
    item.setText(text)
    item.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
