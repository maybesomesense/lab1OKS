from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

bitsNumberComboBoxItems: list[str] = ['8 бит', '7 бит', '6 бит', '5 бит']

class Ui_MainWindow(object):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.serialPort: QSerialPort = QSerialPort()
        self.serialPort.readyRead.connect(self.onRecieveBytes)

    def setupUi(self, MainWindow):
        # Настройки окна
        MainWindow.setObjectName("SerialPort")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # доступные порты
        self.port = QtWidgets.QComboBox(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(190, 430, 101, 21))
        self.port.setObjectName("port")
        self.fillPortNumberComboBox()

        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(140, 100, 271, 101))
        self.input.setObjectName("input")
        self.input.keyPressEvent = self.onInputTextChanged

        # количество бит в байте
        self.count_of_bits_in_byte = QtWidgets.QComboBox(self.centralwidget)
        self.count_of_bits_in_byte.setGeometry(QtCore.QRect(375, 470, 101, 21))
        self.count_of_bits_in_byte.setObjectName("count_of_bits_in_byte")
        self.fillBitsNumberComboBox()


        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(460, 100, 271, 101))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")


        self.label_input = QtWidgets.QLabel(self.centralwidget)
        self.label_input.setGeometry(QtCore.QRect(140, 40, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(22)


        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(460, 40, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")


        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(140, 210, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_status.setFont(font)
        self.label_status.setObjectName("label_status")


        self.label_control = QtWidgets.QLabel(self.centralwidget)
        self.label_control.setGeometry(QtCore.QRect(140, 370, 170, 41))


        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_control.setFont(font)
        self.label_control.setObjectName("label_control")
        self.label_count_of_symbols = QtWidgets.QLabel(self.centralwidget)
        self.label_count_of_symbols.setGeometry(QtCore.QRect(140, 260, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_count_of_symbols.setFont(font)
        self.label_count_of_symbols.setObjectName("label_count_of_symbols")


        self.label_baud_rate = QtWidgets.QLabel(self.centralwidget)
        self.label_baud_rate.setGeometry(QtCore.QRect(140, 300, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_baud_rate.setFont(font)
        self.label_baud_rate.setObjectName("label_baud_rate")


        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 420, 48, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")


        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 460, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")


        self.count_of_received_bytes = QtWidgets.QLineEdit(self.centralwidget)
        self.count_of_received_bytes.setGeometry(QtCore.QRect(400, 270, 71, 21))
        self.count_of_received_bytes.setReadOnly(True)
        self.count_of_received_bytes.setObjectName("count_of_received_bytes")


        self.baud_rate = QtWidgets.QLineEdit(self.centralwidget)
        self.baud_rate.setGeometry(QtCore.QRect(380, 310, 71, 21))
        self.baud_rate.setReadOnly(True)
        self.baud_rate.setObjectName("baud_rate")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.openPort()
        self.port.currentIndexChanged.connect(self.onChangePort)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Последовательный порт"))
        self.label_input.setText(_translate("MainWindow", "Ввод"))
        self.label_output.setText(_translate("MainWindow", "Вывод"))
        self.label_status.setText(_translate("MainWindow", "Статус"))
        self.label_control.setText(_translate("MainWindow", "Контроль"))
        self.label_count_of_symbols.setText(_translate("MainWindow", "Количество переданных байт:"))
        self.label_baud_rate.setText(_translate("MainWindow", "Скорость передачи данных:"))
        self.label_7.setText(_translate("MainWindow", "Порт:"))
        self.label_8.setText(_translate("MainWindow", "Количество битов в байте:"))

    def fillPortNumberComboBox(self):
        availablePorts: list[QSerialPortInfo] = QSerialPortInfo.availablePorts()
        currentPort: str = self.port.currentText()
        if availablePorts:
            self.port.blockSignals(True)
            self.port.clear()

            for availablePort in availablePorts:
                self.port.addItem(availablePort.portName())

            currentIndex: int = self.port.findText(currentPort)

            if currentIndex != -1:
                self.port.setCurrentIndex(currentIndex)

            self.port.blockSignals(False)
        else:
            QMessageBox.warning(None, "Error", "No available COM Ports")
            sys.exit(app.exec_())


    def fillBitsNumberComboBox(self):
        self.count_of_bits_in_byte.clear()
        for item in bitsNumberComboBoxItems:
            self.count_of_bits_in_byte.addItem(item)

            
    def openPort(self):
            if not self.serialPort.isOpen():
                self.configurePort()
                if not self.tryOpenPort(self.serialPort.portName()):
                    availablePorts: list[QSerialPortInfo] = QSerialPortInfo.availablePorts()
                    for availablePort in availablePorts:
                        if self.tryOpenPort(availablePort.portName()):
                            self.port.setCurrentText(availablePort.portName())
                            self.serialPort.setPortName(availablePort.portName())
                            break
                    else:
                        QMessageBox.warning(None, "Ошибка", "Нет доступных COM-портов")
                        sys.exit(app.exec_())
                self.serialPort.open(QtCore.QIODevice.ReadWrite)

                
    def tryOpenPort(self, portName: str) -> bool:
        port: QSerialPort = QSerialPort()
        port.setPortName(portName)
        if port.open(QtCore.QIODevice.ReadWrite):
            port.close()
            return True
        else:
            return False
        
            
    def configurePort(self):
        portName: str = self.port.currentText()
        self.serialPort.setPortName(portName)
        
        baudRate: int = 9600
        self.serialPort.setBaudRate(baudRate)
        
        dataBits: int = int(self.count_of_bits_in_byte.currentText()[0])
        self.serialPort.setDataBits(dataBits)
        
        self.serialPort.setParity(QSerialPort.Parity.NoParity)
        self.serialPort.setStopBits(QSerialPort.StopBits.OneStop)
        self.serialPort.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
            

    def onInputTextChanged(self, event):
        QtWidgets.QTextEdit.keyPressEvent(self.input, event)
        if event.key() == QtCore.Qt.Key_Return:
            self.onSendBytes()

            

            
    def onSendBytes(self):
        text: str = self.input.toPlainText().replace("\n","")
        sendedBytesCount: int = len(text)
        self.serialPort.write(text.encode())
        self.input.clear()
        self.count_of_received_bytes.setText(str(sendedBytesCount))
        self.baud_rate.setText(str(self.serialPort.baudRate()))
        
        
    def onRecieveBytes(self):
        text = self.serialPort.readAll().data()
        if len(text) == 0:
            QMessageBox.warning(None, "Ошибка", "Нельзя прочесть данные из порта")
            sys.exit(app.exec_())
        else:
            self.output.setText(text.decode())
            
            
    def onChangePort(self, index):
        if self.serialPort.isOpen():
            self.serialPort.close()
        self.fillBitsNumberComboBox()
        self.fillPortNumberComboBox()
        self.openPort()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
