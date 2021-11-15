# class Time:
#     def __init__(self, hour, minute, second):
#         self.hour = hour
#         self.minute = minute
#         self.second = second

#     def is_time_valid(time_string):
#         hour, minute, second = map(int,time_string.split(':'))
#         return hour <= 24 and minute <= 59 and second <= 60
 
#     def from_string(time_string):
#         hour, minute, second = map(int, time_string.split(':'))
#         return Time(hour, minute, second)

# time_string = input()
 
# if Time.is_time_valid(time_string):
#     t = Time.from_string(time_string)
#     print(t.hour, t.minute, t.second)
# else:
#     print('잘못된 시간 형식입니다.')

import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 모드 및 테스트 환경 입력 박스 (Top)
        selectRB = QComboBox(self)
        selectRB.addItem('RX2')
        selectRB.addItem('RX3')

        # 모드 및 테스트 환경 입력 박스 (Left)
        leftbox = QVBoxLayout()

        Label0 = QLabel('Serial Number : ', self)
        Label1 = QLabel('Mode : ', self)
        Label2 = QLabel('Position : ', self)
        Label3 = QLabel('Operating Time : ', self)
        Label4 = QLabel('SW ver : ', self)
        Label5 = QLabel('HW ver : ', self)
        Label6 = QLabel('FW ver : ', self)
        Label7 = QLabel('Temparature : ', self)
        
        leftbox.addWidget(Label0)
        leftbox.addWidget(Label1)
        leftbox.addWidget(Label2)
        leftbox.addWidget(Label3)
        leftbox.addWidget(Label4)
        leftbox.addWidget(Label5)
        leftbox.addWidget(Label6)
        leftbox.addWidget(Label7)
        

        # 모드 및 테스트 환경 입력 박스 (Right)
        rightbox = QVBoxLayout()
        modeBox = QComboBox(self)
        modeBox.addItem('Auto')
        modeBox.addItem('Silent')
        modeBox.addItem('Turbo')

        posBox = QComboBox(self)
        posBox.addItem('1')
        posBox.addItem('2')
        posBox.addItem('3')


        SN = QLineEdit()
        RValue1 = QLineEdit()
        RValue2 = QLineEdit()
        RValue3 = QLineEdit()
        RValue4 = QLineEdit()
        RValue5 = QLineEdit()

        rightbox.addWidget(SN)
        rightbox.addWidget(modeBox)
        rightbox.addWidget(posBox)
        rightbox.addWidget(RValue1)
        rightbox.addWidget(RValue2)
        rightbox.addWidget(RValue3)
        rightbox.addWidget(RValue4)
        rightbox.addWidget(RValue5)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftbox)
        mainLayout.addLayout(rightbox)

        #OK, Cancle, Reset 버튼 레이아웃
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        resetButton = QPushButton('Reset')

        hbox = QHBoxLayout()
        hbox.addStretch(4)
        hbox.addWidget(okButton)
        hbox.addWidget(resetButton)
        hbox.addStretch(3)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(9)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        resultBox = QVBoxLayout()
        resultBox.addWidget(selectRB)
        resultBox.addLayout(mainLayout)
        resultBox.addLayout(vbox)
        self.setLayout(resultBox)


        # 창 이름 및 사이즈, 위치 설정
        self.setWindowTitle('Jayce')
        self.center()
        self.resize(200, 400)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())

# import openpyxl
# f = open("/Users/jskim2/Desktop/atom_algorithm/Algorithm/total_coverage.txt", 'r')
# print(f.readlines()[1].split(','))
# f.close()
