from PyQt5.QtWidgets import  (QApplication, QMainWindow, QVBoxLayout, QScrollArea,
                             QLineEdit, QHBoxLayout, QFrame, 
                             QPushButton, QLabel, QDialog, QWidget)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QTableWidget, QTextEdit

from db_mysql import (insert_test_uge, insert_test_ugts, insert_test_ugts, 
                       insert_test_uge, get_all_tests_uge, get_all_tests_ugts,
                       search_test_uge, search_test_ugts, delete_test_uge, delete_test_ugts_title,
                       update_test_uge, update_test_ugts, create_table_version_UGE, save_all_to_csv_ygts,
                       insert_test_in_version_ugts, create_table_version_UGTS, get_all_tests_ugts_version)

class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CTF MAGALLY')
        self.resize(400, 200)

        #self.windowUGE = WindowUGE()  
        self.windowUGTS = WindowUGTS()

        mainLayout = QVBoxLayout()  

        verticalSpacerTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(verticalSpacerTop)

        buttonUGE = QPushButton('Base de Donnée UGE')
        buttonUGE.setFixedWidth(230)
        buttonUGE.clicked.connect(lambda chacked: self.toggle_window(self.windowUGE))

        hLayoutUGE = QHBoxLayout()
        hLayoutUGE.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Left spacer
        hLayoutUGE.addWidget(buttonUGE)
        hLayoutUGE.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Right spacer

        mainLayout.addLayout(hLayoutUGE)  # Add the horizontal layout to the main vertical layout

        buttonUGTS = QPushButton('Base de Donnée UGTS')
        buttonUGTS.setFixedWidth(230)
        buttonUGTS.clicked.connect(lambda checked: self.toggle_window(self.windowUGTS))

        hLayoutUGTS = QHBoxLayout()
        hLayoutUGTS.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  
        hLayoutUGTS.addWidget(buttonUGTS)
        hLayoutUGTS.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  

        mainLayout.addLayout(hLayoutUGTS)  

        verticalSpacerBottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(verticalSpacerBottom)

        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

# class WindowUGE(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         self.load_collection()
#         self.setWindowTitle("BD UGE")
#         self.resize(1000,800)

#     def initUI(self):
#         self.main_layout = QVBoxLayout(self)  
#         self.search_widget = SearchRecordUGE(self)
#         self.main_layout.addWidget(self.search_widget)
#         tests_label = QLabel('Tests')
#         tests_label.setStyleSheet('font-size:18px;')
#         self.main_layout.addWidget(tests_label)
#         self.test_collection_area()

#     def test_collection_area(self):
#         scroll_frame = QFrame()
#         self.test_collection_layout = QVBoxLayout(scroll_frame)
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)
#         scroll.setWidget(scroll_frame)
#         scroll.setStyleSheet('QScrollArea{border:0px}')
#         self.test_collection_layout.addStretch()
#         self.main_layout.addWidget(scroll)        

#     def load_collection(self):
#         for i in reversed(range(self.test_collection_layout.count())):
#             widget = self.test_collection_layout.itemAt(i).widget()
#             if widget is not None: 
#                 widget.deleteLater()
        
#         collections = get_all_tests_uge()
#         for collection in collections: 
#             frame = TestCardUGE(*collection, self)
#             self.test_collection_layout.insertWidget(0, frame)        

#     def load_collection_search(self, test):
#         for i in reversed(range(self.test_collection_layout.count())):
#             widget = self.test_collection_layout.itemAt(i).widget()
#             if widget is not None: 
#                 widget.deleteLater()

#         collections = search_test_uge(test)
#         for collection in collections: 
#             frame = TestCardUGE(*collection, self)
#             self.test_collection_layout.insertWidget(0, frame)

#     def update_test_uge(self, test_id, scenario, test, orig, cat, agr, n_ugts, objet_du_test):
#         dialog = UpdateTestDialogUGE(self, test_id, scenario, test, orig, cat, agr, n_ugts, objet_du_test)
#         dialog.exec()  
    
#     def add_test_uge(self):
#         dialog = CreateRecordUGE(self)
#         dialog.exec()

