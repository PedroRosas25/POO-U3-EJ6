from menu import Menu
from manejador import Manejador as M

if __name__=='__main__':
    menu=Menu()
    m=M()
    m.cargarlista()
    menu.opciones(m)