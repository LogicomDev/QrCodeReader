# This indicates comments; line in grey won't be executed when running

# Libraries importation (this is all the external code that we might want to use. The list below are actually default python libraries
import json  # Handles the JSON data formatting... Which is the same writting as in python ! How convenient :)
import re  # Handles text detection (aka regex) with the use of canvas (that we call patterns)
import time  # Controls time in python (impressive)
import sys  # System related library
import os

# This is our interface made in Qt
import interface
# Loads Qt graphic library
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem, QShortcut, QFileDialog, QMessageBox)
from PyQt5.QtGui import QKeySequence, QColor

# This is a non-standard lib that will help us send requests to the server... because we are too lazy to rewrite it ! ;)
import requests

__version__ = "0.1"

# Here are our "GLOBAL" variables; they can be called wherever we want. Usually you have to avoid doing such variables, but as it's a small script ... we don't care
base_url = "http://api.qrserver.com/v1/read-qr-code/"  # This is the url of the website we are feeding the QRCodes to. It returns our data in JSON format
param_fileurl = ""  # If set, means we try to decode from the web
param_file = ""  # If set, means we try to decode from our computer
param_outputformat = "json"  # Can also be "xml" but not required !

error_color = QColor(255, 165, 0)
ok_color = QColor(255, 255, 255)

PRODUCT = 0
CARTON = 1
PALLET = 2
PRODUCT_TYPE = PRODUCT

"""
This is a comment on multiple lines.

Exemples of JSON Returns
------------------------------------
SUCCESSFUL JSON
[
    {
       "type": "qrcode",
       "symbol":
        [
            {
               "seq": 0,
               "data": "Content of the read QR code",
               "error": null
            }
        ]
    }
]

UNSUCCESSFUL JSON:
[
    {
       "type": "qrcode",
       "symbol":
        [
            {
               "seq": 0,
               "data": null,
               "error": "error description, e.g. \"download error (could not establish connection)\""
            }
        ]
    }
]
"""
# This is our main class


class LogicomQRCodeChecker(QMainWindow):
    """
        This is the main Class
    """

    def __init__(self):
        QMainWindow.__init__(self)
        self.uic = interface.Ui_Interface()
        self.uic.setupUi(self)
        self.issues = []
        self.filepath = ""

        # Here we list all our patterns.
        self.product_pattern = """CTN::SUPPLIERID:(?P<supplier>[0-9]{2});MODEL:(?P<model>.*);QTY:(?P<qty>[0-9]{1,4});CTNNUMBER:(?P<carton>[0-9]{1,4})?;BATCHNUMBER:(?P<batch>[0-9]{6});COLOR:(?P<color>.*);EAN:(?P<ean>[0-9]{13})
(?P<products>(PDT::SN:(?P<lastsn>[0-9]{13});SIM1-IMEI:(?P<lastsim1>[0-9]{14});SIM2-IMEI:(?P<lastsim2>[0-9]{14})
)+)ITF-14::(?P<itf14>[0-9]{13})"""

        self.carton_pattern = """CTN::SUPPLIERID:(?P<supplier>[0-9]{2});MODEL:(?P<model>.*);QTY:(?P<qty>[0-9]{1,4});CTNNUMBER:(?P<carton>[0-9]{1,4});BATCHNUMBER:(?P<batch>[0-9]{6});COLOR:(?P<color>.*);EAN:(?P<ean>[0-9]{13})
(?P<products>(PDT::SN:(?P<lastsn>[0-9]{13});SIM1-IMEI:(?P<lastsim1>[0-9]{14});SIM2-IMEI:(?P<lastsim2>[0-9]{14})
)+)ITF-14::(?P<itf14>[0-9]{13})"""

        self.connect_events()
        self.setFixedSize(500, 570)

    def connect_events(self):
        self.uic.btn_filepath.clicked.connect(self.set_filepath)
        QShortcut(QKeySequence("Ctrl+o"), self, self.set_filepath)

        self.uic.btn_check.clicked.connect(self.check_qrcode_data_integrity)
        QShortcut(QKeySequence("Ctrl+r"), self, self.check_qrcode_data_integrity)

        QShortcut(QKeySequence("Ctrl+q"), self, self.close)

    # Here is a function. This one takes a string parameter in input and return as string as output
    def decode_qrdata_from_file(self):
        files = {'file': open(self.filepath, 'rb')}
        r = requests.post(base_url, files=files)
        qrdata_raw = r.text
        qrdata = json.loads(qrdata_raw)
        # If the request failed, then we return None
        self.data = qrdata[0]["symbol"][0]["data"]

    def set_filepath(self):
        '''
            Opens a dialog to search for QRCode image
        '''
        self.filepath, _ = QFileDialog.getOpenFileName(self, "Select a file", os.path.expanduser("~"))
        try:
            self.uic.filepath.setText(self.filepath)
        except Exception as ex:
            print(ex)

    def show_error_tab(self, display):
        self.uic.tab_results.setTabEnabled(2, display)
        self.uic.tab_error.hide()

    def add_error(self, error_txt):
        numRows = self.uic.table_error.rowCount()
        self.uic.table_error.insertRow(numRows)
        self.uic.table_error.setItem(numRows, 0, QTableWidgetItem(error_txt))

    def check_qrcode_data_integrity(self):
        '''
            This function checks that the qrcode data is actually correct
        '''
        if not self.filepath:
            return

        self.decode_qrdata_from_file()
        self.uic.table_error.setRowCount(0)
        self.uic.table_products.setRowCount(0)
        self.uic.raw_text.setText(self.data)

        if self.uic.cb_label_type.currentText() in ["CARTON", "PALLET"]:
            pattern = re.compile(self.carton_pattern)
        else:
            pattern = re.compile(self.product_pattern)

        if pattern.match(self.data):
            self.uic.validity_result.setText(" GOOD QR CODE FORMAT !")
            self.uic.validity_result.setStyleSheet("background-color: green")
        else:
            self.uic.validity_result.setText(" BAD QR CODE FORMAT !")
