import requests
import calendar
import datetime
import json
import csv
import pandas as pd
from bs4 import BeautifulSoup

data = []
date = []
avg_temp = []
max_temp = []
min_temp = []
rainy = []
now = datetime.datetime.now()
now_year = now.strftime('%Y')   #strftime() == 문자열을 전달받아서 시간정보로 나타낸다.
now_month = now.strftime('%m')

for y in range(2009,int(now_year)+1): #2011년부터 올해까지 반복
    print('크롤링 연도 : ' + str(y))
    if(str(y) == str(now_year)): #몇월까지 크롤링할지 정한다
        month_range = int(now_month) + 1
    else:
        month_range = 13
    
    
    day = ['']*7 #요일별 데이터 저장
    day_num = ['']*7 #몇일인지 저장 ex) 1일 ==> 1
    temp_avg = ['']*7 #평균기온 저장
    temp_max = ['']*7 #최고기온 저장
    temp_min = ['']*7 #최저기온 저장
    rain = ['']*7 #일 강수량 저장
    findex = ['']*7 #최고기온 시작 인덱스 저장
    sindex = ['']*7 #최저기온 시작 인덱스 저장
    tindex = ['']*7 #운량 시작 인덱스 저장
    ffindex = ['']*7 #강수량 시작 인덱스 저장
    
    for m in range(1,month_range):
        response = requests.get('http://www.kma.go.kr/weather/climate/past_cal.jsp?stn=108&yy='+str(y)+'&mm='+str(m)+'&obs=1')  
        #url 에서 request 객체 저장
        soup = BeautifulSoup(response.content,'html.parser')
        #request 객체를 html 문서로 변환
        table = soup.find('table',{'class' : 'table_develop' })
        #table class 이름이 table_develop 인거를 찾겠다는 거?
        column = 0 #몇번째 열인지 나타낸다 (짝수면 요일 홀수면 기온 정보)
        
        for tr in table.find_all('tr'): #테이블에서 tr 인거 모두 찾아라
            tds = list(tr.find_all('td')) #tr 에서 td 인거 모두 찾아라

            if len(tds) > 0 : #td가 존재한다면 실행
                for i in range(0,7):
                    day[i] = tds[i].text
        
                if column%2 != 0: #몇일인지에 관한 정보가 들어가 있는경우
                    for k in range(0,7):
                        day_num[k] = day[k].translate({ord('일'):''})
                    
                if column%2==0: #기온 정보가 있는 경우
                    for k in range(0,7): #7일 반복
                        findex[k] = day[k].find('최고기온')#시작 인덱스 찾기
                        sindex[k] = day[k].find('최저기온')
                        tindex[k] = day[k].find('평균운량')
                        ffindex[k] = day[k].find('일강수량')
                        temp_avg[k] = day[k][5:findex[k]].translate({ord('℃'):''})
                        temp_max[k] = day[k][findex[k]+5:sindex[k]].translate({ord('℃'):''})
                        temp_min[k] = day[k][sindex[k]+5:tindex[k]].translate({ord('℃'):''})
                        rain[k] = day[k][ffindex[k]+5:].translate({ord(' '):'',ord('-'):'0.0',ord('m'):''})
                        
                    if day[0]=='\xa0' or temp_avg[0]=='':
                        sun=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[0])
                        avg_temp.append(temp_avg[0])
                        max_temp.append(temp_max[0])
                        min_temp.append(temp_min[0])
                        rainy.append(rain[0])
                        #data.append([sun])
                        #print(sun)
                        
                    
                    if day[1]=='\xa0' or temp_avg[1]=='':
                        mon=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[1])
                        avg_temp.append(temp_avg[1])
                        max_temp.append(temp_max[1])
                        min_temp.append(temp_min[1])
                        rainy.append(rain[1])
                        #mon = str(y) + '-' + str(m) + '-'+day_num[1]+','+temp_avg[1] + ','+temp_max[1]+','+temp_min[1]+','+rain[1]
                        #data.append([mon])
                        #print(mon)
                        
                    if day[2]=='\xa0' or temp_avg[2]=='':
                        tue=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[2])
                        avg_temp.append(temp_avg[2])
                        max_temp.append(temp_max[2])
                        min_temp.append(temp_min[2])
                        rainy.append(rain[2])
                        #tue = str(y)+'-'+str(m)+'-'+day_num[2]+','+temp_avg[2]+','+temp_max[2]+','+temp_min[2]+','+rain[2]
                        #data.append([tue])
                        #print(tue)
                        
                    if day[3]=='\xa0' or temp_avg[3]=='':
                        wed=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[3])
                        avg_temp.append(temp_avg[3])
                        max_temp.append(temp_max[3])
                        min_temp.append(temp_min[3])
                        rainy.append(rain[3])
                        #wed = str(y) + '-' + str(m) + '-'+day_num[3]+','+temp_avg[3] + ','+temp_max[3]+','+temp_min[3]+','+rain[3]
                        #data.append([wed])
                        #print(wed)
                        
                    if day[4]=='\xa0' or temp_avg[4]=='':
                        thu=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[4])
                        avg_temp.append(temp_avg[4])
                        max_temp.append(temp_max[4])
                        min_temp.append(temp_min[4])
                        rainy.append(rain[4])
                        #thu = str(y) + '-' + str(m) + '-'+day_num[4]+','+temp_avg[4] + ','+temp_max[4]+','+temp_min[4]+','+rain[4]
                        #data.append([thu])
                        #print(thu)
                        
                    if day[5]=='\xa0' or temp_avg[5]=='':
                        fri=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[5])
                        avg_temp.append(temp_avg[5])
                        max_temp.append(temp_max[5])
                        min_temp.append(temp_min[5])
                        rainy.append(rain[5])
                        #fri = str(y) + '-' + str(m) + '-'+day_num[5]+','+temp_avg[5] + ','+temp_max[5]+','+temp_min[5]+','+rain[5]
                        #data.append([fri])
                        #print(fri)
                        
                    if day[6]=='\xa0' or temp_avg[6]=='':
                        sat=""
                    else:
                        date.append(str(y)+'/'+str(m)+'/'+day_num[6])
                        avg_temp.append(temp_avg[6])
                        max_temp.append(temp_max[6])
                        min_temp.append(temp_min[6])
                        rainy.append(rain[6])
                        #sat = str(y) + '-' + str(m) + '-'+day_num[6]+','+temp_avg[6] + ','+temp_max[6]+','+temp_min[6]+','+rain[6]
                        #data.append([sat])
                        #print(sat)
            column += 1

            
            

#data.append(date[:len(date)//4])
#data.append(avg_temp[:len(date)//4])
#data.append(max_temp[:len(date)//4])
#data.append(min_temp[:len(date)//4])
#data.append(rainy[:len(date)//4])

res = {}

c = ['date', 'avg_temp', 'max_temp', 'min_temp','rain_fall'] # 열의 이름

res[c[0]] = date[:len(date)]
res[c[1]] = avg_temp[:len(date)]
res[c[2]] = max_temp[:len(date)]
res[c[3]] = min_temp[:len(date)]
res[c[4]] = rainy[:len(date)]

#dictionary = dict(zip(c,data))
#json_val = json.dumps(dictionary)

#print(res)
try:
    df = pd.DataFrame(res)
    df.to_csv('weather.csv', encoding='cp949') # 한글이 깨지므로 인코딩
    # cp949, euc-kr
    print('저장 완료!')
except Exception as ex:
    print('저장 오류 ! ',ex)