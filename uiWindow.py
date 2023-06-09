# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        self.labelPath.setText("")
        self.labelPath.setObjectName("labelPath")
        self.horizontalLayout_4.addWidget(self.labelPath)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBoxPath = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxPath.setObjectName("groupBoxPath")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBoxPath)
        self.verticalLayout_5.setContentsMargins(-1, 5, 2, -1)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBoxPath)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnChooseFile = QtWidgets.QPushButton(self.frame_2)
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.horizontalLayout_2.addWidget(self.btnChooseFile)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_7.addWidget(self.frame_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.tab_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnChooseFolder = QtWidgets.QPushButton(self.frame_3)
        self.btnChooseFolder.setObjectName("btnChooseFolder")
        self.horizontalLayout_3.addWidget(self.btnChooseFolder)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cbMpegFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbMpegFile.setChecked(True)
        self.cbMpegFile.setObjectName("cbMpegFile")
        self.gridLayout_3.addWidget(self.cbMpegFile, 1, 1, 1, 1)
        self.cbTsFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbTsFile.setChecked(True)
        self.cbTsFile.setObjectName("cbTsFile")
        self.gridLayout_3.addWidget(self.cbTsFile, 1, 3, 1, 1)
        self.cbAviFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbAviFile.setChecked(True)
        self.cbAviFile.setObjectName("cbAviFile")
        self.gridLayout_3.addWidget(self.cbAviFile, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 8, 0, 1, 4)
        self.cbMp4File = QtWidgets.QCheckBox(self.groupBox)
        self.cbMp4File.setChecked(True)
        self.cbMp4File.setObjectName("cbMp4File")
        self.gridLayout_3.addWidget(self.cbMp4File, 0, 0, 1, 1)
        self.cbWmvFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbWmvFile.setChecked(True)
        self.cbWmvFile.setObjectName("cbWmvFile")
        self.gridLayout_3.addWidget(self.cbWmvFile, 1, 0, 1, 1)
        self.cbMkvFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbMkvFile.setChecked(True)
        self.cbMkvFile.setObjectName("cbMkvFile")
        self.gridLayout_3.addWidget(self.cbMkvFile, 1, 2, 1, 1)
        self.cbRmFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbRmFile.setChecked(True)
        self.cbRmFile.setObjectName("cbRmFile")
        self.gridLayout_3.addWidget(self.cbRmFile, 2, 0, 1, 1)
        self.cbMovFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbMovFile.setChecked(True)
        self.cbMovFile.setObjectName("cbMovFile")
        self.gridLayout_3.addWidget(self.cbMovFile, 0, 1, 1, 1)
        self.cbFlvFile = QtWidgets.QCheckBox(self.groupBox)
        self.cbFlvFile.setChecked(True)
        self.cbFlvFile.setObjectName("cbFlvFile")
        self.gridLayout_3.addWidget(self.cbFlvFile, 0, 3, 1, 1)
        self.leditCustomEncode = QtWidgets.QLineEdit(self.groupBox)
        self.leditCustomEncode.setObjectName("leditCustomEncode")
        self.gridLayout_3.addWidget(self.leditCustomEncode, 6, 0, 1, 2)
        self.btnCustomCheck = QtWidgets.QPushButton(self.groupBox)
        self.btnCustomCheck.setObjectName("btnCustomCheck")
        self.gridLayout_3.addWidget(self.btnCustomCheck, 6, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 4)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout_8.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_9.addWidget(self.groupBoxPath)
        self.groupBoxEncode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEncode.setObjectName("groupBoxEncode")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxEncode)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBoxEncode)
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.groupBoxEncode)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_9.addWidget(self.groupBoxEncode)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.btnTransmit = QtWidgets.QPushButton(self.centralwidget)
        self.btnTransmit.setObjectName("btnTransmit")
        self.horizontalLayout_6.addWidget(self.btnTransmit)
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_6.addWidget(self.btnClear)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NercDTV编码转换工具V1.0.1(2023.06.09)"))
        self.label_2.setText(_translate("MainWindow", "当前路径:"))
        self.groupBoxPath.setTitle(_translate("MainWindow", "路径设置"))
        self.btnChooseFile.setText(_translate("MainWindow", "选择文件..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "选择文件"))
        self.btnChooseFolder.setText(_translate("MainWindow", "选择文件夹..."))
        self.groupBox.setTitle(_translate("MainWindow", "递归处理文件夹中以下类型"))
        self.cbMpegFile.setText(_translate("MainWindow", ".mpeg"))
        self.cbTsFile.setText(_translate("MainWindow", ".ts"))
        self.cbAviFile.setText(_translate("MainWindow", ".avi"))
        self.label_3.setText(_translate("MainWindow", "自定义用空格分开,如：.mp3 .vob"))
        self.cbMp4File.setText(_translate("MainWindow", ".mp4"))
        self.cbWmvFile.setText(_translate("MainWindow", ".wmv"))
        self.cbMkvFile.setText(_translate("MainWindow", ".mkv"))
        self.cbRmFile.setText(_translate("MainWindow", ".rmvb"))
        self.cbMovFile.setText(_translate("MainWindow", ".mov"))
        self.cbFlvFile.setText(_translate("MainWindow", ".flv"))
        self.btnCustomCheck.setText(_translate("MainWindow", "应用"))
        self.label.setText(_translate("MainWindow", "自定义类型"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "选择文件夹"))
        self.groupBoxEncode.setTitle(_translate("MainWindow", "编码设置"))
        self.label_4.setText(_translate("MainWindow", "转换后的编码:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "NercDTV Key 01"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-END-"))
        self.btnTransmit.setText(_translate("MainWindow", "转换"))
        self.btnClear.setText(_translate("MainWindow", "清屏"))
