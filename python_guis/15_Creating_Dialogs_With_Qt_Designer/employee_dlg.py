# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 447)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(parent=Dialog)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok|QtWidgets.QDialogButtonBox.StandardButton.Open|QtWidgets.QDialogButtonBox.StandardButton.Save|QtWidgets.QDialogButtonBox.StandardButton.SaveAll)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.comboBox)
        self.label_4.setBuddy(self.comboBox_2)
        self.label_5.setBuddy(self.doubleSpinBox)
        self.label_6.setBuddy(self.textEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.doubleSpinBox)
        Dialog.setTabOrder(self.doubleSpinBox, self.textEdit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "&Employee Name"))
        self.label_2.setText(_translate("Dialog", "&Employee Date"))
        self.label_3.setText(_translate("Dialog", "&Department"))
        self.label_4.setText(_translate("Dialog", "&Position"))
        self.label_5.setText(_translate("Dialog", "&Annual Salary"))
        self.label_6.setText(_translate("Dialog", "&Job Description"))
