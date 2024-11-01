import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # configurações da janela
        self.setWindowTitle("minha janela PyQT")
        self.setGeometry(100, 100, 400, 300) # (x, y, largura, altura)
        
if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())