#             self.uic.validity_result.setStyleSheet("background-color: rgb(255, 165, 0);")
            self.uic.validity_result.setStyleSheet("background-color: orange")

        # Here we split the string "the old way"
        lines = self.data.split("\n")
        if not lines[0].startswith("CTN::"):
            self.add_error("The QRCode does not start with 'CTN::' !")
        if "PDT" in lines[0]:
            self.add_error("The CTN and PDT lines are not seperated by a CRLF")

        try:
            # Removes the first line and checks integrity
            ctn_line = lines.pop(0)
            ctn_line = ctn_line.replace("CTN::", "")
            ctn_data = ctn_line.split(";")
            for rawstr in ctn_data:
                key, value = rawstr.split(":")

                if not value:
                    self.add_error("Key {} has no value".format(key))

                if key == "SUPPLIERID":
                    self.uic.supplier_id.setText(value)
                    if ";" in value or not value:
                        self.uic.supplier_id.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.supplier_id.setStyleSheet("background-color: white;")
                elif key == "MODEL":
                    self.uic.model_name.setText(value)
                    if ";" in value or not value:
                        self.uic.model_name.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.model_name.setStyleSheet("background-color: white;")
                elif key == "CTNNUMBER":
                    self.uic.ctn_number.setText(value)
                    if ";" in value or not value:
                        self.uic.ctn_number.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.ctn_number.setStyleSheet("background-color: white;")
                elif key == "BATCHNUMBER":
                    self.uic.batch_number.setText(value)
                    if ";" in value or not value:
                        self.uic.batch_number.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.batch_number.setStyleSheet("background-color: white;")
                elif key == "QTY":
                    self.uic.qty_number.setText(value)
                    if ";" in value or not value:
                        self.uic.qty_number.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.qty_number.setStyleSheet("background-color: white;")
                elif key == "COLOR":
                    self.uic.color.setText(value)
                    if ";" in value or not value:
                        self.uic.color.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.color.setStyleSheet("background-color: white;")
                elif key == "EAN":
                    self.uic.ean_13.setText(value)
                    if ";" in value or not value:
                        self.uic.ean_13.setStyleSheet("background-color: orange;")
                    else:
                        self.uic.ean_13.setStyleSheet("background-color: white;")
                else:
                    self.add_error("Unknown key {}".format(key))

        except Exception as ex:
            self.add_error("Can't retrieve all CTN informations")
            self.add_error(str(ex))

        try:
            # Checks all intermediate product lines and checks integrity
            for product_line in lines:
                if product_line.startswith("ITF"):
                    # In case we have reached a ITF, stop parsing for products and start parsing for ITF
                    break

                # Create a empty row at bottom of table
                numRows = self.uic.table_products.rowCount()
                self.uic.table_products.insertRow(numRows)

                if not product_line.startswith("PDT::"):
                    self.add_error("The line '{}' does start with 'PDT::'".format(product_line))

                values = product_line.split(";")

                if len(values) == 3:
                    sn = values[0].replace("PDT::SN:", "")
                    sim1 = values[1].replace("SIM1-IMEI:", "")
                    sim2 = values[2].replace("SIM2-IMEI:", "")
                elif len(values) == 2:
                    sn = values[0].replace("PDT::SN:", "")
                    sim1 = values[1].replace("SIM1-IMEI:", "")
                    sim2 = None
                elif len(values) == 1:
                    sn = values[0].replace("PDT::SN:", "")
                    sim1 = None
                    sim2 = None
                else:
                    self.add_error("The is too much values to unpack in PDT line")

                if sn:
                    self.uic.table_products.setItem(numRows, 0, QTableWidgetItem(sn))
                    if ";" in sn or not sn.isdigit():
                        self.add_error("S/N line contains or ends with text like ';'")
                        item = self.uic.table_products.item(numRows, 0)
                        item.setBackground(error_color)

                if sim1:
                    self.uic.table_products.setItem(numRows, 1, QTableWidgetItem(sim1))
                    if not sim1.startswith("3578"):
                        self.add_error("SIM1-IMEI does not begin by '3578'")
                        self.uic.table_products.item(numRows, 1).setBackground(ok_color)
                    if len(sim1) != 14:
                        self.add_error("SIM1-IMEI has not the correct length(Should be 14 chars, {} found)".format(len(sim1)))
                        self.uic.table_products.item(numRows, 1).setBackground(ok_color)

                if sim2:
                    self.uic.table_products.setItem(numRows, 2, QTableWidgetItem(sim2))
                    if not sim2.startswith("3578"):
                        self.add_error("SIM2-IMEI value does not begin by '3578'")
                        self.uic.table_products.item(numRows, 2).setBackground(ok_color)
                    if len(sim2) != 14:
                        self.add_error("SIM2-IMEI has not the correct length(Should be 14 chars, {} found)".format(len(sim2)))
                        self.uic.table_products.item(numRows, 2).setBackground(ok_color)
        except Exception as ex:
            self.add_error("Can't retrieve all PDT informations")
            self.add_error(str(ex))

        # Removes the last line and checks integrity
        if not lines[-1].startswith("ITF-14::"):
            self.add_error("The QRCode does not end with a ITF-14 line")
            self.uic.itf_14.setText("- - -")
            self.uic.itf_14.setStyleSheet("background-color: orange")
        else:
            itf_14 = lines[-1].replace("ITF-14::", "")
            self.uic.itf_14.setText(itf_14)

            if ";" in value:
                self.uic.itf_14.setStyleSheet("background-color: orange")
                self.add_error("ITF-14 value ends with ';'")
            else:
                self.uic.itf_14.setStyleSheet("background-color: white")

    def closeEvent(self, event):
        """
            Callback on application closing
        """
        ret = QMessageBox.question(self, "Leaving so soon", "Are you sure you want to quit ? :(", QMessageBox.Yes, QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.close()
        else:
            event.ignore()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# This writting below tells the computer to execute this set of instructions
# Everything else above that is not within a function will be executed too... So we have to have a clean code ;)
if __name__ == '__main__':
    # Reactivates Stack Traces for debug
    sys.excepthook = except_hook

    app = QApplication(sys.argv)
    frame = LogicomQRCodeChecker()
    frame.show()
    try:
        sys.exit(app.exec_())
    except Exception as ex:
        print(ex)

#     print("Read BAD QrCode :")
#     # Here, we will store data in a variable as we want to exploit the returned value later on
#     check_qrcode_data_integrity("test_qrcode_bad.png", PRODUCT)
#     time.sleep(2)
#     print("\nRead GOOD QrCode :")
#     check_qrcode_data_integrity("test_qrcode_good.png", PRODUCT)
#     time.sleep(1)
#     print("")
#     check_qrcode_data_integrity("test_qrcode_good.png", CARTON)
