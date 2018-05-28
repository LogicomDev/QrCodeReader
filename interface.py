# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\interface.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Interface(object):
    def setupUi(self, Interface):
        Interface.setObjectName("Interface")
        Interface.setWindowModality(QtCore.Qt.ApplicationModal)
        Interface.setEnabled(True)
        Interface.resize(500, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Interface.sizePolicy().hasHeightForWidth())
        Interface.setSizePolicy(sizePolicy)
        Interface.setMinimumSize(QtCore.QSize(500, 570))
        Interface.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Interface.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("qr-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Interface.setWindowIcon(icon)
        Interface.setAutoFillBackground(False)
        Interface.setStyleSheet("\n"
"QMainWindow\n"
"{\n"
"background-color: rgb(237,241,242);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"color: rgb(138, 138, 138);\n"
"}\n"
"\n"
"QLineEdit, QLineEdit:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QLineEdit:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QLineEdit:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"QSpinBox, QSpinBox:hover {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 1px solid #dddddd;\n"
"    background-color:rgba(0,0,0,0);\n"
"}\n"
"\n"
"QSpinBox:editable{\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #b2dfdb;\n"
"}\n"
"\n"
"QLineEdit:disabled{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #eeeeee;\n"
"}\n"
"\n"
"QSpinBox:focus{\n"
"    border: 0px solid white;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"    color: #111111;\n"
"}\n"
"QSpinBox:pressed {\n"
"    border: none;\n"
"    padding-bottom: 2px;\n"
"    border-bottom: 2px solid #00695c;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(230, 230, 230);;    \n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"  background-color: rgb(130, 186, 23);\n"
"    width: 20px;\n"
"}\n"
"\n"
"QPushButton, QPushButton:focus {\n"
"  border: none;\n"
"  color: black;\n"
"  padding: 3px 20px\n"
"}\n"
"\n"
"QPushButton:hover, QPushButton:hover:focus {\n"
"  background-color: rgb(130, 186, 23);\n"
"  border-color: #ffffff\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgb(131, 186, 23);\n"
"    border: none\n"
"}\n"
"\n"
"QTreeWidget{\n"
"    background-color: rgb(150,150, 150);\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTreeWidget:item:hover,QTreeWidget:item:focus {\n"
"    background-color: rgb(58, 176, 0);\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: white;\n"
"    selection-background-color: rgb(150,150, 150);\n"
"}\n"
"\n"
"QTableWidgetItem:hover{\n"
"    background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    background: red;\n"
"    position: absolute; /* absolutely position 4px from the left and right of the widget. setting margins on the widget should work too... */\n"
"    left: 4px; right: 4px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background: green;\n"
"    margin: 0 -4px; /* expand outside the groove */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: pink;\n"
"}\n"
"\n"
"QGroupBox{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(217, 217, 217);\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"")
        Interface.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        Interface.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(Interface)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_filepath = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_filepath.sizePolicy().hasHeightForWidth())
        self.btn_filepath.setSizePolicy(sizePolicy)
        self.btn_filepath.setMinimumSize(QtCore.QSize(100, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("download-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_filepath.setIcon(icon1)
        self.btn_filepath.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btn_filepath.setObjectName("btn_filepath")
        self.horizontalLayout.addWidget(self.btn_filepath)
        self.filepath = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filepath.setText("")
        self.filepath.setReadOnly(True)
        self.filepath.setObjectName("filepath")
        self.horizontalLayout.addWidget(self.filepath)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.cb_label_type = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.cb_label_type.setObjectName("cb_label_type")
        self.cb_label_type.addItem("")
        self.cb_label_type.addItem("")
        self.horizontalLayout_4.addWidget(self.cb_label_type)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.btn_check = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_check.setObjectName("btn_check")
        self.verticalLayout.addWidget(self.btn_check)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_statut = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_statut.sizePolicy().hasHeightForWidth())
        self.lbl_statut.setSizePolicy(sizePolicy)
        self.lbl_statut.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbl_statut.setObjectName("lbl_statut")
        self.horizontalLayout_2.addWidget(self.lbl_statut)
        self.validity_result = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.validity_result.setMinimumSize(QtCore.QSize(0, 40))
        self.validity_result.setReadOnly(True)
        self.validity_result.setObjectName("validity_result")
        self.horizontalLayout_2.addWidget(self.validity_result)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tab_results = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tab_results.setMaximumSize(QtCore.QSize(16777215, 210))
        self.tab_results.setObjectName("tab_results")
        self.ctn_tab = QtWidgets.QWidget()
        self.ctn_tab.setObjectName("ctn_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.ctn_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.batch_number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.batch_number.setReadOnly(True)
        self.batch_number.setObjectName("batch_number")
        self.gridLayout.addWidget(self.batch_number, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.color = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.color.setReadOnly(True)
        self.color.setObjectName("color")
        self.gridLayout.addWidget(self.color, 5, 2, 1, 1)
        self.qty_number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.qty_number.setReadOnly(True)
        self.qty_number.setObjectName("qty_number")
        self.gridLayout.addWidget(self.qty_number, 4, 2, 1, 1)
        self.ctn_number = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ctn_number.setReadOnly(True)
        self.ctn_number.setObjectName("ctn_number")
        self.gridLayout.addWidget(self.ctn_number, 2, 2, 1, 1)
        self.model_name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.model_name.setReadOnly(True)
        self.model_name.setObjectName("model_name")
        self.gridLayout.addWidget(self.model_name, 1, 2, 1, 1)
        self.supplier_id = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.supplier_id.setReadOnly(True)
        self.supplier_id.setObjectName("supplier_id")
        self.gridLayout.addWidget(self.supplier_id, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.ean_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.ean_13.setReadOnly(True)
        self.ean_13.setObjectName("ean_13")
        self.gridLayout.addWidget(self.ean_13, 6, 2, 1, 1)
        self.tab_results.addTab(self.ctn_tab, "")
        self.product_tab = QtWidgets.QWidget()
        self.product_tab.setObjectName("product_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.product_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 451, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table_products = QtWidgets.QTableWidget(self.gridLayoutWidget_2)
        self.table_products.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_products.setDragDropOverwriteMode(False)
        self.table_products.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_products.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_products.setObjectName("table_products")
        self.table_products.setColumnCount(3)
        self.table_products.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_products.setHorizontalHeaderItem(2, item)
        self.table_products.horizontalHeader().setDefaultSectionSize(143)
        self.table_products.horizontalHeader().setMinimumSectionSize(50)
        self.table_products.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.table_products, 0, 0, 1, 1)
        self.tab_results.addTab(self.product_tab, "")
        self.tab_error = QtWidgets.QWidget()
        self.tab_error.setObjectName("tab_error")
        self.table_error = QtWidgets.QTableWidget(self.tab_error)
        self.table_error.setGeometry(QtCore.QRect(0, 0, 471, 181))
        self.table_error.setObjectName("table_error")
        self.table_error.setColumnCount(1)
        self.table_error.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_error.setHorizontalHeaderItem(0, item)
        self.table_error.horizontalHeader().setVisible(False)
        self.table_error.horizontalHeader().setStretchLastSection(True)
        self.table_error.verticalHeader().setVisible(False)
        self.tab_results.addTab(self.tab_error, "")
        self.verticalLayout.addWidget(self.tab_results)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setMinimumSize(QtCore.QSize(90, 0))
        self.label_8.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.itf_14 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.itf_14.setReadOnly(True)
        self.itf_14.setObjectName("itf_14")
        self.horizontalLayout_3.addWidget(self.itf_14)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.raw_text = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.raw_text.setMaximumSize(QtCore.QSize(16777215, 150))
        self.raw_text.setObjectName("raw_text")
        self.verticalLayout.addWidget(self.raw_text)
        Interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(Interface)
        self.tab_results.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Interface)

    def retranslateUi(self, Interface):
        _translate = QtCore.QCoreApplication.translate
        Interface.setWindowTitle(_translate("Interface", "Logicom QRCode Checker"))
        self.btn_filepath.setText(_translate("Interface", "Select a picture"))
        self.filepath.setPlaceholderText(_translate("Interface", "<- Select a picture to upload and check"))
        self.label_9.setText(_translate("Interface", "Label type :"))
        self.cb_label_type.setItemText(0, _translate("Interface", "CARTON"))
        self.cb_label_type.setItemText(1, _translate("Interface", "PRODUCT"))
        self.btn_check.setText(_translate("Interface", "Check QRCode"))
        self.lbl_statut.setText(_translate("Interface", "QRCode validity :"))
        self.label_5.setText(_translate("Interface", "Quantity :"))
        self.label_2.setText(_translate("Interface", "Model Name :"))
        self.label.setText(_translate("Interface", "Supplier ID :"))
        self.label_4.setText(_translate("Interface", "Batch Number :"))
        self.label_3.setText(_translate("Interface", "CTN Number :"))
        self.label_6.setText(_translate("Interface", "Color :"))
        self.label_7.setText(_translate("Interface", "EAN 13 :"))
        self.tab_results.setTabText(self.tab_results.indexOf(self.ctn_tab), _translate("Interface", "Carton Data"))
        item = self.table_products.horizontalHeaderItem(0)
        item.setText(_translate("Interface", "S/N"))
        item = self.table_products.horizontalHeaderItem(1)
        item.setText(_translate("Interface", "SIM 1"))
        item = self.table_products.horizontalHeaderItem(2)
        item.setText(_translate("Interface", "SIM 2"))
        self.tab_results.setTabText(self.tab_results.indexOf(self.product_tab), _translate("Interface", "Product Data"))
        item = self.table_error.horizontalHeaderItem(0)
        item.setText(_translate("Interface", "Error"))
        self.tab_results.setTabText(self.tab_results.indexOf(self.tab_error), _translate("Interface", "Errors"))
        self.label_8.setText(_translate("Interface", "ITF-14 :"))
        self.label_10.setText(_translate("Interface", "QR Code Raw data :"))

