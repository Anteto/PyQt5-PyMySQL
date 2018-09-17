# coding=utf-8
import sys
import pymysql
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QFrame, QCheckBox, QLineEdit, QLabel, QPushButton, \
    QTextBrowser, QTableWidget, QAbstractItemView, QTableWidgetItem, QMenuBar, QStatusBar
from PyQt5 import QtCore
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='')
        self.cur = self.conn.cursor()
        self.sqlString = "select * from student where "
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(760, 440)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName('frame')

        self.check_sid = QCheckBox(self.frame)
        self.check_sid.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.check_sid.setObjectName('check_sid')

        # self.check_sage = QCheckBox(self.frame)
        # self.check_sage.setGeometry(QtCore.QRect(20, 70, 71, 16))
        # self.check_sage.setObjectName("check_Sage")

        self.check_sname = QCheckBox(self.frame)
        self.check_sname.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.check_sname.setObjectName('check_sname')

        self.check_sgender = QCheckBox(self.frame)
        self.check_sgender.setGeometry(QtCore.QRect(20, 100, 71, 16))
        self.check_sgender.setObjectName('check_sgender')

        self.sid = QLineEdit(self.frame)
        self.sid.setGeometry(QtCore.QRect(90, 10, 113, 16))
        self.sid.setObjectName('sid')

        self.sname = QLineEdit(self.frame)
        self.sname.setGeometry(QtCore.QRect(90, 40, 113, 16))
        self.sname.setObjectName("sname")

        # self.first_sage = QLineEdit(self.frame)
        # self.first_sage.setGeometry(QtCore.QRect(90, 70, 41, 16))
        # self.first_sage.setObjectName("first_sage")

        self.sgender = QLineEdit(self.frame)
        self.sgender.setGeometry(QtCore.QRect(90, 100, 113, 16))
        self.sgender.setObjectName("sgender")

        self.label = QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 70, 16, 16))
        self.label.setObjectName('label')

        self.check_sdept = QCheckBox(self.frame)
        self.check_sdept.setGeometry(QtCore.QRect(270, 40, 71, 16))
        self.check_sdept.setObjectName("check_sdept")
        self.sdept = QLineEdit(self.frame)
        self.sdept.setGeometry(QtCore.QRect(340, 40, 113, 16))
        self.sdept.setObjectName("sdept")

        self.sclass = QLineEdit(self.frame)
        self.sclass.setGeometry(QtCore.QRect(340, 10, 113, 16))
        self.sclass.setObjectName("sclass")
        self.check_sclass = QCheckBox(self.frame)
        self.check_sclass.setGeometry(QtCore.QRect(270, 10, 71, 16))
        self.check_sclass.setObjectName("check_sclass")

        self.find = QPushButton(self.frame)
        self.find.setGeometry(QtCore.QRect(380, 100, 75, 21))
        self.find.setObjectName('find')
        self.find.clicked.connect(self.find_btn)

        self.sql_out = QTextBrowser(self.centralwidget)
        self.sql_out.setGeometry(QtCore.QRect(10, 140, 740, 61))
        self.sql_out.setObjectName('sql_out')

        self.result_out = QTableWidget(self.centralwidget)
        self.result_out.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_out.setGeometry(QtCore.QRect(10, 210, 740, 171))
        self.result_out.setObjectName('result_out')

        self.result_out.setColumnCount(5)
        self.result_out.setRowCount(5)
        self.result_out.resizeColumnsToContents()
        self.result_out.resizeRowsToContents()
        item = QTableWidgetItem()
        self.result_out.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.result_out.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.result_out.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.result_out.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.result_out.setHorizontalHeaderItem(4, item)
        self.result_out.horizontalHeader().setDefaultSectionSize(100)
        self.result_out.horizontalHeader().setMinimumSectionSize(25)
        self.result_out.verticalHeader().setDefaultSectionSize(30)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(675, 390, 75, 21))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.p2_clicked)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def p2_clicked(self):
        self.pyqt_clicked1.emit()

    def find_btn(self):
        self.pyqt_clicked2.emit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.check_sid.setText(_translate("MainWindow", "学号", None))
        # self.check_Sage.setText(_translate("MainWindow", "年龄自", None))
        self.check_sname.setText(_translate("MainWindow", "姓名", None))
        self.check_sgender.setText(_translate("MainWindow", "性别", None))
        # self.label.setText(_translate("MainWindow", "到", None))
        self.check_sdept.setText(_translate("MainWindow", "方向", None))
        self.check_sclass.setText(_translate("MainWindow", "班级", None))
        self.find.setText(_translate("MainWindow", "查询", None))
        self.sql_out.setText(self.sqlString)

        item = self.result_out.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "学号", None))
        item = self.result_out.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名", None))
        item = self.result_out.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别", None))
        item = self.result_out.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "班级", None))
        item = self.result_out.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "专业方向", None))
        self.pushButton_2.setText(_translate("MainWindow", "退出", None))

    def mousePressEvent(self, event):
        print(">_<")

    def buttonTest(self):
        temp_sqlstring = self.sqlString
        is_first = True
        if self.check_sid.isChecked():
            mystr = self.sid.text()
            if is_first:
                is_first = False
                if mystr.find("%") == -1:
                    temp_sqlstring += "sid='" + self.sid.text() + "'"
                else:
                    temp_sqlstring += "sid like'" + self.sid.text() + "'"
            else:
                if mystr.find("%") == -1:
                    temp_sqlstring += " and sid = '" + self.sid.text() + "'"
                else:
                    temp_sqlstring += " and sid like '" + self.sid.text() + "'"

        if self.check_sname.isChecked():
            if is_first:
                mystr = self.sname.text()
                is_first = False
                if mystr.find("%") == -1:
                    temp_sqlstring += "sname = '" + self.sname.text() + "'"
                else:
                    temp_sqlstring += "sname like '" + self.sname.text() + "'"
            else:
                if mystr.find("%") == -1:
                    temp_sqlstring += " and sname = '" + self.sname.text() + "'"
                else:
                    temp_sqlstring += " and sname like '" + self.sname.text() + "'"

        if self.check_sgender.isChecked():
            if is_first:
                is_first = False
                temp_sqlstring += "sgender = '" + self.sgender.text() + "'"
            else:
                temp_sqlstring += " and sgender = '" + self.sgender.text() + "'"

        if self.check_sclass.isChecked():
            if is_first:
                mystr = self.sclass.text()
                is_first = False
                if mystr.find("%") == -1:
                    temp_sqlstring += "sclass = '" + self.sclass.text() + "'"
                else:
                    temp_sqlstring += "sclass like '" + self.sclass.text() + "'"
            else:
                if mystr.find("%") == -1:
                    temp_sqlstring += " and sclass = '" + self.sclass.text() + "'"
                else:
                    temp_sqlstring += " and sclass like '" + self.sclass.text() + "'"

        if self.check_sdept.isChecked():
            if is_first:
                mystr = self.sdept.text()
                is_first = False
                if mystr.find("%") == -1:
                    temp_sqlstring += "sdept = '" + self.sdept.text() + "'"
                else:
                    temp_sqlstring += "sdept like '" + self.sdept.text() + "'"
            else:
                if mystr.find("%") == -1:
                    temp_sqlstring += " and sdept = '" + self.sdept.text() + "'"
                else:
                    temp_sqlstring += " and sdept like '" + self.sdept.text() + "'"

        self.result_out.clearContents()

        if not (is_first):
            print(temp_sqlstring)
            self.cur.execute(temp_sqlstring)
            k = 0
            for i in self.cur:
                print("------------", i)
                w = 0
                for j in i:
                    if type(j) == int:
                        newItem = QTableWidgetItem(str(j))
                    else:
                        newItem = QTableWidgetItem(j)
                    self.result_out.setItem(k, w, newItem)
                    w += 1
                k += 1

        self.sql_out.setText("")
        self.sql_out.append(temp_sqlstring)
        print("find button pressed")

    def buttonExit(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        self.close()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.key_Escape:
            self.buttonExit()


class MyWindow(QMainWindow, Ui_MainWindow):
    pyqt_clicked1 = pyqtSignal()
    pyqt_clicked2 = pyqtSignal()

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pyqt_clicked1.connect(self.buttonExit)
        self.pyqt_clicked2.connect(self.buttonTest)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
