import sqlite3
from PyQt5 import uic, QtCore, QtGui, QtWidgets


def login(email, passw, signal):
    con = sqlite3.connect('db/db.sqlite')
    cur = con.cursor()

    # Проверка на существование аккаунта
    cur.execute(f'SELECT * FROM user WHERE email="{email}";')
    value = cur.fetchall()

    if value != [] and value[0][3] == passw:
        signal.emit('Ok')
        print('Авторизован')
    else:
        signal.emit('Неправильно введет логин или пароль')

    cur.close()
    con.close()


def registr(fio, email, passw, signal):
    con = sqlite3.connect('db/db.sqlite')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM user WHERE email="{email}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Аккаунт с этим email уже используется')
        osh = Osh('Аккаунт с этим email уже используется')
        osh.show()
    elif value == []:
        cur.execute(f"INSERT INTO user (fio, email, password) VALUES ('{fio}', '{email}', '{passw}')")
        print("Зарегистрирован")
        con.commit()

    cur.close()
    con.close()


class Osh(QtWidgets.QWidget):
    def __init__(self, text_osh):
        super().__init__()
        uic.loadUi('ui/osh.ui', self)
        self.initUI()
        self.label.setText(text_osh)
        self.vhod = App(self)
        self.pushButton.clicked.connect(self.vhod.show())