class WindowUGTS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_collection()
        self.setWindowTitle("BD UGTS")
        self.resize(1000,800)
            
    def initUI(self):
        self.main_layout = QVBoxLayout(self)  
        self.search_widget = SearchRecordUGTS(self)
        self.main_layout.addWidget(self.search_widget)
        tests_label = QLabel('Tests')
        tests_label.setStyleSheet('font-size:18px;')
        self.main_layout.addWidget(tests_label)
        self.test_collection_area()

    def test_collection_area(self):
        scroll_frame = QFrame()
        self.test_collection_layout = QVBoxLayout(scroll_frame)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(scroll_frame)
        scroll.setStyleSheet('QScrollArea{border:0px}')
        self.test_collection_layout.addStretch()
        self.main_layout.addWidget(scroll)        

    def load_collection(self):
        for i in reversed(range(self.test_collection_layout.count())):
            widget = self.test_collection_layout.itemAt(i).widget()
            if widget is not None: 
                widget.deleteLater()
        
        collections = get_all_tests_ugts()
        for collection in collections: 
            frame = TestCardUGTS(*collection, self)
            self.test_collection_layout.insertWidget(0, frame)

    def load_collection_version(self, version):
        for i in reversed(range(self.test_collection_layout.count())):
            widget = self.test_collection_layout.itemAt(i).widget()
            if widget is not None: 
                widget.deleteLater()
        
        collections = get_all_tests_ugts_version(version)
        for collection in collections: 
            frame = TestCardUGTS(*collection, self)
            self.test_collection_layout.insertWidget(0, frame)
                
    def load_collection_search(self, test):
        for i in reversed(range(self.test_collection_layout.count())):
            widget = self.test_collection_layout.itemAt(i).widget()
            if widget is not None: 
                widget.deleteLater()

        collections = search_test_ugts(test)
        for collection in collections: 
            frame = TestCardUGTS(*collection, self)
            self.test_collection_layout.insertWidget(0, frame)

    def update_test_ugts(self, test_id, scenario, test, orig, cat, agr, n_ugts, objet_du_test):
        dialog = UpdateTestDialogUGTS(self, test_id, scenario, test, orig, cat, agr, n_ugts, objet_du_test)
        dialog.exec()  
    
    def add_test_ugts(self):
        dialog = CreateRecordUGTStest(self)
        dialog.exec()
   
    def delete_test_ugts(self):
        dialog = DeleteTestUGTS(self)
        dialog.exec()
    
    def version_test_ugts(self):
        dialog = VersionTestUGTS(self)
        dialog.exec()

