import sys

import psycopg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor, QPixmap
from PyQt5.QtWidgets import QComboBox, QTableWidgetItem, QListWidgetItem, QDialog, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QApplication, QWidget, QMessageBox, QMenuBar, QAction, QMainWindow

from TableBuilder import TableBuilder
from UiComponents import InputDialog
from database import DatabaseConnection
from config import *
from themes import *


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection(**DB_CONFIG)
        self.connection = self.db.connection
        self.initialize_db()

    def open_dialog(self):
        dialog = InputDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            value = dialog.get_input_text()
            print(f"Entered value: {value}")
            return value

    def initialize_db(self):
        table_builder = TableBuilder(self.db)
        table_builder.create_tables()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200,800)

        self.menu_bar = self.menuBar()
        self.theme_menu = self.menu_bar.addMenu("Themes")

        # Добавляем действия для тем
        self.dark_theme_action = QAction("Dark Theme", self)
        self.dark_theme_action.triggered.connect(lambda: apply_theme(app, "dark"))
        self.theme_menu.addAction(self.dark_theme_action)

        self.windows_xp_theme_action = QAction("Windows XP Theme", self)
        self.windows_xp_theme_action.triggered.connect(lambda: apply_theme(app, "windows_xp"))
        self.theme_menu.addAction(self.windows_xp_theme_action)

        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.create_conf = QWidget()
        self.create_conf.setObjectName("create_conf")

        self.progressBar = QtWidgets.QProgressBar(self.create_conf)
        self.progressBar.setGeometry(QtCore.QRect(847, 30, 261, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.progressBar_2 = QtWidgets.QProgressBar(self.create_conf)
        self.progressBar_2.setGeometry(QtCore.QRect(847, 70, 261, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")

        self.label_required = QLabel("Обязательные компоненты", self.create_conf)
        self.label_required.move(577, 30)

        self.label_optional = QLabel("Необязательные компоненты", self.create_conf)
        self.label_optional.move(557, 70)

        self.layoutWidget = QtWidgets.QWidget(self.create_conf)
        self.layoutWidget.setGeometry(QtCore.QRect(15, 109, 431, 591))
        self.layoutWidget.setObjectName("layoutWidget")

        self.tabWidget.addTab(self.create_conf, "Create Configuration")
        self.horizontalLayout_10.addWidget(self.tabWidget)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_mother_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_mother_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mother_2.setObjectName("label_mother_2")
        self.horizontalLayout_11.addWidget(self.label_mother_2)
        self.comboBox_9 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_9.setObjectName("comboBox_9")
        self.horizontalLayout_11.addWidget(self.comboBox_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_power_supply_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_power_supply_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_power_supply_2.setObjectName("label_power_supply_2")
        self.horizontalLayout_12.addWidget(self.label_power_supply_2)
        self.comboBox_10 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_10.setObjectName("comboBox_10")
        self.horizontalLayout_12.addWidget(self.comboBox_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_cpu_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_cpu_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cpu_2.setObjectName("label_cpu_2")
        self.horizontalLayout_13.addWidget(self.label_cpu_2)
        self.comboBox_11 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_11.setObjectName("comboBox_11")
        self.horizontalLayout_13.addWidget(self.comboBox_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_gpu_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_gpu_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_gpu_2.setObjectName("label_gpu_2")
        self.horizontalLayout_14.addWidget(self.label_gpu_2)
        self.comboBox_12 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_12.setObjectName("comboBox_12")
        self.horizontalLayout_14.addWidget(self.comboBox_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_cooler_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_cooler_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cooler_2.setObjectName("label_cooler_2")
        self.horizontalLayout_15.addWidget(self.label_cooler_2)
        self.comboBox_13 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_13.setObjectName("comboBox_13")
        self.horizontalLayout_15.addWidget(self.comboBox_13)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_ram_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_ram_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ram_2.setObjectName("label_ram_2")
        self.horizontalLayout_16.addWidget(self.label_ram_2)
        self.comboBox_14 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_14.setObjectName("comboBox_14")
        self.horizontalLayout_16.addWidget(self.comboBox_14)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_HDD_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_HDD_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_HDD_2.setObjectName("label_HDD_2")
        self.horizontalLayout_17.addWidget(self.label_HDD_2)
        self.comboBox_15 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_15.setObjectName("comboBox_15")
        self.horizontalLayout_17.addWidget(self.comboBox_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_frame_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_frame_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_frame_2.setObjectName("label_frame_2")
        self.horizontalLayout_18.addWidget(self.label_frame_2)
        self.comboBox_16 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_16.setObjectName("comboBox_16")
        self.horizontalLayout_18.addWidget(self.comboBox_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.pushButton_save = QtWidgets.QPushButton(self.create_conf)
        self.pushButton_save.setGeometry(QtCore.QRect(460, 620, 301, 81))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_characteristics = QtWidgets.QLabel(self.create_conf)
        self.label_characteristics.setGeometry(QtCore.QRect(20, 20, 530, 71))
        self.label_characteristics.setObjectName("label_characteristics")
        self.label_characteristics.setWordWrap(True)
        self.tabWidget.addTab(self.create_conf, "")
        self.tab_add_components = QtWidgets.QWidget()
        self.tab_add_components.setObjectName("tab_add_components")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_add_components)
        self.layoutWidget1.setGeometry(QtCore.QRect(250, 670, 321, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Button_add = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_add.setObjectName("Button_add")
        self.horizontalLayout.addWidget(self.Button_add)
        self.Button_update = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_update.setObjectName("Button_update")
        self.horizontalLayout.addWidget(self.Button_update)
        self.Button_delete = QtWidgets.QPushButton(self.layoutWidget1)
        self.Button_delete.setObjectName("Button_delete")
        self.horizontalLayout.addWidget(self.Button_delete)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_add_components)
        self.layoutWidget2.setGeometry(QtCore.QRect(580, 0, 77, 691))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 40, 0, 40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_addmother = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addmother.setObjectName("pushButton_addmother")
        self.verticalLayout.addWidget(self.pushButton_addmother)
        self.pushButton_addsupply = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addsupply.setObjectName("pushButton_addsupply")
        self.verticalLayout.addWidget(self.pushButton_addsupply)
        self.pushButton_addcpu = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addcpu.setObjectName("pushButton_addcpu")
        self.verticalLayout.addWidget(self.pushButton_addcpu)
        self.pushButton_addgpu = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addgpu.setObjectName("pushButton_addgpu")
        self.verticalLayout.addWidget(self.pushButton_addgpu)
        self.pushButton_addcooler = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addcooler.setObjectName("pushButton_addcooler")
        self.verticalLayout.addWidget(self.pushButton_addcooler)
        self.pushButton_addram = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addram.setObjectName("pushButton_addram")
        self.verticalLayout.addWidget(self.pushButton_addram)
        self.pushButton_addHDD = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addHDD.setObjectName("pushButton_addHDD")
        self.verticalLayout.addWidget(self.pushButton_addHDD)
        self.pushButton_addframe = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_addframe.setObjectName("pushButton_addframe")
        self.verticalLayout.addWidget(self.pushButton_addframe)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_add_components)
        self.tableWidget_2.setGeometry(QtCore.QRect(710, 80, 431, 561))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab_add_components)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 30, 551, 631))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_mother = QtWidgets.QLabel(self.layoutWidget3)
        self.label_mother.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_mother.setObjectName("label_mother")
        self.horizontalLayout_2.addWidget(self.label_mother)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_power_supply = QtWidgets.QLabel(self.layoutWidget3)
        self.label_power_supply.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_power_supply.setObjectName("label_power_supply")
        self.horizontalLayout_3.addWidget(self.label_power_supply)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_cpu = QtWidgets.QLabel(self.layoutWidget3)
        self.label_cpu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cpu.setObjectName("label_cpu")
        self.horizontalLayout_4.addWidget(self.label_cpu)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_gpu = QtWidgets.QLabel(self.layoutWidget3)
        self.label_gpu.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_gpu.setObjectName("label_gpu")
        self.horizontalLayout_5.addWidget(self.label_gpu)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_5.addWidget(self.comboBox_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_cooler = QtWidgets.QLabel(self.layoutWidget3)
        self.label_cooler.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_cooler.setObjectName("label_cooler")
        self.horizontalLayout_6.addWidget(self.label_cooler)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_6.addWidget(self.comboBox_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_ram = QtWidgets.QLabel(self.layoutWidget3)
        self.label_ram.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_ram.setObjectName("label_ram")
        self.horizontalLayout_7.addWidget(self.label_ram)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_7.addWidget(self.comboBox_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_HDD = QtWidgets.QLabel(self.layoutWidget3)
        self.label_HDD.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_HDD.setObjectName("label_HDD")
        self.horizontalLayout_8.addWidget(self.label_HDD)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_7.setObjectName("comboBox_7")
        self.horizontalLayout_8.addWidget(self.comboBox_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_frame = QtWidgets.QLabel(self.layoutWidget3)
        self.label_frame.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_frame.setObjectName("label_frame")
        self.horizontalLayout_9.addWidget(self.label_frame)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox_8.setObjectName("comboBox_8")
        self.horizontalLayout_9.addWidget(self.comboBox_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.tabWidget.addTab(self.tab_add_components, "")
        self.tab_ready_conf = QtWidgets.QWidget()
        self.tab_ready_conf.setObjectName("tab_ready_conf")
        self.listWidget = QtWidgets.QListWidget(self.tab_ready_conf)
        self.listWidget.setGeometry(QtCore.QRect(10, 0, 411, 721))
        self.listWidget.setObjectName("listWidget")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_ready_conf)
        self.tableWidget.setGeometry(QtCore.QRect(430, 0, 721, 611))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_change = QtWidgets.QPushButton(self.tab_ready_conf)
        self.pushButton_change.setGeometry(QtCore.QRect(808, 630, 161, 101))
        self.pushButton_change.setObjectName("pushButton_change")
        self.pushButton_delete = QtWidgets.QPushButton(self.tab_ready_conf)
        self.pushButton_delete.setGeometry(QtCore.QRect(971, 630, 161, 101))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.tabWidget.addTab(self.tab_ready_conf, "")
        self.horizontalLayout_10.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.load_all_configurations() # загрузка предыдущих конфигураций

        self.last_clicked_button = None
        self.last_changed_combobox = None
        self.current_table_name = None
        self.current_combobox_value = None

        self.pushButton_addmother.clicked.connect(self.addMother)
        self.pushButton_addsupply.clicked.connect(self.addSupply)
        self.pushButton_addgpu.clicked.connect(self.addGPU)
        self.pushButton_addram.clicked.connect(self.addRAM)
        self.pushButton_addcpu.clicked.connect(self.addCPU)
        self.pushButton_addcooler.clicked.connect(self.addCooler)
        self.pushButton_addframe.clicked.connect(self.addFrame)
        self.pushButton_addHDD.clicked.connect(self.addHDD)

        self.listWidget.itemClicked.connect(self.show_selected_configuration) # проверка на выбранную конфигурацию

        self.Button_add.clicked.connect(self.Button_add_clicked)
        self.pushButton_save.clicked.connect(self.save_current_configuration)
        self.pushButton_change.clicked.connect(self.change_configuration)
        self.pushButton_delete.clicked.connect(self.delete_configuration) # готовые конфигурации

        self.configurations = []  # Конфигурации

        self.unique_configurations = set() # Конфигурации для отображения


        self.comboBox.currentIndexChanged.connect(lambda:self.update_tableWidget2("motherboard", "comboBox"))
        self.comboBox_2.currentIndexChanged.connect(lambda:self.update_tableWidget2("supply", "comboBox_2"))
        self.comboBox_3.currentIndexChanged.connect(lambda:self.update_tableWidget2("cpu", "comboBox_3"))
        self.comboBox_4.currentIndexChanged.connect(lambda: self.update_tableWidget2("gpu", "comboBox_4"))
        self.comboBox_5.currentIndexChanged.connect(lambda: self.update_tableWidget2("cooler", "comboBox_5"))
        self.comboBox_6.currentIndexChanged.connect(lambda: self.update_tableWidget2("ram", "comboBox_6"))
        self.comboBox_7.currentIndexChanged.connect(lambda: self.update_tableWidget2("hdd", "comboBox_7"))
        self.comboBox_8.currentIndexChanged.connect(lambda: self.update_tableWidget2("frame", "comboBox_8"))

        self.comboBox_9.currentIndexChanged.connect(lambda:self.update_label_characteristics("motherboard", "comboBox_9"))
        self.comboBox_10.currentIndexChanged.connect(lambda:self.update_label_characteristics("supply", "comboBox_10"))
        self.comboBox_11.currentIndexChanged.connect(lambda:self.update_label_characteristics("cpu", "comboBox_11"))
        self.comboBox_12.currentIndexChanged.connect(lambda: self.update_label_characteristics("gpu", "comboBox_12"))
        self.comboBox_13.currentIndexChanged.connect(lambda: self.update_label_characteristics("cooler", "comboBox_13"))
        self.comboBox_14.currentIndexChanged.connect(lambda: self.update_label_characteristics("ram", "comboBox_14"))
        self.comboBox_15.currentIndexChanged.connect(lambda: self.update_label_characteristics("hdd", "comboBox_15"))
        self.comboBox_16.currentIndexChanged.connect(lambda: self.update_label_characteristics("frame", "comboBox_16"))

        self.populate_combobox(self.comboBox, "motherboard")
        self.populate_combobox(self.comboBox_2, "supply")
        self.populate_combobox(self.comboBox_3, "cpu")
        self.populate_combobox(self.comboBox_4, "gpu")
        self.populate_combobox(self.comboBox_5, "cooler")
        self.populate_combobox(self.comboBox_6, "ram")
        self.populate_combobox(self.comboBox_7, "hdd")
        self.populate_combobox(self.comboBox_8, "frame")
        self.populate_combobox(self.comboBox_9, "motherboard")
        self.populate_combobox(self.comboBox_10, "supply")
        self.populate_combobox(self.comboBox_11, "cpu")
        self.populate_combobox(self.comboBox_12, "gpu")
        self.populate_combobox(self.comboBox_13, "cooler")
        self.populate_combobox(self.comboBox_14, "ram")
        self.populate_combobox(self.comboBox_15, "hdd")
        self.populate_combobox(self.comboBox_16, "frame")

        self.comboBox_9.setCurrentIndex(-1)
        self.comboBox_10.setCurrentIndex(-1)
        self.comboBox_11.setCurrentIndex(-1)
        self.comboBox_12.setCurrentIndex(-1)
        self.comboBox_13.setCurrentIndex(-1)
        self.comboBox_14.setCurrentIndex(-1)
        self.comboBox_15.setCurrentIndex(-1)
        self.comboBox_16.setCurrentIndex(-1)

        self.frame_label = QLabel(self.create_conf)
        self.motherboard_label = QLabel(self.create_conf)
        self.supply_label = QLabel(self.create_conf)
        self.gpu_label = QLabel(self.create_conf)
        self.hdd_label = QLabel(self.create_conf)
        self.cpu_label = QLabel(self.create_conf)
        self.cooler_label = QLabel(self.create_conf)
        self.ram_label = QLabel(self.create_conf)

        self.supply_label.setPixmap(QPixmap("sprites/Блок_питания.png"))
        self.gpu_label.setPixmap(QPixmap("sprites/Видео_карта.png"))
        self.hdd_label.setPixmap(QPixmap("sprites/Жесткий диск.png"))
        self.frame_label.setPixmap(QPixmap("sprites/Корпус.png"))
        self.cooler_label.setPixmap(QPixmap("sprites/Кулер.png"))
        self.motherboard_label.setPixmap(QPixmap("sprites/материнка.png"))
        self.ram_label.setPixmap(QPixmap("sprites/Оператива.png"))
        self.cpu_label.setPixmap(QPixmap("sprites/Проц.png"))

        for label in [self.supply_label, self.gpu_label, self.hdd_label, self.frame_label, self.cooler_label,
                      self.motherboard_label, self.ram_label, self.cpu_label]:
            label.setGeometry(600, 100, 554, 522)
            label.setVisible(False)

        self.comboBox_9.currentIndexChanged.connect(self.update_visibility_1)
        self.comboBox_10.currentIndexChanged.connect(self.update_visibility_2)
        self.comboBox_11.currentIndexChanged.connect(self.update_visibility_3)
        self.comboBox_12.currentIndexChanged.connect(self.update_visibility_4)
        self.comboBox_13.currentIndexChanged.connect(self.update_visibility_5)
        self.comboBox_14.currentIndexChanged.connect(self.update_visibility_6)
        self.comboBox_15.currentIndexChanged.connect(self.update_visibility_7)
        self.comboBox_16.currentIndexChanged.connect(self.update_visibility_8)

        # обязательний прогресбар
        self.comboBox_9.currentIndexChanged.connect(self.update_progress_bar)
        self.comboBox_10.currentIndexChanged.connect(self.update_progress_bar)
        self.comboBox_11.currentIndexChanged.connect(self.update_progress_bar)
        self.comboBox_13.currentIndexChanged.connect(self.update_progress_bar)
        self.comboBox_14.currentIndexChanged.connect(self.update_progress_bar)
        self.comboBox_15.currentIndexChanged.connect(self.update_progress_bar)

        self.comboBox_12.currentIndexChanged.connect(self.update_progress_bar_2)
        self.comboBox_16.currentIndexChanged.connect(self.update_progress_bar_2)

        self.Button_update.clicked.connect(self.update_database)

        #competible
        self.comboBox_9.currentIndexChanged.connect(self.check_compatibility)
        self.comboBox_11.currentIndexChanged.connect(self.check_compatibility)
        self.comboBox_14.currentIndexChanged.connect(self.check_compatibility)
        self.comboBox_10.currentIndexChanged.connect(self.check_compatibility)
        self.comboBox_12.currentIndexChanged.connect(self.check_compatibility)
        self.comboBox_13.currentIndexChanged.connect(self.check_compatibility)

    def check_compatibility(self):
        with self.connection.cursor() as cursor:
            selected_motherboard = self.comboBox_9.currentText()
            selected_supply = self.comboBox_10.currentText()
            selected_cpu = self.comboBox_11.currentText()
            selected_gpu = self.comboBox_12.currentText()
            selected_ram = self.comboBox_14.currentText()
            selected_cooler = self.comboBox_13.currentText()

            power_supply = 0

            if len(selected_motherboard)>0:
                # Сокет материнской платы
                cursor.execute("SELECT soket FROM motherboard WHERE name = %s", (selected_motherboard,))
                motherboard_socket = cursor.fetchone()[0]

                # Тип памяти материнской платы
                cursor.execute("SELECT type_member FROM motherboard WHERE name = %s", (selected_motherboard,))
                motherboard_memory_type = cursor.fetchone()[0]

            if len(selected_cpu)>0:
                # Сокет процессора
                cursor.execute("SELECT soket FROM cpu WHERE name = %s", (selected_cpu,))
                cpu_socket = cursor.fetchone()[0]
            if len(selected_ram)>0:
                # Тип памяти оперативной памяти
                cursor.execute("SELECT type_member FROM ram WHERE name = %s", (selected_ram,))
                ram_memory_type = cursor.fetchone()[0]
            if len(selected_supply)>0:
                # Мощность блока питания
                cursor.execute("SELECT power FROM supply WHERE name = %s", (selected_supply,))
                power_supply = int(cursor.fetchone()[0])  # Предполагается, что значения числовые

            if len(selected_cpu)>0:
                # Получите значение power_use для cpu
                cursor.execute("SELECT power_use FROM cpu WHERE name = %s", (selected_cpu,))
                cpu_power_use = int(cursor.fetchone()[0])
            if len(selected_gpu)>0:
                cursor.execute("SELECT power_use FROM gpu WHERE name = %s", (selected_gpu,))
                gpu_power_use = cursor.fetchone()
            if len(selected_ram)>0:
                # Аналогично для RAM
                cursor.execute("SELECT power_use FROM ram WHERE name = %s", (selected_ram,))
                ram_power_use = cursor.fetchone()
            if len(selected_cooler)>0:
                cursor.execute("SELECT power_use FROM cooler WHERE name = %s", (selected_cooler,))
                cooler_power_use = int(cursor.fetchone()[0])

        # Проверки на совместимость

        if len(self.comboBox_9.currentText()) > 0 and len(self.comboBox_11.currentText()) > 0:
                # Проверка совместимости сокетов
            compatible_socket = motherboard_socket == cpu_socket
            if not compatible_socket:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Сокет несовместим!")
                msg.setInformativeText("Выберите совместимый сокет для материнской платы и процессора.")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        if len(self.comboBox_9.currentText()) > 0 and len(self.comboBox_14.currentText()) > 0:
            compatible_memory = motherboard_memory_type == ram_memory_type
            if not compatible_memory:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Тип памяти несовместим!")
                msg.setInformativeText("Выберите совместимый тип памяти для материнской платы и оперативной памяти.")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
        if (len(self.comboBox_10.currentText()) > 0
                and len(self.comboBox_11.currentText()) > 0
                and len(self.comboBox_12.currentText()) > 0
                and len(self.comboBox_14.currentText())
                and len(self.comboBox_13.currentText())):
            try:
                compatible_power = power_supply <= cpu_power_use + gpu_power_use + ram_power_use + cooler_power_use
                if not compatible_power:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Слабый блок питания!")
                    msg.setInformativeText("Выберите более мощный блок питания.")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
            except Exception as e:
                print(f"An error occurred: {e}")
                compatible_power = False  # Помечаем, что совместимость по мощности

    def update_database(self):
        try:
            if self.current_table_name and self.current_combobox_value:
                with self.connection.cursor() as cursor:
                    if self.current_table_name == "motherboard":
                        # Для таблицы motherboard
                        update_query = """
                                        UPDATE motherboard
                                        SET name = %s, price = %s, form = %s, soket = %s, type_member = %s, interface = %s
                                        WHERE name = %s
                                        """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        form = self.tableWidget_2.item(2, 1).text()
                        soket = self.tableWidget_2.item(3, 1).text()
                        type_member = self.tableWidget_2.item(4, 1).text()
                        interface = self.tableWidget_2.item(5, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query,
                                       (name, price, form, soket, type_member, interface, self.current_combobox_value))
                    elif self.current_table_name == "supply":
                        update_query = """
                                                UPDATE supply
                                                SET name = %s, price = %s, power = %s, type = %s
                                                WHERE name = %s
                                                """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        power = self.tableWidget_2.item(2, 1).text()
                        type_value = self.tableWidget_2.item(3, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, power, type_value, self.current_combobox_value))
                    elif self.current_table_name == "ram":
                        update_query = """
                                                UPDATE ram
                                                SET name = %s, price = %s, frequency = %s, type_member = %s, power_use = %s
                                                WHERE name = %s
                                                """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        frequency = self.tableWidget_2.item(2, 1).text()
                        type_member = self.tableWidget_2.item(3, 1).text()
                        power_use = self.tableWidget_2.item(4, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, frequency, type_member, power_use, self.current_combobox_value))


                    elif self.current_table_name == "hdd":
                        update_query = """
                                        UPDATE hdd
                                        SET name = %s, price = %s, capacity = %s, recording = %s, reading = %s
                                        WHERE name = %s
                                        """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        capacity = self.tableWidget_2.item(2, 1).text()
                        recording = self.tableWidget_2.item(3, 1).text()
                        reading = self.tableWidget_2.item(4, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, capacity, recording, reading, self.current_combobox_value))

                    elif self.current_table_name == "gpu":
                        update_query = """
                                        UPDATE gpu
                                        SET name = %s, price = %s, frequency = %s, soket = %s, power_use = %s
                                        WHERE name = %s
                                        """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        frequency = self.tableWidget_2.item(2, 1).text()
                        soket = self.tableWidget_2.item(3, 1).text()
                        power_use = self.tableWidget_2.item(4, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, frequency, soket, power_use, self.current_combobox_value))

                    elif self.current_table_name == "frame":
                        update_query = """
                                        UPDATE frame
                                        SET name = %s, price = %s, form = %s
                                        WHERE name = %s
                                        """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        form = self.tableWidget_2.item(2, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, form))

                    elif self.current_table_name == "cpu":
                        update_query = """
                                       UPDATE cpu
                                       SET name = %s, price = %s, soket = %s, frequency = %s, power_use = %s
                                       WHERE name = %s
                                       """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        soket = self.tableWidget_2.item(2, 1).text()
                        frequency = self.tableWidget_2.item(3, 1).text()
                        power_use = self.tableWidget_2.item(4, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, soket, frequency, power_use, self.current_combobox_value))

                    elif self.current_table_name == "cooler":
                        update_query = """
                                        UPDATE cooler
                                        SET name = %s, price = %s, speed = %s, power_use = %s
                                        WHERE name = %s
                                        """
                        # Получаем значения из второго столбца tableWidget_2
                        name = self.tableWidget_2.item(0, 1).text()
                        price = self.tableWidget_2.item(1, 1).text()
                        speed = self.tableWidget_2.item(2, 1).text()
                        power_use = self.tableWidget_2.item(3, 1).text()

                        # Выполняем запрос
                        cursor.execute(update_query, (name, price, speed, power_use, self.current_combobox_value))

                self.connection.commit()
        except Exception as e:
                print(f"Произошло исключение: {e}")


    def update_progress_bar(self):
        non_empty_count = sum(1 for combo in
                              [self.comboBox_9, self.comboBox_10, self.comboBox_11, self.comboBox_13, self.comboBox_14,
                               self.comboBox_15] if combo.currentIndex() != -1)

        # Устанавливаем значение ProgressBar в процентном соотношении
        total_comboboxes = len([self.comboBox_9, self.comboBox_10, self.comboBox_11, self.comboBox_13, self.comboBox_14,
                                self.comboBox_15])  # Общее количество ComboBox
        progress_value = int(
            (non_empty_count / total_comboboxes) * 100) if total_comboboxes > 0 else 0  # Преобразуем в int
        self.progressBar.setValue(progress_value)

    def update_progress_bar_2(self):
        non_empty_count = sum(1 for combo in
                              [self.comboBox_12, self.comboBox_16] if combo.currentIndex() != -1)

        # Устанавливаем значение ProgressBar в процентном соотношении
        total_comboboxes = len([self.comboBox_12, self.comboBox_16])  # Общее количество ComboBox
        progress_value = int(
            (non_empty_count / total_comboboxes) * 100) if total_comboboxes > 0 else 0  # Преобразуем в int
        self.progressBar_2.setValue(progress_value)

    def update_visibility_1(self):
        self.motherboard_label.setVisible(self.comboBox_9.currentIndex() > -1)
    def update_visibility_2(self):
        self.supply_label.setVisible(self.comboBox_10.currentIndex() > -1)
    def update_visibility_3(self):
        self.cpu_label.setVisible(self.comboBox_11.currentIndex() > -1)
    def update_visibility_4(self):
        self.gpu_label.setVisible(self.comboBox_12.currentIndex() > -1)
    def update_visibility_5(self):
        self.cooler_label.setVisible(self.comboBox_13.currentIndex() > -1)
    def update_visibility_6(self):
        self.ram_label.setVisible(self.comboBox_14.currentIndex() > -1)
    def update_visibility_7(self):
        self.hdd_label.setVisible(self.comboBox_15.currentIndex() > -1)
    def update_visibility_8(self):
        self.frame_label.setVisible(self.comboBox_16.currentIndex() > -1)


    def addMother(self):

        self.last_clicked_button = "motherboard"

        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(6)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Форм-фактор:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Сокет:"))
        self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Тип памяти:"))
        self.tableWidget_2.setItem(5, 0, QtWidgets.QTableWidgetItem("Интерфейсы:"))

    def addSupply(self):

        self.last_clicked_button = "supply"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(4)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Мощность:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Тип:"))

    def addGPU(self):

        self.last_clicked_button = "gpu"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(5)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Частота:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Сокет:"))
        self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Энергопотребление:"))

    def addRAM(self):

        self.last_clicked_button = "ram"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(5)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Частота:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Тип памяти:"))
        self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Энергопотребление:"))

    def addCPU(self):

        self.last_clicked_button = "cpu"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(5)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Сокет:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Частота:"))
        self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Энергопотребление:"))

    def addCooler(self):

        self.last_clicked_button = "cooler"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(4)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Количество_оборотов:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Энергопотребление:"))

    def addFrame(self):

        self.last_clicked_button = "frame"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(3)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Форм-фактор:"))

    def addHDD(self):

        self.last_clicked_button = "hdd"
        # Очищаем таблицу
        self.tableWidget_2.clear()

        # Добавляем строки и столбцы
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(5)

        # Заполняем ячейки
        self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
        self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
        self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Вместимость:"))
        self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Скорость записи:"))
        self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Скорость чтения:"))

    def Button_add_clicked(self):

        selected_component = self.last_clicked_button
        print(selected_component)

        with self.connection.cursor() as cursor:

            if selected_component == "motherboard":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    form = self.tableWidget_2.item(2, 1).text()
                    soket = self.tableWidget_2.item(3, 1).text()
                    type_member = self.tableWidget_2.item(4, 1).text()
                    interface = self.tableWidget_2.item(5, 1).text()

                    if not all([name, form, soket, type_member, interface]):
                        raise ValueError("Не все поля заполнены")

                    query = ("INSERT INTO motherboard (name, price, form, soket, type_member, interface)"
                             " VALUES (%s, %s, %s, %s, %s, %s)")
                    values = (name, price, form, soket, type_member, interface)

                    with self.connection.cursor() as cursor:
                        cursor.execute(query, values)
                        self.connection.commit()

                    self.comboBox_9.addItem(name)
                    self.comboBox.addItem(name)

                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)


            elif selected_component == "supply":
                try:

                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    power = self.tableWidget_2.item(2, 1).text()
                    type = self.tableWidget_2.item(3, 1).text()

                    if not all([name, power, type]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO supply (name, price, power, type) VALUES (%s, %s, %s, %s)"
                    value = (name, price, power, type)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_10.addItem(name)
                    self.comboBox_2.addItem(name)
                    self.comboBox_10.setCurrentIndex(-1)
                except Exception as e:
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)

            elif selected_component == "gpu":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    frequency = self.tableWidget_2.item(2, 1).text()
                    soket = self.tableWidget_2.item(3, 1).text()
                    power_use = self.tableWidget_2.item(4, 1).text()

                    if not all([name, frequency, soket, power_use]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO gpu (name, price, frequency, soket, power_use) VALUES (%s, %s, %s, %s, %s)"
                    value = (name, price, frequency, soket, power_use)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_12.addItem(name)
                    self.comboBox_4.addItem(name)
                    self.comboBox_12.setCurrentIndex(-1)
                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)


            elif selected_component == "ram":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    frequency = self.tableWidget_2.item(2, 1).text()
                    type_member = self.tableWidget_2.item(3, 1).text()
                    power_use = self.tableWidget_2.item(4, 1).text()

                    if not all([name, frequency, type_member, power_use]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO ram (name, price, frequency, type_member, power_use) VALUES (%s, %s, %s, %s, %s)"
                    value = (name, price, frequency, type_member, power_use)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_14.addItem(name)
                    self.comboBox_6.addItem(name)
                    self.comboBox_14.setCurrentIndex(-1)
                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)


            elif selected_component == "cpu":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    soket = self.tableWidget_2.item(2, 1).text()
                    frequency = self.tableWidget_2.item(3, 1).text()
                    power_use = self.tableWidget_2.item(4, 1).text()

                    if not all([name, soket, frequency, power_use]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO cpu (name, price, soket, frequency, power_use) VALUES (%s, %s, %s, %s, %s)"
                    value = (name, price, soket, frequency, power_use)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_11.addItem(name)
                    self.comboBox_3.addItem(name)
                    self.comboBox_11.setCurrentIndex(-1)
                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)

            elif selected_component == "cooler":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    speed = self.tableWidget_2.item(2, 1).text()
                    power_use = self.tableWidget_2.item(3, 1).text()

                    if not all([name, speed, power_use]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO cooler (name, price, speed, power_use) VALUES (%s, %s, %s, %s)"
                    value = (name, price, speed, power_use)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_13.addItem(name)
                    self.comboBox_5.addItem(name)
                    self.comboBox_13.setCurrentIndex(-1)
                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)


            elif selected_component == "frame":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    form = self.tableWidget_2.item(2, 1).text()

                    if not all([name, form]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO frame (name, price, form) VALUES (%s, %s, %s)"
                    value = (name, price, form)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_16.addItem(name)
                    self.comboBox_8.addItem(name)
                    self.comboBox_16.setCurrentIndex(-1)
                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)


            elif selected_component == "hdd":
                try:
                    name = self.tableWidget_2.item(0, 1).text()
                    price = self.tableWidget_2.item(1, 1).text()
                    capacity = self.tableWidget_2.item(2, 1).text()
                    recording = self.tableWidget_2.item(3, 1).text()
                    reading = self.tableWidget_2.item(4, 1).text()

                    if not all([name, capacity,recording,reading]):
                        raise ValueError("Не все поля заполнены")

                    query = "INSERT INTO hdd (name, price, capacity, recording, reading) VALUES (%s, %s, %s, %s, %s)"
                    value = (name, price, capacity, recording, reading)
                    cursor.execute(query, value)
                    self.connection.commit()

                    self.comboBox_15.addItem(name)
                    self.comboBox_7.addItem(name)
                    self.comboBox_15.setCurrentIndex(-1)
                except Exception as e:
                    # Выводим окно ошибки
                    error_message = f"Ошибка при добавлении материнской платы: {str(e)}"
                    QMessageBox.critical(self, "Ошибка", error_message)


            for row in range(self.tableWidget_2.rowCount()):
                item = QtWidgets.QTableWidgetItem("")
                self.tableWidget_2.setItem(row, 1, item)

    def populate_combobox(self, combobox, table_name):
        # Запрос к базе данных для получения данных
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT name FROM {table_name}")
        result = cursor.fetchall()
        combobox.addItems([item[0] for item in result])

    def search_component_by_name(self, table_name, component_name):
        # Используем существующее соединение с базой данных

        with self.connection.cursor() as cursor:
            # Запрос к базе данных для получения всей строки выбранной записи
            cursor.execute(f"SELECT * FROM {table_name} WHERE name = %s", (component_name,))
            result = cursor.fetchone()

            if result:
                if table_name == "motherboard":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, форма:{result[3]},"
                                       f" сокет:{result[4]}, тип памяти:{result[5]}, интерфейсы:{result[6]}")
                    print(result)
                    self.label_characteristics.setText(characteristics)
                elif table_name == "supply":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, мощность:{result[3]},"
                                       f" тип:{result[4]}")
                    self.label_characteristics.setText(characteristics)
                elif table_name == "ram":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, частота:{result[3]:.2f},"
                                       f" тип:{result[4]}, потребление энергии:{result[5]}")
                    self.label_characteristics.setText(characteristics)
                elif table_name == "hdd":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, объем:{result[3]} ГБ,"
                                       f" запись:{result[4]} MB/s, чтение:{result[5]} MB/s")
                    self.label_characteristics.setText(characteristics)
                elif table_name == "gpu":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f},"
                                       f" частота:{result[3]:.1f} ГГц, сокет:{result[4]},"
                                       f" потребление энергии:{result[5]} Вт")
                    self.label_characteristics.setText(characteristics)
                elif table_name == "frame":
                    characteristics = f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, форма:{result[3]}"
                    self.label_characteristics.setText(characteristics)
                elif table_name == "cpu":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, сокет:{result[3]},"
                                       f" частота:{result[4]:.1f} ГГц, потребление энергии:{result[5]} Вт")
                    self.label_characteristics.setText(characteristics)
                elif table_name == "cooler":
                    characteristics = (f"Выбранный компонент {result[1]}, цена:{result[2]:.2f}, скорость:{result[3]},"
                                       f" потребление энергии:{result[4]}")
                    self.label_characteristics.setText(characteristics)
            else:
                self.label_characteristics.setText("Компонент не найден")

    def update_table_widget_2(self, table_name, component_name):
        # Используем существующее соединение с базой данных
        with self.connection.cursor() as cursor:
            # Запрос к базе данных для получения всей строки выбранной записи
            cursor.execute(f"SELECT * FROM {table_name} WHERE name = %s", (component_name,))
            result = cursor.fetchone()
            print(result)

            # Очищаем таблицу перед добавлением новых данных
            self.tableWidget_2.clear()

            # Устанавливаем количество строк в таблице
            self.tableWidget_2.setRowCount(len(result)-1)

            # Устанавливаем количество столбцов в таблице (два столбца: название и значение)
            self.tableWidget_2.setColumnCount(2)

            # Заполняем второй столбец таблицы в зависимости от значения table_name
            if table_name == "motherboard":
                # Добавляем строки для motherboard
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Форм-фактор:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Сокет:"))
                self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Тип памяти:"))
                self.tableWidget_2.setItem(5, 0, QtWidgets.QTableWidgetItem("Интерфейсы:"))

                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "supply":
                # Очищаем таблицу перед добавлением новых данных
                self.tableWidget_2.clear()
                self.tableWidget_2.setRowCount(4)
                self.tableWidget_2.setColumnCount(2)

                # Добавляем строки для supply
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Мощность:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Тип:"))

                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "ram":
                # Очищаем таблицу перед добавлением новых данных
                self.tableWidget_2.clear()
                self.tableWidget_2.setRowCount(5)
                self.tableWidget_2.setColumnCount(2)

                # Добавляем строки для ram
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Частота:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Тип памяти:"))
                self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Потребление энергии:"))

                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "hdd":
                self.tableWidget_2.clear()
                self.tableWidget_2.setRowCount(5)
                self.tableWidget_2.setColumnCount(2)

                # Добавляем строки для hdd
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Объем:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Запись (MB/s):"))
                self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Чтение (MB/s):"))

                # Добавляем данные из component_name во второй столбец таблицы (без первого значения)
                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "gpu":
                self.tableWidget_2.clear()
                self.tableWidget_2.setRowCount(5)
                self.tableWidget_2.setColumnCount(2)

                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Частота:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Сокет:"))
                self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Потребление энергии:"))

                # Добавляем данные из component_name во второй столбец таблицы (без первого значения)
                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "frame":
                self.tableWidget_2.clear()
                self.tableWidget_2.setRowCount(3)
                self.tableWidget_2.setColumnCount(2)

                # Добавляем строки для frame
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Форм-фактор:"))

                # Добавляем данные из component_name во второй столбец таблицы (без первого значения)
                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "cpu":
                # Очищаем таблицу перед добавлением новых данных
                self.tableWidget_2.clear()

                # Устанавливаем количество строк в таблице
                self.tableWidget_2.setRowCount(5)  # Здесь 5 строк для 5 столбцов

                # Устанавливаем количество столбцов в таблице (два столбца: название и значение)
                self.tableWidget_2.setColumnCount(2)

                # Добавляем строки для cpu
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Сокет:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Частота:"))
                self.tableWidget_2.setItem(4, 0, QtWidgets.QTableWidgetItem("Потребление энергии:"))

                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

            elif table_name == "cooler":
                # Очищаем таблицу перед добавлением новых данных
                self.tableWidget_2.clear()

                # Устанавливаем количество строк в таблице
                self.tableWidget_2.setRowCount(4)  # Здесь 4 строки для 4 столбцов

                # Устанавливаем количество столбцов в таблице (два столбца: название и значение)
                self.tableWidget_2.setColumnCount(2)

                # Добавляем строки для cooler
                self.tableWidget_2.setItem(0, 0, QtWidgets.QTableWidgetItem("Имя:"))
                self.tableWidget_2.setItem(1, 0, QtWidgets.QTableWidgetItem("Цена:"))
                self.tableWidget_2.setItem(2, 0, QtWidgets.QTableWidgetItem("Скорость:"))
                self.tableWidget_2.setItem(3, 0, QtWidgets.QTableWidgetItem("Потребление энергии:"))

                with self.connection.cursor() as cursor:
                    # Запрос к базе данных для получения всей строки выбранной записи
                    query = f"SELECT * FROM {self.current_table_name} WHERE name = %s"
                    cursor.execute(query, (self.current_combobox_value,))
                    result = cursor.fetchone()
                    print(result)
                for row_index, column_value in enumerate(result[1:], 0):
                    self.tableWidget_2.setItem(row_index, 1, QTableWidgetItem(str(column_value)))

    def update_label_characteristics(self, table_name, current_combobox):
        # Получение последнего выбранного компонента
        selected_component_name = getattr(self, current_combobox).currentText()
        # print(selected_component_name)

        # Используем новый метод для поиска и отображения характеристик
        self.search_component_by_name(table_name, selected_component_name)

    def update_tableWidget2(self, table_name, current_combobox):
        selected_component_name = getattr(self, current_combobox).currentText()
        self.current_table_name = table_name
        self.current_combobox_value =  selected_component_name

        self.update_table_widget_2(table_name, selected_component_name)


    def load_all_configurations(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM configuration")
            configurations = cursor.fetchall()

            for configuration in configurations:
                confid = configuration[0]
                named = configuration[-1]
                component_names = self.get_component_names(cursor, configuration)
                configuration_text = f"Configuration {confid} {named}: {', '.join(component_names)}"
                self.listWidget.addItem(QListWidgetItem(configuration_text))

    def save_current_configuration(self):

        # Создаем новый словарь для текущей конфигурации
        current_configuration_ru = {
            "Материнская плата": self.comboBox_9.currentText(),
            "Блок питания": self.comboBox_10.currentText(),
            "Процессор": self.comboBox_11.currentText(),
            "Видеокарта": self.comboBox_12.currentText(),
            "Кулер": self.comboBox_13.currentText(),
            "Оперативная память": self.comboBox_14.currentText(),
            "Диск": self.comboBox_15.currentText(),
            "Корпус": self.comboBox_16.currentText(),
        }
        current_configuration_eng = {
            "motherboard": self.comboBox_9.currentText(),
            "supply": self.comboBox_10.currentText(),
            "cpu": self.comboBox_11.currentText(),
            "gpu": self.comboBox_12.currentText(),
            "cooler": self.comboBox_13.currentText(),
            "ram": self.comboBox_14.currentText(),
            "hdd": self.comboBox_15.currentText(),
            "frame": self.comboBox_16.currentText(),
        }

        value = self.open_dialog()

        component_ids = {}
        with self.connection.cursor() as cursor:
            for component_name, component_value in current_configuration_eng.items():
                # Замените названия таблиц на ваши реальные таблицы
                cursor.execute(f"SELECT id FROM {component_name} WHERE name = %s", (component_value,))
                result = cursor.fetchone()
                if result:
                    component_ids[component_name] = result[0]

            cursor.execute("SELECT MAX(confid) FROM configuration")
            max_confid = cursor.fetchone()[0] or 0  # Если нет записей, устанавливаем 0

            # Создаем запись в таблице configuration
            cursor.execute("""
                INSERT INTO configuration (conf_id, motherboard, supply, cpu, gpu, cooler, ram, hdd, frame, named)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                max_confid+1,
                component_ids.get("motherboard"),
                component_ids.get("supply"),
                component_ids.get("cpu"),
                component_ids.get("gpu"),
                component_ids.get("cooler"),
                component_ids.get("ram"),
                component_ids.get("hdd"),
                component_ids.get("frame"),
                value
            ))
            print(max_confid)

            configuration_text = f"Configuration {max_confid + 1} {value}: {', '.join(dict(current_configuration_ru).values())}"
            self.listWidget.addItem(configuration_text)

            # Сохраняем изменения
            self.connection.commit()

    def get_component_names(self, cursor, configuration_data):
        component_names = []
        component_ids = configuration_data[
                        1:]  # Пропускаем первый элемент, который является идентификатором конфигурации
        for component_id, table_name in zip(component_ids, COMPONENT_TABLES):
            # Извлекаем название компонента из таблицы по идентификатору
            cursor.execute(f"SELECT name FROM {table_name} WHERE id = %s", (component_id,))
            result = cursor.fetchone()
            if result:
                component_names.append(result[0])
        return component_names

    def show_selected_configuration(self):
        # Получаем выбранный элемент из listWidget
        selected_item = self.listWidget.currentItem()
        if selected_item is not None:
            configuration_text = selected_item.text()
            confid_start = configuration_text.find("Configuration") + len("Configuration") + 1  # Индекс начала id
            confid_end = configuration_text.find(" ", confid_start)  # Индекс конца id
            confid = configuration_text[confid_start:confid_end]
            print(f"{confid}")

        if selected_item:
            # Получаем текст конфигурации и извлекаем компоненты
            configuration_text = selected_item.text()
            components_text = configuration_text.split(": ")[1]
            components = components_text.split(", ")

            # Очищаем tableWidget перед добавлением новых данных
            self.tableWidget.clear()
            self.tableWidget.setRowCount(len(components))
            self.tableWidget.setColumnCount(2)

            # Добавляем компоненты в tableWidget
            for index, component in enumerate(components):
                self.tableWidget.setItem(index, 1, QTableWidgetItem(component))
                self.tableWidget.setItem(index, 0, QTableWidgetItem(
                    COMPONENT_TABLES_RU[index] if index != -1 else 'unknown'))

    def change_configuration(self):
        # Получаем выбранную конфигурацию
        selected_item = self.listWidget.currentItem()
        if selected_item:
            # Получаем текст конфигурации и извлекаем компоненты
            configuration_text = selected_item.text()
            components_text = configuration_text.split(": ")[1]
            components = components_text.split(", ")

            # Устанавливаем значения в соответствующие comboBox на вкладке create_conf
            self.comboBox_9.setCurrentText(components[0])
            self.comboBox_10.setCurrentText(components[1])
            self.comboBox_11.setCurrentText(components[2])
            self.comboBox_12.setCurrentText(components[3])
            self.comboBox_13.setCurrentText(components[4])
            self.comboBox_14.setCurrentText(components[5])
            self.comboBox_15.setCurrentText(components[6])
            self.comboBox_16.setCurrentText(components[7])

            # Переключаемся на вкладку create_conf
            self.tabWidget.setCurrentIndex(0)
            configuration_id = int(configuration_text.split(":")[0].split()[1])
            with self.connection.cursor() as cursor:
                delete_query = "DELETE FROM configuration WHERE confid = %s"
                cursor.execute(delete_query, (configuration_id,))
                self.connection.commit()

            row = self.listWidget.row(selected_item)
            self.listWidget.takeItem(row)

    def delete_configuration(self):
        # Получаем выбранную конфигурацию
        selected_item = self.listWidget.currentItem()

        if selected_item:
            configuration_text = selected_item.text()
            confid_str = configuration_text.split(":")[0].split()[1]
            confid = int(confid_str)
            print(confid)

            with self.connection.cursor() as cursor:
                cursor.execute("DELETE FROM configuration WHERE confid = %s", (confid,))
                self.connection.commit()

            row = self.listWidget.row(selected_item)
            self.listWidget.takeItem(row)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PCBUILDER"))
        self.label_mother_2.setText(_translate("MainWindow", "Материнская плата"))
        self.label_power_supply_2.setText(
            _translate("MainWindow", "<html><head/><body><p>Блок питания</p></body></html>"))
        self.label_cpu_2.setText(_translate("MainWindow", "Процессор"))
        self.label_gpu_2.setText(_translate("MainWindow", "Видеокарта"))
        self.label_cooler_2.setText(_translate("MainWindow", "Кулер"))
        self.label_ram_2.setText(_translate("MainWindow", "Оперативная память"))
        self.label_HDD_2.setText(_translate("MainWindow", "Жесткий диск"))
        self.label_frame_2.setText(_translate("MainWindow", "Корпус"))
        self.pushButton_save.setText(_translate("MainWindow", "сохранить конфигурацию"))
        self.label_characteristics.setText(_translate("MainWindow", "характеристики"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.create_conf),
                                  _translate("MainWindow", "Создание конфигурации"))
        self.Button_add.setText(_translate("MainWindow", "Добавить"))
        self.Button_update.setText(_translate("MainWindow", "Обновить"))
        self.Button_delete.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_addmother.setText(_translate("MainWindow", "+"))
        self.pushButton_addsupply.setText(_translate("MainWindow", "+"))
        self.pushButton_addcpu.setText(_translate("MainWindow", "+"))
        self.pushButton_addgpu.setText(_translate("MainWindow", "+"))
        self.pushButton_addcooler.setText(_translate("MainWindow", "+"))
        self.pushButton_addram.setText(_translate("MainWindow", "+"))
        self.pushButton_addHDD.setText(_translate("MainWindow", "+"))
        self.pushButton_addframe.setText(_translate("MainWindow", "+"))
        self.label_mother.setText(_translate("MainWindow", "Материнская плата"))
        self.label_power_supply.setText(
            _translate("MainWindow", "<html><head/><body><p>Блок питания</p></body></html>"))
        self.label_cpu.setText(_translate("MainWindow", "Процессор"))
        self.label_gpu.setText(_translate("MainWindow", "Видеокарта"))
        self.label_cooler.setText(_translate("MainWindow", "Кулер"))
        self.label_ram.setText(_translate("MainWindow", "Оперативная память"))
        self.label_HDD.setText(_translate("MainWindow", "Жесткий диск"))
        self.label_frame.setText(_translate("MainWindow", "Корпус"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_add_components),
                                  _translate("MainWindow", "Добавить компонент"))
        self.pushButton_change.setText(_translate("MainWindow", "Изменить"))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ready_conf),
                                  _translate("MainWindow", "Готовые конфигурации"))
def main():
    global app
    app = QtWidgets.QApplication(sys.argv)
    apply_theme(app, "dark")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()