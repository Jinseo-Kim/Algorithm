import datetime
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler


def check_2d():
    # CGV 메인 도메인 + 예매시간표 페이지 iframe 내 자원주소(src)
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=202&theatercode=0325&date=20211214"

    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    chatbot = telegram.Bot(token='5048329112:AAF4lvw_NfPr1zV74eD6ZtYD9yd6gHXYAMw')
    chatbot_2 = telegram.Bot(token='5006420253:AAE5ezcKn-Ioj1nw_5hHsfJMpOiv3yH2R2c')


    result = []

    # 이상한 값이 끼어들어와서 이후에 replace로 날려줄 값
    nullvalue = '[<strong>\r\n                                                '
    nullvalue2 = '</strong>]'

    # 상영목록이 담긴 리스트를 받아옴
    two_d = bs.find_all('div', attrs={"class": "col-times"})

    if (two_d):
        for i in two_d:
            # 4dx 클래스값을 가진 항목이 있는지 검사
            if (i.find(class_='info-movie')):
                # 해당 항목의 a > strong(타이틀부분) 가져옴
                title = i.select('a > strong')
                result.append(str(title))

        result = [word.replace(nullvalue, '') for word in result]
        result = [word.replace(nullvalue2, '') for word in result]
        
        for i,j in enumerate(result):
            if j.find('듄') == -1:
                result[i] = 0
            else:
                chatbot.sendMessage(chat_id=5064622110,text=j + " 의 예매가 오픈되었습니다.")
                chatbot_2.sendMessage(chat_id=5009781554,text=j + " 의 예매가 오픈되었습니다.")
                # sc.pause()

    else:
        chatbot.sendMessage(chat_id=5064622110, text="아직 오픈된 예매가 없습니다.")
        chatbot_2.sendMessage(chat_id=5009781554, text="아직 오픈된 예매가 없습니다.")


# 스케쥴 구성을 위한 수행부
sc = BlockingScheduler()
sc.add_job(check_2d, 'interval', seconds=60)
sc.start()
