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
from PyQt5.QtCore import reset
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        # 모드 및 테스트 환경 입력 박스 (Top)
        # Robot 선택 버튼 생성
        self.selectRB = QComboBox(self)
        self.selectRB.addItem('RX2')
        self.selectRB.addItem('RX3')

        # 모드 및 테스트 환경 입력 박스 (Left)
        leftbox = QVBoxLayout()

        # 입력 또는 선택할 목록 세팅(이름)
        self.Label0 = QLabel('Serial Number : ', self)
        self.Label1 = QLabel('Mode : ', self)
        self.Label2 = QLabel('Position : ', self)
        self.Label3 = QLabel('Operating Time : ', self)
        self.Label4 = QLabel('SW ver : ', self)
        self.Label5 = QLabel('HW ver : ', self)
        self.Label6 = QLabel('FW ver : ', self)
        self.Label7 = QLabel('Temparature : ', self)
        
        leftbox.addWidget(self.Label0)
        leftbox.addWidget(self.Label1)
        leftbox.addWidget(self.Label2)
        leftbox.addWidget(self.Label3)
        leftbox.addWidget(self.Label4)
        leftbox.addWidget(self.Label5)
        leftbox.addWidget(self.Label6)
        leftbox.addWidget(self.Label7)
        

        # 모드 및 테스트 환경 입력 박스 (Right)
        rightbox = QVBoxLayout()

        # 주행 모드 / Position 선택 박스 생성 (ComboBox)
        self.modeBox = QComboBox(self)
        self.modeBox.addItem('Auto')
        self.modeBox.addItem('Silent')
        self.modeBox.addItem('Turbo')

        self.posBox = QComboBox(self)
        self.posBox.addItem('1')
        self.posBox.addItem('2')
        self.posBox.addItem('3')

        # 각 목록의 입력값을 받을 text Box 생성
        self.SerialNumber = QLineEdit()
        self.RValue1 = QLineEdit()
        self.RValue2 = QLineEdit()
        self.RValue3 = QLineEdit()
        self.RValue4 = QLineEdit()
        self.RValue5 = QLineEdit()

        # right 박스 내에 위에서 만든 위젯을 추가
        rightbox.addWidget(self.SerialNumber)
        rightbox.addWidget(self.modeBox)
        rightbox.addWidget(self.posBox)
        rightbox.addWidget(self.RValue1)
        rightbox.addWidget(self.RValue2)
        rightbox.addWidget(self.RValue3)
        rightbox.addWidget(self.RValue4)
        rightbox.addWidget(self.RValue5)

        # 전체적인 레이아웃 (right box, left box)를 QHBoxLayout으로 묶어 좌우측으로 배치되도록 설정
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftbox)
        mainLayout.addLayout(rightbox)

        #OK, Cancle, Reset 버튼 생성
        saveButton = QPushButton('Save')
        resetButton = QPushButton('Reset')

        # 버튼의 레이아웃 위치 조정 
        hbox = QHBoxLayout()
        hbox.addStretch(4)
        hbox.addWidget(saveButton)
        hbox.addWidget(resetButton)
        hbox.addStretch(3)

        vbox = QVBoxLayout()
        vbox.addStretch(9)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 최종 박스 (버튼의 레이아웃 + 메인 레이아웃)을 QVBoxLayout으로 묶어 상하단 정렬 형태로 출력
        resultBox = QVBoxLayout()
        resultBox.addWidget(self.selectRB)
        resultBox.addLayout(mainLayout)
        resultBox.addLayout(vbox)
        self.setLayout(resultBox)

        # 버튼 클릭 시 이벤트 생성(ResetButton)
        resetButton.clicked.connect(self.resetBTN_clicked)
        

        # 버튼 클릭 시 이벤트 생성(SaveButton)
        saveButton.released.connect(self.saveBTN_clicked)

        # 버튼 클릭 시 이벤트 생성(ExitButton)
        # exitButton.released.connect()

        # 창 이름 및 사이즈, 위치 설정
        self.setWindowTitle('Masterpiece')
        self.center()
        self.resize(250, 400)
        self.show()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def saveBTN_clicked(self):
        self.masterpiece = []
        self.masterpiece.append(str(self.selectRB.currentText()))
        self.masterpiece.append(self.SerialNumber.text())
        self.masterpiece.append(str(self.modeBox.currentText()))
        self.masterpiece.append(str(self.posBox.currentText()))
        self.masterpiece.append(self.RValue1.text())
        self.masterpiece.append(self.RValue2.text())
        self.masterpiece.append(self.RValue3.text())
        self.masterpiece.append(self.RValue4.text())
        self.masterpiece.append(self.RValue5.text())    

    def resetBTN_clicked(self):
        self.SerialNumber.clear()
        self.RValue1.clear()
        self.RValue2.clear()
        self.RValue3.clear()
        self.RValue4.clear()
        self.RValue5.clear()
        self.masterpiece = []
    
if __name__ == '__main__':
   app = QApplication(sys.argv)
   chamber = MyApp()
   if app.exec_() == 0:
       print(chamber.masterpiece)
       sys.exit()

   
   

# import openpyxl
# f = open("/Users/jskim2/Desktop/atom_algorithm/Algorithm/total_coverage.txt", 'r')
# print(f.readlines()[1].split(','))
# f.close()
