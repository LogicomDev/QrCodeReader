import kivy
kivy.require('1.0.9')

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
# FIXME this shouldn't be necessary
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import time
import os
import requests
import json
import re
import sys


PRODUCT = "Product"
CARTON = "Carton"
PALLET = "Pallet"


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class QrCode(Widget):
    source = StringProperty(None)
    last_image = ""
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    rawtext = StringProperty()
    itf = StringProperty()
    ean = StringProperty()
    color = StringProperty()
    qty = StringProperty()
    supplier = StringProperty()
    batchnb = StringProperty()
    cartonnb = StringProperty()
    model = StringProperty()
    verdict = StringProperty()
    product_type = StringProperty()
    rgb = StringProperty()
    rgb = [50, 50, 50]

    def __init__(self, **kwargs):
        super(QrCode, self).__init__(**kwargs)
        """
        Ugly patch to creates private variables...
        """
        self.issues = []
        self.filepath = ""

        self.product_pattern = """CTN::SUPPLIERID:(?P<supplier>[0-9]{2});MODEL:(?P<model>.*);QTY:(?P<qty>[0-9]{1,4});CTNNUMBER:(?P<carton>[0-9]{1,4})?;BATCHNUMBER:(?P<batch>[0-9]{6});COLOR:(?P<color>.*);EAN:(?P<ean>[0-9]{13})
(?P<products>(PDT::SN:(?P<lastsn>[0-9]{13});SIM1-IMEI:(?P<lastsim1>[0-9]{14});SIM2-IMEI:(?P<lastsim2>[0-9]{14})
)+)ITF-14::(?P<itf14>[0-9]{13})"""

        self.carton_pattern = """CTN::SUPPLIERID:(?P<supplier>[0-9]{2});MODEL:(?P<model>.*);QTY:(?P<qty>[0-9]{1,4});CTNNUMBER:(?P<carton>[0-9]{1,4});BATCHNUMBER:(?P<batch>[0-9]{6});COLOR:(?P<color>.*);EAN:(?P<ean>[0-9]{13})
(?P<products>(PDT::SN:(?P<lastsn>[0-9]{13});SIM1-IMEI:(?P<lastsim1>[0-9]{14});SIM2-IMEI:(?P<lastsim2>[0-9]{14})
)+)ITF-14::(?P<itf14>[0-9]{13})"""

        __version__ = "0.1"

        # For decoding the picture
        self.base_url = "http://api.qrserver.com/v1/read-qr-code/"
        self.param_fileurl = ""
        self.param_file = ""
        self.param_outputformat = "json"

        # Color picker
        self.error_color = [255, 165, 0]
        self.ok_color = [255, 255, 255]

        self.product_type = PRODUCT

    def dismiss_popup(self):
        """
        Dismiss the pop-up cleanly
        """
        self._popup.dismiss()

    def load(self, path, filename):
        """
        Loads the filepath from the pop-up
        """
        self.filepath = filename[0]
        self.dismiss_popup()
        self.check_qrcode_data_integrity()

    def capture_picture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date then parse them
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

    def select_picture(self):
        '''
        Function to retrieve the QrCode image and parse them
        '''
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()

    def decode_qrdata_from_file(self):
        """
        Send the picture to the website and waits for it's data returns
        """
        files = {'file': open(self.filepath, 'rb')}
        r = requests.post(self.base_url, files=files)
        qrdata_raw = r.text
        qrdata = json.loads(qrdata_raw)
        # If the request failed, then we return None
        self.data = qrdata[0]["symbol"][0]["data"]

    def add_error(self, msg):
        print(msg)

    def check_integrity(self, item, value):
        """
        Makes sure that the value is not faulty (spaces or ';' in the text)
        """
        print("'" + value + "'")
        if ";" in value or not value:
            item.background_color = [1, 0, 0, 1]
        else:
            item.background_color = [0, 1, 0, 1]

    def check_qrcode_data_integrity(self):
        '''
        This function checks that the qrcode data is actually correct
        '''
        if not self.filepath:
            return

        self.decode_qrdata_from_file()
