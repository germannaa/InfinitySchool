##Login convertido do arquivo .ui



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(191, 247)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_login = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_login.setGeometry(QtCore.QRect(40, 60, 113, 20))
        self.txt_login.setObjectName("txt_login")
        self.txt_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha.setGeometry(QtCore.QRect(40, 110, 113, 20))
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setObjectName("txt_senha")
        self.lbl_login = QtWidgets.QLabel(self.centralwidget)
        self.lbl_login.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.lbl_login.setObjectName("lbl_login")
        self.lbl_senha = QtWidgets.QLabel(self.centralwidget)
        self.lbl_senha.setGeometry(QtCore.QRect(40, 90, 47, 13))
        self.lbl_senha.setObjectName("lbl_senha")
        self.btn_entrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_entrar.setGeometry(QtCore.QRect(60, 170, 75, 23))
        self.btn_entrar.setObjectName("btn_entrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_login.setText(_translate("MainWindow", "Login"))
        self.lbl_senha.setText(_translate("MainWindow", "Senha"))
        self.btn_entrar.setText(_translate("MainWindow", "Entrar"))
