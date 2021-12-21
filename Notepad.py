#QTPY

#참조
#https://www.youtube.com/watch?v=Ss7dDDS-DhU&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&ab_channel=%EC%9E%AC%EC%A6%90%EB%B3%B4%ED%94%84
#https://wikidocs.net/35478
#https://appia.tistory.com/298


import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDialog, QFileDialog, QTextEdit, QHBoxLayout, QVBoxLayout
from googletrans import Translator
from PyQt5 import uic

#UI파일 연결
form_class = uic.loadUiType("font.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class fontPopup(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


        # 버튼에 기능을 연결하는 코드
        self.pushButton.clicked.connect(self.okButtonFunction)
        self.pushButton_2.clicked.connect(self.cancelButtonFunction)

    def okButtonFunction(self):
        self.close()

    def cancelButtonFunction(self):
        self.close()


class QtGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("Notepad")
        menubar = self.menuBar()

        Filemenu = menubar.addMenu("File")
        Filemenu1 = menubar.addMenu("Format")
        Filemenu2 = menubar.addMenu("Trans")

        loadfile = QAction('laod File ...', self)
        savefile = QAction('save File ...', self)
        exit = QAction('Exit', self)
        fontset = QAction('Font', self)
        transtexten = QAction('English', self)
        transtextko = QAction('Korean', self)

        loadfile.triggered.connect(self.add_open)
        savefile.triggered.connect(self.add_save)
        fontset.triggered.connect(self.font_popup)

        exit.triggered.connect(qApp.quit)
        Filemenu.addAction(loadfile)
        Filemenu.addAction(savefile)
        Filemenu.addAction(exit)

        transtexten.triggered.connect(self.trans_text_en)
        transtextko.triggered.connect(self.trans_text_ko)

        Filemenu1.addAction(fontset)
        Filemenu2.addAction(transtexten)
        Filemenu2.addAction(transtextko)

        self.text1 = QTextEdit(self)
        self.text1.setAcceptRichText(True)
        self.setCentralWidget(self.text1)
        self.show()

    def add_open(self):
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
        f = open(FileOpen[0], 'r')
        textcontenct = f.read()
        self.text1.setText(textcontenct)
        f.close()

    def add_save(self):
        FileSave = QFileDialog.getSaveFileName(self, 'Save file', './')
        textcontent = self.text1.toPlainText()
        f = open(FileSave[0], 'w')
        f.write(textcontent)
        f.close()

    def trans_text_en(self):
        translator = Translator()
        textcontent = self.text1.toPlainText()
        tr_result = translator.translate(textcontent)
        self.text1.append('->' + tr_result.text)

    def trans_text_ko(self):
        translator = Translator()
        textcontent = self.text1.toPlainText()
        tr_result = translator.translate(textcontent, src='auto', dest="ko")
        self.text1.append('->' + tr_result.text)

    def font_popup(self):
        popup = fontPopup()
        popup.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtGUI()
    app.exec_()