class VersionTestUGTS(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle('Version Test')

        self.main_layout = QVBoxLayout(self)

        self.layoutt = QHBoxLayout(self)
        self.test_line = QLineEdit()
        self.label = QLabel('Créer Une Nouvelle Version:')
        self.test_line.setPlaceholderText('Nom Version')
        self.push_button = QPushButton(text='Créer')
        self.push_button.clicked.connect(self.create_version)

        self.layoutt.addWidget(self.test_line)
        self.layoutt.addWidget(self.push_button)

        self.label_one = QLabel('Tagger un Test:')

        self.layout_2 = QHBoxLayout(self)
        self.label_one_2 = QLabel('Test:')
        self.test_line_2 = QLineEdit()
        self.test_line_2.setPlaceholderText('Nom Test')
        
        self.layout_2.addWidget(self.label_one_2)
        self.layout_2.addWidget(self.test_line_2)
        
        self.layout_3 = QHBoxLayout(self)
        self.label_one_3 = QLabel('Version:')
        self.test_line_3 = QLineEdit()
        self.test_line_3.setPlaceholderText('Nom Version')
        self.push_button_2 = QPushButton(text='Tagger')
        self.push_button_2.clicked.connect(self.tagger_test)

        self.layout_3.addWidget(self.label_one_3)
        self.layout_3.addWidget(self.test_line_3)

        self.push_button_3 = QPushButton(text='Créer')

        self.main_layout.addWidget(self.label)
        self.main_layout.addLayout(self.layoutt)
        self.main_layout.addWidget(self.label_one)
        self.main_layout.addLayout(self.layout_2)
        self.main_layout.addLayout(self.layout_3)
        self.main_layout.addWidget(self.push_button_2)

    def create_version(self):
        version_name = self.test_line.text()
        
        if version_name:
            create_table_version_UGTS(version_name)

    def tagger_test(self): 
        test_name = self.test_line_2.text()
        version_name = self.test_line_3.text()

        if test_name and version_name:
            print(test_name)
            print(version_name)
            insert_test_in_version_ugts(test_name,version_name)
            

            
class DeleteTestUGTS(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle('Delete Test')
        self.setFixedSize(300,300)

        self.layout = QVBoxLayout(self)
        self.label = QLabel('Nom du test à supprimer:')
        self.test_line = QLineEdit()
        self.test_line.setPlaceholderText('Nom Test')
        self.push_button = QPushButton(text='Supprimer')
        self.push_button.clicked.connect(self.delete_test)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.test_line)
        self.layout.addWidget(self.push_button)


    def delete_test(self):
        
        test = self.test_line.text()
        if test:
            delete_test_ugts_title(test)
            self.main_window.load_collection()
        
# class SearchRecordUGE(QFrame): 
#     def __init__(self, main_window):
#         super().__init__()
#         self.main_window = main_window
 
#         layout = QHBoxLayout(self)  # Use a vertical layout

#         self.search_bar = QLineEdit()
#         self.search_bar.setPlaceholderText('Test Title')
#         layout.addWidget(self.search_bar)

#         self.search_button = QPushButton(text='Search')
#         self.search_button.clicked.connect(self.search_test)
#         layout.addWidget(self.search_button)

#         self.clear_button = QPushButton(text='Clear')
#         self.clear_button.clicked.connect(self.clear_find_all)
#         layout.addWidget(self.clear_button)

#         self.add_button = QPushButton(text="Add Test +", clicked = lambda: self.add_test_click(main_window))
#         layout.addWidget(self.add_button)

#     def add_test_click(self, main_window):
#         main_window.add_test_uge()

#     def search_test(self):

#         test = self.search_bar.text()
#         if test:
#             self.main_window.load_collection_search(test)
#             self.search_bar.clear()
    
#     def clear_find_all(self):
#         self.main_window.load_collection()

class SearchRecordUGTS(QFrame): 
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Main vertical layout
        layout_main = QVBoxLayout(self)

        # Version selection layout
        layout_version = QHBoxLayout()
        self.select_version = QLabel('Select version:')
        self.select_version_box = QLineEdit()
        self.select_version_box.setPlaceholderText('Version')
        self.search_button = QPushButton('Search in Version')
        self.search_button.clicked.connect(self.find_all_version)

        self.export_button = QPushButton('Export csv')
        self.export_button.clicked.connect(self.save_to_csv)


        # Setting fixed width to make it smaller
        self.select_version.setFixedWidth(100)
        self.select_version_box.setFixedWidth(200)
        
        layout_version.addWidget(self.select_version)
        layout_version.addWidget(self.select_version_box)
        layout_version.addWidget(self.search_button)
        layout_version.addWidget(self.export_button)
        layout_version.addStretch()  
        # Search and action buttons layout
        layout_actions = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText('Test Title')
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.search_test)
        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_find_all)
        self.add_button = QPushButton('Add Test +', clicked=lambda: self.add_test_click(main_window))
        self.delete_button = QPushButton('Delete Test', clicked=lambda: self.delete_test_click(main_window))
        self.version_button = QPushButton('+ Version', clicked=lambda: self.version_test_click(main_window))

        layout_actions.addWidget(self.search_bar)
        layout_actions.addWidget(self.search_button)
        layout_actions.addWidget(self.clear_button)
        layout_actions.addWidget(self.add_button)
        layout_actions.addWidget(self.delete_button)
        layout_actions.addWidget(self.version_button)

        # Adding sub-layouts to the main layout
        layout_main.addLayout(layout_version)
        layout_main.addLayout(layout_actions)

    def save_to_csv(self):
        version = self.select_version_box.text()
        print(f"Version: {version}")
        if not version:
            print(f"Version here 1: {version}")
            version = 0  
        else:
            try:
                version = int(version)  
            except ValueError:
                version = 0  
        print(f"Version here 2: {version}")
        save_all_to_csv_ygts(version)


    def add_test_click(self, main_window):
        main_window.add_test_ugts()

    def delete_test_click(self, main_window):
        main_window.delete_test_ugts()

    def version_test_click(self, main_window):
        main_window.version_test_ugts()

    def search_test(self):
        test = self.search_bar.text()
        if test:
            self.main_window.load_collection_search(test)
            self.search_bar.clear()
    
    def clear_find_all(self):
        self.main_window.load_collection()

    def find_all_version(self):
        version = self.select_version_box.text()

        if version:
            self.main_window.load_collection_version(version)

