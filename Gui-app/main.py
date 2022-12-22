import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit,QAction

print('Starting...')
class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Create a QTextEdit widget and set it as the 
        # central widget
        # of the main window
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # create a QAction for quitting the application 
        # and add 
        # it to the File menu
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        self.file_menu = self.menuBar().addMenu("Options")
        self.file_menu.addAction(exit_action)

if True:
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())

print('Finished')
    