import urllib.request
import re
from bs4 import BeautifulSoup
import pandas as pd

page1 = urllib.request.urlopen("http://ncov.mohw.go.kr/").read()
soup1 = BeautifulSoup(page1, 'html.parser')

patient_data = soup1.find('div', {'class' : 'container'})

current_data = patient_data.find('div', {'class' : 'liveNumOuter'})
when_current = current_data.find('span', {'class' : 'livedate'}).text  
print(when_current)

when_current_t = re.split('\W+', when_current)
print(when_current_t)
when = (when_current_t[1]+'월 '+when_current_t[2]+'일 '+when_current_t[3]+' '+when_current_t[4])
print(when)

today_current = current_data.find('div', {'class' : 'liveNum_today_new'})

tit = today_current.find('strong', {'class' : 'tit'}).text
subtit = today_current.find('span', {'class' : 'subtit'}).text

subtit_number = today_current.find('span', {'class' : 'data'}).text
when_current_info= (when+' '+tit+' 중 '+subtit+'자는 '+subtit_number+"명 입니다. \n")
print(when_current_info)
page2 = urllib.request.urlopen("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=").read()
soup2 = BeautifulSoup(page2, 'html.parser')
#table_today = soup2.find('table',{'class':'num midsize'})
data = []

tables = soup2.select('table')
table_html = str(tables)
table_df_list = pd.read_html(table_html)
table_df = table_df_list[0]

print(table_df)

print(table_df.columns)

table_df_y = table_df[["시도명", "전일대비확진환자 증감"]]
table_df_y_i = table_df[[("시도명","시도명"), ("전일대비확진환자 증감", "국내발생")]]

x_c = table_df[["시도명"]]
y_c = table_df[[("전일대비확진환자 증감", "합계")]]
y_c_in = table_df[[("전일대비확진환자 증감", "국내발생")]]
y_c_out = table_df[[("전일대비확진환자 증감", "해외유입")]]
print(y_c_out)


ax = table_df_y.plot(kind='barh', stacked=True, title="COVID19 시도별 발생동향", rot=0)
for p in ax.patches:
    left, bottom, width, height = p.get_bbox().bounds
    ax.annotate("%.1f"%(width*100), xy=(left+width/2, bottom+height/2), ha='center', va='center')
plt.box(False)

plt.xlabel("도시")
plt.ylabel("전일 대비 확진환자")
plt.title("COVID19 시도별 발생동향")

#plt.show()