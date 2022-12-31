import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

print('Starting...')
class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create a QTextEdit widget and set it as the 
        # central widget
        # of the main window
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # create a Qaction for saving and loading
        #  the application
        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_notes)
        load_action = QAction("Load",self)
        load_action.triggered.connect(self.load_notes)

        # create a QAction for quitting the application 
        # and add 
        # it to the file menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        self.file_menu = self.menuBar().addMenu("File")
        self.formatting_menu = self.menuBar().addMenu("Formatting")

        # add it to the file menu
        self.file_menu.addAction(save_action)
        self.file_menu.addAction(load_action)
        self.file_menu.addAction(exit_action)

        # add it to the formatting menu
        self.formatting_menu.addAction(save_action)
    
    def save_notes(self):
        options = QFileDialog.options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self,"Save Notes","Text Files(*.txt);;All Files(*)", options=options)
        if file_name:
            with open(file_name, 'w') as f:
                f.write(self.text_edit.toPlainText())
    
    def load_notes(self):
        options = QFileDialog.options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self,"Load Notes","Text Files(*.txt);;All Files(*)", options=options)
        if file_name:
            with open(file_name, 'r') as f:
                self.text_edit.setPlainText(f.read())


if True:
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())

print('Finished')
    