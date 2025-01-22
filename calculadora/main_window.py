from PySide6.QtWidgets import ( QMainWindow, QVBoxLayout, QWidget,)

class MainWindow(QMainWindow):
    def __init__(self,parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, *kwargs)
        
        #Titulo da janela.
        self.setWindowTitle('Calculadora')
        

        #Configurando o layout básico.
        self.cw  = QWidget()
        self.vlayout = QVBoxLayout()
        self.cw.setLayout(self.vlayout)
        self.setCentralWidget(self.cw)
        


    def adjustFixedSize(self):
        #Ultima coisa a ser feita.
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def addToVlayout(self, widget: QWidget):
        self.vlayout.addWidget(widget)