class CreateRecordUGTStest(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle('Add Test')
        self.setFixedSize(500,400)
       
        self.scenario = QLineEdit()
        self.scenario.setPlaceholderText('Scenario')

        self.test = QLineEdit()
        self.test.setPlaceholderText('Test')

        self.orig = QLineEdit()
        self.orig.setPlaceholderText('Orig')

        self.agr = QLineEdit()
        self.agr.setPlaceholderText('Agr')

        self.cat = QLineEdit()
        self.cat.setPlaceholderText('Cat')

        self.n_ugts = QLineEdit()
        self.n_ugts.setPlaceholderText('N° UGTS')

        self.objet_du_test = QLineEdit()
        self.objet_du_test.setPlaceholderText('Objet Du Test')
        self.objet_du_test.setFixedHeight(100)

        self.add_button = QPushButton(text='Add Test')

        self.add_button.clicked.connect(self.add_test)

        main_layout = QVBoxLayout(self)

        # First row of inputs: scenario, test, orig
        row1_layout = QHBoxLayout()
        line1_row1 = QHBoxLayout()

        line1_row1.addWidget(QLabel('Scenario:'))
        row1_layout.addWidget(self.scenario)
        line1_row1.addWidget(QLabel('Test:'))
        row1_layout.addWidget(self.test)
        line1_row1.addWidget(QLabel('Orig:'))
        row1_layout.addWidget(self.orig)
        main_layout.addLayout(line1_row1)
        main_layout.addLayout(row1_layout)  

        row2_layout = QHBoxLayout()
        line1_row2 = QHBoxLayout()
        line1_row2.addWidget(QLabel('Cat:'))
        row2_layout.addWidget(self.cat)
        line1_row2.addWidget(QLabel('Agr:'))
        row2_layout.addWidget(self.agr)
        line1_row2.addWidget(QLabel('N° UGTS:'))
        row2_layout.addWidget(self.n_ugts)
        main_layout.addLayout(line1_row2)
        main_layout.addLayout(row2_layout)  
        main_layout.setSpacing(5)
        main_layout.addWidget(QLabel('Objet du Test:'))
        main_layout.addWidget(self.objet_du_test)

        main_layout.addWidget(self.add_button)
        
    def add_test(self):
        scenario = self.scenario.text()
        test = self.test.text()
        orig = self.orig.text()
        cat = self.cat.text()
        agr = self.agr.text()
        n_ugts = self.n_ugts.text()
        objet_du_test = self.objet_du_test.text()

        if all([scenario, test, orig, cat, agr, n_ugts, objet_du_test]):
            insert_test_ugts(scenario, test, orig, cat, agr, n_ugts, objet_du_test)

            self.main_window.load_collection()

            self.scenario.clear()
            self.test.clear()
            self.orig.clear()
            self.cat.clear()
            self.agr.clear()
            self.n_ugts.clear()
            self.objet_du_test.clear()

# class CreateRecordUGE(QDialog):
#     def __init__(self, main_window):
#         super().__init__()
#         self.main_window = main_window
#         self.setWindowTitle('Add Test')
#         self.setFixedSize(500,400)
       
#         self.scenario = QLineEdit()
#         self.scenario.setPlaceholderText('Scenario')

#         self.test = QLineEdit()
#         self.test.setPlaceholderText('Test')

#         self.orig = QLineEdit()
#         self.orig.setPlaceholderText('Orig')

#         self.agr = QLineEdit()
#         self.agr.setPlaceholderText('Agr')

#         self.cat = QLineEdit()
#         self.cat.setPlaceholderText('Cat')

#         self.n_ugts = QLineEdit()
#         self.n_ugts.setPlaceholderText('N° UGTS')

#         self.objet_du_test = QLineEdit()
#         self.objet_du_test.setPlaceholderText('Objet Du Test')
#         self.objet_du_test.setFixedHeight(100)

#         self.add_button = QPushButton(text='Add Test')

#         self.add_button.clicked.connect(self.add_test)

#         main_layout = QVBoxLayout(self)

#         # First row of inputs: scenario, test, orig
#         row1_layout = QHBoxLayout()
#         line1_row1 = QHBoxLayout()

#         line1_row1.addWidget(QLabel('Scenario:'))
#         row1_layout.addWidget(self.scenario)
#         line1_row1.addWidget(QLabel('Test:'))
#         row1_layout.addWidget(self.test)
#         line1_row1.addWidget(QLabel('Orig:'))
#         row1_layout.addWidget(self.orig)
#         main_layout.addLayout(line1_row1)
#         main_layout.addLayout(row1_layout)  

#         row2_layout = QHBoxLayout()
#         line1_row2 = QHBoxLayout()
#         line1_row2.addWidget(QLabel('Cat:'))
#         row2_layout.addWidget(self.cat)
#         line1_row2.addWidget(QLabel('Agr:'))
#         row2_layout.addWidget(self.agr)
#         line1_row2.addWidget(QLabel('N° UGTS:'))
#         row2_layout.addWidget(self.n_ugts)
#         main_layout.addLayout(line1_row2)
#         main_layout.addLayout(row2_layout)  
#         main_layout.setSpacing(5)
#         main_layout.addWidget(QLabel('Objet du Test:'))
#         main_layout.addWidget(self.objet_du_test)

#         main_layout.addWidget(self.add_button)
        
#     def add_test(self):
#         scenario = self.scenario.text()
#         test = self.test.text()
#         orig = self.orig.text()
#         cat = self.cat.text()
#         agr = self.agr.text()
#         n_ugts = self.n_ugts.text()
#         objet_du_test = self.objet_du_test.text()

#         if all([scenario, test, orig, cat, agr, n_ugts, objet_du_test]):
#             insert_test_uge(scenario, test, orig, cat, agr, n_ugts, objet_du_test)

#             self.main_window.load_collection()

#             self.scenario.clear()
#             self.test.clear()
#             self.orig.clear()
#             self.cat.clear()
#             self.agr.clear()
#             self.n_ugts.clear()
#             self.objet_du_test.clear()

# class TestCardUGE(QFrame):
#     def __init__(self, test_id, scenario, test, orig, cat, agr, n_ugts, objet_du_test, main_window):
#         super().__init__()
#         self.main_window = main_window 
#         self.test_id, self.scenario, self.test, self.orig, self.cat, self.agr, self.n_ugts, self.objet_du_test = test_id, scenario, test, orig, cat, agr, n_ugts, objet_du_test

#         self.setStyleSheet('background:white; border-radius:4px; color:black;')
#         self.setFixedHeight(50)
#         layout = QHBoxLayout()
#         layout.setSpacing(10)  # Set spacing between widgets in the layout

#         # Adding labels to the layout
#         scenario_label = QLabel(f'<strong>{scenario}</strong>')
#         test_label = QLabel(f'<strong>{test}</strong>')
#         orig_label = QLabel(f'<strong>{orig}</strong>')
#         cat_label = QLabel(f'<strong>{cat}</strong>')
#         agr_label = QLabel(f'<strong>{agr}</strong>')
#         n_ugts_label = QLabel(f'<strong>{n_ugts}</strong>')
#         objet_du_test_label = QLabel(f'<strong>{objet_du_test}</strong>')

#         layout.addWidget(scenario_label)
#         layout.addWidget(test_label)
#         layout.addWidget(orig_label)
#         layout.addWidget(cat_label)
#         layout.addWidget(agr_label)
#         layout.addWidget(n_ugts_label)
#         layout.addWidget(objet_du_test_label)

#         layout.addStretch()  

#         delete_button = QPushButton(text='Delete', clicked=self.delete_test_click)
#         delete_button.setFixedWidth(60)
#         delete_button.setStyleSheet('background:orange; padding:3px;')
#         layout.addWidget(delete_button)

#         layout.addSpacing(5)  

#         edit_button = QPushButton(text='Edit', clicked=lambda: self.edit_test_click(main_window))
#         edit_button.setFixedWidth(60)
#         edit_button.setStyleSheet('background:lightblue; padding:3px;')
#         layout.addWidget(edit_button)

#         self.setLayout(layout)

#     def delete_test_click(self):
#         delete_test_uge(self.test_id)
#         self.close()

#     def edit_test_click(self, main_window):
#         main_window.update_test_uge(self.test_id, self.scenario, self.test, self.orig, self.cat, self.agr, self.n_ugts, self.objet_du_test)

class TestCardUGTS(QFrame):
    def __init__(self, test_id, scenario, test, cat, agr, orig, n_ugts, objet_du_test, main_window):
        super().__init__()
        self.main_window = main_window 
        self.test_id, self.scenario, self.test, self.cat, self.agr, self.orig, self.n_ugts, self.objet_du_test = test_id, scenario, test, cat, agr, orig, n_ugts, objet_du_test

        self.setStyleSheet('background:white; border-radius:4px; color:black;')
        layout = QHBoxLayout(self)  
        self.table = QTableWidget()
        self.table.setShowGrid(False)
        self.table.setStyleSheet('QTableView::item {border-right: 1px solid #d6d9dc;}')
        self.table.setColumnCount(7)  

        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(False)

        # Set header labels
        self.table.setHorizontalHeaderLabels([
            "Scenario", "Test", "Cat", "Agr", "Orig", "N_UGTS", "Objet_du_Test"
        ])

        self.add_table_row(scenario, test, cat, agr, orig, n_ugts, objet_du_test)

        layout.addWidget(self.table)
        self.setLayout(layout)

    def add_table_row(self, scenario, test, cat, agr, orig, n_ugts, objet_du_test):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

        # Insert data into each cell using QLineEdit for text columns
        text_items = [
            QLineEdit(scenario),
            QLineEdit(test),
            QLineEdit(cat),
            QLineEdit(agr),
            QLineEdit(orig),
            QLineEdit(n_ugts),
        ]

        for i, editor in enumerate(text_items):
            editor.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.table.setCellWidget(row_position, i, editor)
            editor.textChanged.connect(lambda _, row=row_position, col=i: self.on_text_changed(row, col))

        for i in range(2):  
            self.table.setColumnWidth(i, 150) 

        for i in range(2, 6):
            self.table.setColumnWidth(i, 50) 
        
        # Use QTextEdit for objet_du_test
        objet_du_test_editor = QTextEdit(objet_du_test)
        objet_du_test_editor.setAlignment(Qt.AlignCenter)
        objet_du_test_editor.setReadOnly(False)
        self.table.setCellWidget(row_position, 6, objet_du_test_editor)
        objet_du_test_editor.textChanged.connect(lambda: self.on_text_changed(row_position, 6))

        self.table.setColumnWidth(6, 599)  
        self.adjust_row_height(row_position, 6)

    

    def adjust_row_height(self, row, column):
        cell_widget = self.table.cellWidget(row, column)
        if cell_widget:
            document = cell_widget.document()
            content_height = int(document.size().height()) + 30
            self.table.setRowHeight(row, content_height)
            self.setFixedHeight(content_height + 20)
        
    def on_text_changed(self, row, column):
        cell_widget = self.table.cellWidget(row, column)
        if cell_widget:
            new_value = cell_widget.text() if isinstance(cell_widget, QLineEdit) else cell_widget.toPlainText()
            self.update_data(row, column, new_value)

    def update_data(self, row, column, new_value):
        if column == 0:
            self.scenario = new_value
        elif column == 1:
            self.test = new_value
        elif column == 2:
            self.cat = new_value
        elif column == 3:
            self.agr = new_value
        elif column == 4:
            self.orig = new_value
        elif column == 5:
            self.n_ugts = new_value
        elif column == 6:
            self.objet_du_test = new_value

        self.send_to_backend()

    def send_to_backend(self):
        update_test_ugts(
            self.test_id,
            self.scenario,
            self.test,
            self.cat,
            self.agr,
            self.orig,
            self.n_ugts,
            self.objet_du_test
        )

# class UpdateTestDialogUGE(QDialog): 
#     def __init__(self, main_window, test_id, scenario, test, agr, orig, cat, n_ugts, objet_du_test):
#         super().__init__(main_window)
#         self.main_window = main_window 
#         self.test_id = test_id 
#         self.setWindowTitle('Update Test')
#         self.setFixedSize(500,400)

#         self.test_scenario_edit = QLineEdit()
#         self.test_scenario_edit.setText(scenario)
        
#         self.test_test_edit = QLineEdit()
#         self.test_test_edit.setText(test)

#         self.test_agr_edit = QLineEdit()
#         self.test_agr_edit.setText(agr)

#         self.test_orig_edit = QLineEdit()
#         self.test_orig_edit.setText(orig)

#         self.test_cat_edit = QLineEdit()
#         self.test_cat_edit.setText(cat)

#         self.test_n_ugts_edit = QLineEdit()
#         self.test_n_ugts_edit.setText(n_ugts)

#         self.test_objet_du_test_edit = QLineEdit()
#         self.test_objet_du_test_edit.setText(objet_du_test)
#         self.test_objet_du_test_edit.setFixedHeight(100)

#         self.action_button_layout = QHBoxLayout()
#         self.save_button = QPushButton(text="Save", clicked=self.save_update)
#         self.cancel_button = QPushButton(text="Cancel", clicked=self.accept)

#         self.main_layout = QVBoxLayout()

#         row1_layout = QHBoxLayout()
#         line1_row1 = QHBoxLayout()

#         line1_row1.addWidget(QLabel('Scenario:'))
#         row1_layout.addWidget(self.test_scenario_edit)
#         line1_row1.addWidget(QLabel('Test:'))
#         row1_layout.addWidget(self.test_test_edit)
#         line1_row1.addWidget(QLabel('Agr:'))
#         row1_layout.addWidget(self.test_agr_edit)
#         self.main_layout.addLayout(line1_row1)
#         self.main_layout.addLayout(row1_layout) 

#         row2_layout = QHBoxLayout()
#         line1_row2 = QHBoxLayout()
#         line1_row2.addWidget(QLabel('Cat:'))
#         row2_layout.addWidget(self.test_cat_edit)
#         line1_row2.addWidget(QLabel('Orig:'))
#         row2_layout.addWidget(self.test_orig_edit)
#         line1_row2.addWidget(QLabel('N° UGTS:'))
#         row2_layout.addWidget(self.test_n_ugts_edit)
#         self.main_layout.addLayout(line1_row2)
#         self.main_layout.addLayout(row2_layout)  
#         self.main_layout.setSpacing(5)
#         self.main_layout.addWidget(QLabel('Objet du Test:'))
#         self.main_layout.addWidget(self.test_objet_du_test_edit)
#         self.action_button_layout.addWidget(self.save_button)
#         self.action_button_layout.addWidget(self.cancel_button)
#         self.main_layout.addLayout(self.action_button_layout)
#         self.setLayout(self.main_layout)

#     def save_update(self):
#         updated_scenario, updated_test, updated_cat, updated_agr, updated_orig, updated_n_ugts, updated_objet_du_test = self.test_scenario_edit.text(), self.test_test_edit.text(), self.test_cat_edit.text(), self.test_agr_edit.text(), self.test_orig_edit.text(), self.test_n_ugts_edit.text(), self.test_objet_du_test_edit.text()
#         update_test_uge(self.test_id, updated_scenario, updated_test, updated_cat, updated_agr, updated_orig, updated_n_ugts, updated_objet_du_test )
#         self.accept()
#         self.main_window.load_collection()

class UpdateTestDialogUGTS(QDialog): 
    def __init__(self, main_window, test_id, scenario, test, agr, orig, cat, n_ugts, objet_du_test):
        super().__init__(main_window)
        self.main_window = main_window 
        self.test_id = test_id 
        self.setWindowTitle('Update Test')
        self.setFixedSize(500,400)

        self.test_scenario_edit = QLineEdit()
        self.test_scenario_edit.setText(scenario)
        
        self.test_test_edit = QLineEdit()
        self.test_test_edit.setText(test)

        self.test_agr_edit = QLineEdit()
        self.test_agr_edit.setText(agr)

        self.test_orig_edit = QLineEdit()
        self.test_orig_edit.setText(orig)

        self.test_cat_edit = QLineEdit()
        self.test_cat_edit.setText(cat)

        self.test_n_ugts_edit = QLineEdit()
        self.test_n_ugts_edit.setText(n_ugts)

        self.test_objet_du_test_edit = QLineEdit()
        self.test_objet_du_test_edit.setText(objet_du_test)
        self.test_objet_du_test_edit.setFixedHeight(100)

        self.action_button_layout = QHBoxLayout()
        self.save_button = QPushButton(text="Save", clicked=self.save_update)
        self.cancel_button = QPushButton(text="Cancel", clicked=self.accept)

        self.main_layout = QVBoxLayout()

        row1_layout = QHBoxLayout()
        line1_row1 = QHBoxLayout()

        line1_row1.addWidget(QLabel('Scenario:'))
        row1_layout.addWidget(self.test_scenario_edit)
        line1_row1.addWidget(QLabel('Test:'))
        row1_layout.addWidget(self.test_test_edit)
        line1_row1.addWidget(QLabel('Agr:'))
        row1_layout.addWidget(self.test_agr_edit)
        self.main_layout.addLayout(line1_row1)
        self.main_layout.addLayout(row1_layout) 

        row2_layout = QHBoxLayout()
        line1_row2 = QHBoxLayout()
        line1_row2.addWidget(QLabel('Cat:'))
        row2_layout.addWidget(self.test_cat_edit)
        line1_row2.addWidget(QLabel('Orig:'))
        row2_layout.addWidget(self.test_orig_edit)
        line1_row2.addWidget(QLabel('N° UGTS:'))
        row2_layout.addWidget(self.test_n_ugts_edit)
        self.main_layout.addLayout(line1_row2)
        self.main_layout.addLayout(row2_layout)  
        self.main_layout.setSpacing(5)
        self.main_layout.addWidget(QLabel('Objet du Test:'))
        self.main_layout.addWidget(self.test_objet_du_test_edit)
        self.action_button_layout.addWidget(self.save_button)
        self.action_button_layout.addWidget(self.cancel_button)
        self.main_layout.addLayout(self.action_button_layout)
        self.setLayout(self.main_layout)

    def save_update(self):
        updated_scenario, updated_test, updated_cat, updated_agr, updated_orig, updated_n_ugts, updated_objet_du_test = self.test_scenario_edit.text(), self.test_test_edit.text(), self.test_cat_edit.text(), self.test_agr_edit.text(), self.test_orig_edit.text(), self.test_n_ugts_edit.text(), self.test_objet_du_test_edit.text()
        update_test_ugts(self.test_id, updated_scenario, updated_test, updated_cat, updated_agr, updated_orig, updated_n_ugts, updated_objet_du_test )
        self.accept()
        self.main_window.load_collection()

def main():
    app = QApplication([])
    app.setStyle('fusion')
    win = Main()
    win.show()
    app.exec_()  

if __name__ == '__main__':
    main()



