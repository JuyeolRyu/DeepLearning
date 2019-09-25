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
now_year = now.strftime('%Y')   #strftime() == ���ڿ��� ���޹޾Ƽ� �ð������� ��Ÿ����.
now_month = now.strftime('%m')

for y in range(2009,int(now_year)+1): #2011����� ���ر��� �ݺ�
    print('ũ�Ѹ� ���� : ' + str(y))
    if(str(y) == str(now_year)): #������� ũ�Ѹ����� ���Ѵ�
        month_range = int(now_month) + 1
    else:
        month_range = 13
    
    
    day = ['']*7 #���Ϻ� ������ ����
    day_num = ['']*7 #�������� ���� ex) 1�� ==> 1
    temp_avg = ['']*7 #��ձ�� ����
    temp_max = ['']*7 #�ְ��� ����
    temp_min = ['']*7 #������� ����
    rain = ['']*7 #�� ������ ����
    findex = ['']*7 #�ְ��� ���� �ε��� ����
    sindex = ['']*7 #������� ���� �ε��� ����
    tindex = ['']*7 #� ���� �ε��� ����
    ffindex = ['']*7 #������ ���� �ε��� ����
    
    for m in range(1,month_range):
        response = requests.get('http://www.kma.go.kr/weather/climate/past_cal.jsp?stn=108&yy='+str(y)+'&mm='+str(m)+'&obs=1')  
        #url ���� request ��ü ����
        soup = BeautifulSoup(response.content,'html.parser')
        #request ��ü�� html ������ ��ȯ
        table = soup.find('table',{'class' : 'table_develop' })
        #table class �̸��� table_develop �ΰŸ� ã�ڴٴ� ��?
        column = 0 #���° ������ ��Ÿ���� (¦���� ���� Ȧ���� ��� ����)
        
        for tr in table.find_all('tr'): #���̺��� tr �ΰ� ��� ã�ƶ�
            tds = list(tr.find_all('td')) #tr ���� td �ΰ� ��� ã�ƶ�

            if len(tds) > 0 : #td�� �����Ѵٸ� ����
                for i in range(0,7):
                    day[i] = tds[i].text
        
                if column%2 != 0: #���������� ���� ������ �� �ִ°��
                    for k in range(0,7):
                        day_num[k] = day[k].translate({ord('��'):''})
                    
                if column%2==0: #��� ������ �ִ� ���
                    for k in range(0,7): #7�� �ݺ�
                        findex[k] = day[k].find('�ְ���')#���� �ε��� ã��
                        sindex[k] = day[k].find('�������')
                        tindex[k] = day[k].find('��տ')
                        ffindex[k] = day[k].find('�ϰ�����')
                        temp_avg[k] = day[k][5:findex[k]].translate({ord('��'):''})
                        temp_max[k] = day[k][findex[k]+5:sindex[k]].translate({ord('��'):''})
                        temp_min[k] = day[k][sindex[k]+5:tindex[k]].translate({ord('��'):''})
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

c = ['date', 'avg_temp', 'max_temp', 'min_temp','rain_fall'] # ���� �̸�

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
    df.to_csv('weather.csv', encoding='cp949') # �ѱ��� �����Ƿ� ���ڵ�
    # cp949, euc-kr
    print('���� �Ϸ�!')
except Exception as ex:
    print('���� ���� ! ',ex)