#         self.uic.table_error.setRowCount(0)
#         self.uic.table_products.setRowCount(0)
        self.rawtext = self.data.replace("\n", "$\n")

        if self.product_type in ["CARTON", "PALLET"]:
            pattern = re.compile(self.carton_pattern)
        else:
            pattern = re.compile(self.product_pattern)

        if pattern.match(self.data):
            self.verdict = "GOOD QR CODE FORMAT !"
            self.ids.txt_verdict.background_color = [0, 1, 0, 1]
        else:
            self.verdict = "BAD QR CODE FORMAT !"
            self.ids.txt_verdict.background_color = [1, 0, 0, 1]

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
                    self.supplier = value
                    self.check_integrity(self.ids.txt_supplier, value)
                elif key == "MODEL":
                    self.model = value
                    self.check_integrity(self.ids.txt_model, value)
                elif key == "CTNNUMBER":
                    self.cartonnb = value
                    self.check_integrity(self.ids.txt_cartonnb, value)
                elif key == "BATCHNUMBER":
                    self.batchnb = value
                    self.check_integrity(self.ids.txt_batchnb, value)
                elif key == "QTY":
                    self.qty = value
                    self.check_integrity(self.ids.txt_qty, value)
                elif key == "COLOR":
                    self.color = value
                    self.check_integrity(self.ids.txt_color, value)
                elif key == "EAN":
                    self.ean = value
                    self.check_integrity(self.ids.txt_ean, value)
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
#                 numRows = self.uic.table_products.rowCount()
#                 self.uic.table_products.insertRow(numRows)

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

#                 if sn:
#                     self.uic.table_products.setItem(numRows, 0, QTableWidgetItem(sn))
#                     if ";" in sn or not sn.isdigit():
#                         self.add_error("S/N line contains or ends with text like ';'")
#                         item = self.uic.table_products.item(numRows, 0)
#                         item.setBackground(error_color)
#
#                 if sim1:
#                     self.uic.table_products.setItem(numRows, 1, QTableWidgetItem(sim1))
#                     if not sim1.startswith("3578"):
#                         self.add_error("SIM1-IMEI does not begin by '3578'")
#                         self.uic.table_products.item(numRows, 1).setBackground(ok_color)
#                     if len(sim1) != 14:
#                         self.add_error("SIM1-IMEI has not the correct length(Should be 14 chars, {} found)".format(len(sim1)))
#                         self.uic.table_products.item(numRows, 1).setBackground(ok_color)
#
#                 if sim2:
#                     self.uic.table_products.setItem(numRows, 2, QTableWidgetItem(sim2))
#                     if not sim2.startswith("3578"):
#                         self.add_error("SIM2-IMEI value does not begin by '3578'")
#                         self.uic.table_products.item(numRows, 2).setBackground(ok_color)
#                     if len(sim2) != 14:
#                         self.add_error("SIM2-IMEI has not the correct length(Should be 14 chars, {} found)".format(len(sim2)))
#                         self.uic.table_products.item(numRows, 2).setBackground(ok_color)
        except Exception as ex:
            self.add_error("Can't retrieve all PDT informations")
            self.add_error(str(ex))

        # Removes the last line and checks integrity
        print(self.product_type)
        if not lines[-1].startswith("ITF-14::") and self.product_type != PRODUCT:
            self.add_error("The QRCode does not end with a ITF-14 line")
            self.itf = "- - -"
            self.ids.txt_itf.background_color = [0, 1, 0, 1]
        else:
            itf_14 = lines[-1].replace("ITF-14::", "")
            self.itf = itf_14

            if ";" in value:
                self.ids.txt_itf.background_color = [0, 1, 0, 1]
                self.add_error("ITF-14 value ends with ';'")
            else:
                self.ids.txt_itf.background_color = [0, 1, 0, 1]


class QrCodeApp(App):

    def build(self):
        return QrCode()

    def on_pause(self):
        return True

if __name__ in ('__main__', '__android__'):
    QrCodeApp().run()
