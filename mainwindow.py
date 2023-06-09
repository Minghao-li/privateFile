'''
@Author: your name
@Date: 2020-03-13 09:44:52
@LastEditTime: 2020-03-16 15:21:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \codeTransmit\mainwindow.py
'''
# This Python file uses the following encoding: utf-8
import sys
import os
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QCheckBox, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Qt, QThread, Signal
from uiWindow import Ui_MainWindow

import codecs
import chardet
import threading
import time

# 转换后的编码类型
UTF8_BOM = 0
UTF8 = 1
GB2312 = 2

FILE = 0
FOLDER = 1

class convertThread(QThread):
    updated = Signal(float)
    show = Signal(str,Exception)
    running = False
    filePath = ""
    progPercent = 0.0
    out_enc = "NERCDTV-S1"

    def convert(self):
        ext = os.path.splitext(self.filePath)
        outputfilePath = ext[0] +'.nerc'
        file_size = os.path.getsize(self.filePath)
        if os.path.exists(outputfilePath):  os.remove(outputfilePath)
        count = 0

        try:
            f2 = open(outputfilePath, 'wb')

            with open(self.filePath, 'rb') as f:
                rd = bytearray(f.read(1024 * 1024))
                while len(rd) != 0:
                    for n, v in enumerate(rd):
                        rd[n] = v ^ 255
                    f2.write(rd)
                    self.progPercent = (((1024 * 1024 * count + len(rd)) / file_size) * 100)
                    self.updated.emit(float(self.progPercent))
                    self.show.emit(self.filePath, str((1024 * 1024 * count + len(rd))/1024/1024) + "M/" + str(round((file_size/1024/1024),2)) + "M")
                    rd = bytearray(f.read(1024 * 1024))
                    count += 1
            f2.close()
            f.close()
            self.show.emit(self.filePath, "文件加密成功，已导出到路径=>" + outputfilePath)
            self.stop()
        except Exception as err:
            self.show.emit(self.filePath, err)
            f2.close()
            f.close()
            self.stop()

    def __init__(self, parent=None):
        super(convertThread, self).__init__(parent)
        self.progPercent = 0
        self.running = True


    def run(self):
        while self.running:
            self.convert()

    def stop(self):
        self.running = False

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initForm()
        self.connectSlots()

        self.__path = None  # 处理的文件/文件夹路径
        self.__fileSuffix = ['.mp4', '.mov', '.avi', '.flv', '.wmv', '.mpeg', '.mkv', '.ts', '.rm',
                             '.rmvb']  # 内置可勾选的文件类型
        self.__customFileSuffix = []  # 自定义的文件类型
        self.__encodeType = 'NERCDTV-01FF'  # 默认的编码类型
        #self.__encodeTypeArr = ['NERCDTV-01FF', 'NERCDTV-00FF', 'NERCDTV-02FF']
        self.__encodeTypeArr = ['NERCDTV-01FF']
        self.__fileOrFolder = FOLDER  # 默认处理文件夹
        self.__mWorker = None  # 私有线程变量

        self.progPercent = 0
        self.convertT = None

    def initForm(self):
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["文件名", "转码状态"])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setColumnWidth(0, 165)
        self.ui.tableWidget.setColumnWidth(1, 70)
        self.ui.progressBar.setValue(0)
        self.ui.progressBar.setMaximum(100)

    def setFilePath(self, path):
        self.__path = path

    def getFileSuffix(self):
        return self.__fileSuffix

    def addFileSuffix(self, item):
        self.__fileSuffix.append(item)

    def removeFileSuffix(self, item):
        self.__fileSuffix.remove(item)

    def clearFileSuffix(self):
        self.__fileSuffix.clear()

    def setEncodeType(self, type):
        self.__encodeType = type

    def connectSlots(self):
        self.ui.btnChooseFolder.clicked.connect(self.onOpenFolderClicked)
        self.ui.btnChooseFile.clicked.connect(self.onOpenFileClicked)
        self.ui.btnClear.clicked.connect(self.onBtnClearClicked)
        self.ui.comboBox.currentIndexChanged.connect(self.onCbEncodeIndexChanged)
        self.ui.btnCustomCheck.clicked.connect(self.onCustomEncodeCheck)
        fileTypeArr = self.ui.groupBox.findChildren(QCheckBox)
        for index, item in enumerate(fileTypeArr):
            item.stateChanged.connect(self.onFileTypeChanged)
        self.ui.btnTransmit.clicked.connect(self.onTransmitClicked)

    def onOpenFileClicked(self):
        fileName = QFileDialog.getOpenFileName(self, "", ".")
        if (fileName is None):
            self.ui.textBrowser.append("open file failed: fileName is None!")
            return

        self.setFilePath(fileName[0])
        self.__fileOrFolder = FILE
        self.ui.labelPath.setText(fileName[0])

    def onOpenFolderClicked(self):
        folderName = QFileDialog.getExistingDirectory(self, "", ".")
        if (folderName is None):
            self.ui.textBrowser.append("open folder failed:folderName is None!")
            return

        self.setFilePath(folderName)
        self.__fileOrFolder = FOLDER
        self.ui.labelPath.setText(folderName)

    def onBtnClearClicked(self):
        self.ui.textBrowser.clear()
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

    def onCbEncodeIndexChanged(self, index):
        self.setEncodeType(self.__encodeTypeArr[index])
        self.ui.textBrowser.append("Set encodeType: %s" % self.__encodeTypeArr[index])

    def onCustomEncodeCheck(self):
        customStr = self.ui.leditCustomEncode.text()
        customArr = customStr.split(' ')

        for index, item in enumerate(customArr):
            if (len(item) < 2):
                QMessageBox.critical(self, "Error!", "自定义后缀无效:长度至少为2!")
                return
            if (item[0] != '.'):
                QMessageBox.critical(self, "Error!", "自定义后缀无效:必须以 '.' 打头!")
                return
            if (item.count('.', ) > 1):
                QMessageBox.critical(self, "Error!", "自定义后缀无效:一种格式中不能出现多个 '.'!")
                return
            # 移除后缀重复的元素
            if (item not in self.__fileSuffix) and (item not in self.__customFileSuffix):
                self.__customFileSuffix.append(item)

    def onFileTypeChanged(self, state):
        checkBox = QCheckBox.sender(self)
        itemText = checkBox.text()
        if (False == state):
            if itemText in self.__fileSuffix:
                self.removeFileSuffix(itemText)
        else:
            if itemText not in self.__fileSuffix:
                self.addFileSuffix(itemText)
            if itemText in self.__customFileSuffix:
                self.__customFileSuffix.remove(itemText)

    def enableWidgets(self, enabled):
        self.ui.groupBoxPath.setEnabled(enabled)
        self.ui.groupBoxEncode.setEnabled(enabled)
        self.ui.btnTransmit.setEnabled(enabled)
        self.ui.btnClear.setEnabled(enabled)

    def onTransmitClicked(self):
        if self.__path is None:
            QMessageBox.warning(self, "Warning!", "请先选择'文件'或'文件夹'路径!")
            return

        #self.ui.tableWidget.clearContents()
        #self.ui.tableWidget.setRowCount(0)

        if self.__fileOrFolder == FILE:
            self.convertT = convertThread(self)
            self.convertT.filePath = self.__path
            self.convertT.out_enc = self.__encodeType
            self.convertT.updated.connect(self.updateValue)
            self.convertT.show.connect(self.addShow)
            self.convertT.start()

            #self.convert(self.__path, self.__encodeType)
        elif self.__fileOrFolder == FOLDER:
            if 0 == len(self.__fileSuffix) and 0 == len(self.__customFileSuffix):
                QMessageBox.critical(self, "Error!", "请设置需要处理的文件后缀格式!")
                return
            self.enableWidgets(False)
            self.__mWorker = threading.Thread(target=self.explore, args=(self.__path,))
            self.__mWorker.start()
        else:
            QMessageBox.critical(self, "Error!", "文件类型错误，无法转换!")
        QApplication.processEvents()

    def explore(self, dir):
        for root, dirs, files in os.walk(dir):
            for file in files:
                suffix = os.path.splitext(file)[1]
                # if suffix == '.h' or suffix == '.c' or suffix == '.cpp' or suffix == '.hpp' or suffix == '.bat': 
                #     path = os.path.join(root,file)
                #     self.convert(path)
                if self.__fileSuffix:
                    for item in self.__fileSuffix:
                        if (item == suffix):
                            path = os.path.join(root, file)
                            self.convertT = convertThread(self)
                            self.convertT.filePath = path
                            self.convertT.out_enc = self.__encodeType
                            self.convertT.updated.connect(self.updateValue)
                            self.convertT.show.connect(self.addShow)
                            self.convertT.start()
                            while self.convertT.running:
                                time.sleep(1)
                            #self.convert(path, self.__encodeType)
                if self.__customFileSuffix:
                    for item in self.__customFileSuffix:
                        if (item == suffix):
                            path = os.path.join(root, file)
                            self.convertT = convertThread(self)
                            self.convertT.filePath = path
                            self.convertT.out_enc = self.__encodeType
                            self.convertT.updated.connect(self.updateValue)
                            self.convertT.show.connect(self.addShow)
                            self.convertT.start()
                            while self.convertT.running:
                                time.sleep(1)
                            #self.convert(path, self.__encodeType)

        self.ui.textBrowser.append("explore over!")
        self.enableWidgets(True)


    def updateValue(self, data):
        self.ui.progressBar.setValue(data)

    def addShow(self, filePath, err):
        self.ui.textBrowser.append("%s 转码中:%s" % (filePath, err))
        if "成功" in err:
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            file = QTableWidgetItem(filePath)
            self.ui.tableWidget.setItem(row_count, 0, file)
            self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem("完成"))

    def convert(self):
        global filePath
        global encodeType
        convert(self, filePath, encodeType)

    def convert(self, filePath, out_enc="NERCDTV-S1"):
        ext = os.path.splitext(filePath)
        # 不要显示.01ff的编码信息
        #outputfilePath = ext[0] + '.01ff'+'.nerc'
        outputfilePath = ext[0] + '.nerc'
        file_size = os.path.getsize(filePath)
        count = 0

        try:
            f2 = open(outputfilePath, 'wb')

            with open(filePath, 'rb') as f:
                rd = bytearray(f.read(1024 * 1024))
                while len(rd) != 0:
                    for n, v in enumerate(rd):
                        rd[n] = v ^ 255
                    f2.write(rd)
                    count += 1
                    self.progPercent = (float(1024 * 1024 * count / file_size) * 100)
                    rd = bytearray(f.read(10240 * 1024))
            f2.close()
            f.close()
            self.convertT.stop()
        except Exception as err:
            self.ui.textBrowser.append("%s:%s" % (filePath, err))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
