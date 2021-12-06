# def solution(L, x):
#     answer = []
#
#     for i,j in enumerate(L):
#         if L.count(x) == 0:
#             answer.append(-1)
#             break
#
#         if j == x:
#             answer.append(i)
#
#     return answer
#
# L = [64, 72, 83, 72, 54]
# x = 49
# print(solution(L,x))


# MAP = [list(map(int, input().split())) for _ in range(int(input()))]
# print(MAP)

# from collections import Counter
#
# word = Counter(input().upper()).most_common()
# if len(word) > 1 and word[0][1] == word[1][1]:
#     print("?")
# else:
#     print(word[0][0])

# def solution(mylist):
#     answer = []
#     for number1, number2 in zip(mylist, mylist[1:]):
#         answer.append(abs(number1 - number2))
#     return answer
#
# if __name__ == '__main__':
#     mylist = [83, 48, 13, 4, 71, 11]
#     print(solution(mylist))


# word = [ord(i)+23 if ord(i)+23 <= 90 else ord(i)-3 for i in list(input())]
# print(''.join(list(map(chr,word))))

# fact = 1
# N = int(input())
# if N == 0:
#     print(1)
# else:
#     for i in range(1,N):
#         fact = fact*(i+1)
#     print(fact)

# value = set(map(lambda x: x if x%2==1 else 0, [int(input()) for _ in range(7)]))
# value.remove(0)
# if len(value) > 0:
#     print(f'{sum(value)}\n{min(value)}')
# else:
#     print(-1)

# for _ in range(int(input())):
#     binary = []
#     n = list(bin(int(input()))[2:])
#     n.reverse()
#
#     for i in range(len(n)):
#         if n[i] == '1':
#             binary.append(i)
#
#     print(*binary)

# from itertools import combinations
# def solution(nums):
#     nums_list = list(map(lambda x: sum(list(x)),combinations(nums,3)))
#     print(nums_list)
#     for i,j in enumerate(nums_list):
#         for k in nums:
#             if j%k == 0 and k != 1:
#                 nums_list[i] = 0
#                 break
#             else:
#                 pass
#
#     nums_list = set(nums_list)
#     nums_list.remove(0)
#     print(len(nums_list))
#
#
#
#
# nums = [1,2,7,6,4]
# solution(nums)

# from itertools import combinations

# class stack():
#     def __init__(self):
#         self.stack_list = []

#     def push(self,num):
#         self.stack_list.append(num)

#     def pop(self):
#         pass

#     def size(self):
#         pass

#     def empty(self):
#         pass

#     def top(self):
#         pass


# for _ in range(int(input())):
#     command = list(map(str, input().split()))
    

# 순열 for문으로 구축해보기 (Combinations편)

# start_num = 5
# result = []

# for i in range(1,start_num+1):
#     for j in range(i+1, start_num):
#         result.append((i,j))

# print(result)

# 순열 for문으로 구축해보기 (Permutations편)

# a = ['A','B','C']
# result = []

# for i in range(len(a)):
#     for j in range(len(a)):
#         if i == j:
#             pass
#         else:
#             result.append((a[i],a[j]))

# print(result)


# <<<<<<< Updated upstream
# <<<<<<< Updated upstream
# # Singled linked list (단일 연결 리스트)
# class Node:
#     def __init__(self, data, next = None) -> None:
#         self.data = data
#         self.next = next
    
# def init():    
#     global node1
#     # 데이터 부분
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(4)

#     # 포인터 부분
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4

# def insert(data):
#     global node1
#     new_node = Node(data)
#     new_node.next = node1
#     node1 = new_node

# def delete(delete_data):
#     global node1
#     prev_node = node1
#     next_node = node1.next
#     if delete_data == prev_node.data:
#         del prev_node
    
#     while next_node:
#         if delete_data == next_node.data:
#             prev_node.next = next_node.next
#             del next_node
#             break

#         prev_node = next_node
#         next_node = next_node.next

# def print_list():
#     global node1
#     prev_node = node1
#     while True:
#         print(prev_node.data)
#         if prev_node.next is None:
#             break
#         prev_node = prev_node.next

# init()
# insert(9)
# delete(3)
# print_list()

# import sys
# import os
# import openpyxl
# from openpyxl.drawing.image import Image

# '/Users/jskim2/Downloads/Coverage/coverage/12/pos1/total_coverage.png'.info['dpi']

# import sys

# cnt = 0
# stack = []
# N = int(input())
# post = list(input())

# for i in range(len(post)):
#     if post[i] == '+':
#         stack.append(stack.pop()+stack.pop())
#     if post[i] == '-':
#         stack.append(stack.pop()-stack.pop())
#     if post[i] == '*':
#         stack.append(stack.pop()*stack.pop())
#     if post[i] == '/':
#         stack.append(stack.pop()/stack.pop())
#     elif N > cnt:
#         cnt += 1
#         stack_num = int(sys.stdin.readline())
#     stack.append(stack_num)

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
                chatbot.sendMessage(chat_id=5064622110,
                                    text=j + " 의 예매가 오픈되었습니다.")
                # sc.pause()        

    else:
        chatbot.sendMessage(chat_id=5064622110, text="아직 오픈된 예매가 없습니다.")


# 스케쥴 구성을 위한 수행부
sc = BlockingScheduler()
sc.add_job(check_2d, 'interval', seconds=60)
sc.start()












        
# def ex4():
#     result = []
#     bs = BeautifulSoup(response.text, 'html.parser')
#     # CSS 처럼 셀렉터를 지정할 수 있다.
#     # tag = bs.find('div', attrs={'class': 'info-movie'})
#     tag = bs.find_all('div', attrs={"class": "col-times"})
#     if (tag):
#         for i in tag:
#             # 4dx 클래스값을 가진 항목이 있는지 검사
#             if (i.find(class_='info-movie')):
#                 # 해당 항목의 a > strong(타이틀부분) 가져옴
#                 title = i.select('a > strong')
#                 result.append(str(title))
#                 print(result)
#     # <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>


# url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=202&theatercode=0325&date="
# today = datetime.date.today().strftime("%Y%m%d")
# url += today

# response = requests.get(url)
# # print(response.text)
# ex4()

