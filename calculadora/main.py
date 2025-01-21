import sys
from info import Info
from PySide6.QtGui import QIcon
from main_window import MainWindow
from display import Display
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    #Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    #Define o ícone.
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVlayout(info)



    #display
    display = Display()
    window.addToVlayout(display)
    display.setPlaceholderText('Digite Algo')


    #Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
    