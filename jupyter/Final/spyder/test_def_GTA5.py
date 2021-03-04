# -*- coding: utf-8 -*-
"""
# 이 서비스는 네이버 open API를 사용하였습니다.
# 이는  API이용 안내의 FAQ에 있는 "네이버 오픈API를 사용하고 있음을 나타내야 합니다."
# 에 의거하여 사용하고 있음을 알리는 바입니다.

# 애플리케이션이 네이버 오픈API를 사용해 개발한 프로그램이나 서비스라는 것을 링크나 네이버 로고를 통해 나타나야 합니다. 
# https://developers.naver.com/products/terms/ 의 이용약관을 준수하며
# 7.3 이용자는 API서비스를 이용함에 있어서 다음과 같은 행위를 하는 것이 금지됩니다.
# 에 위반되는 행위가 없음을 알리는 바입니다.

#https://developers.naver.com/docs/nmt/reference/
#papago 번역 : https://developers.naver.com/docs/papago/papago-nmt-overview.md
#언어감지 : https://developers.naver.com/docs/papago/papago-detectlangs-overview.md

#urllib.request : https://docs.python.org/ko/3/library/urllib.html
# "https://openapi.naver.com/v1/papago/detectLangs"
"""


import urllib.request
import json
import numpy as np
import pandas as pd

client_ID = "heOXaJbWApy2jeSAg27E"
client_PW = "huLrZTZTOW"


# -----------------------------------------
#번역 대상 언어 코드.
Code = {'Language' : ['Auto', 'Korean', 'English', 'Chinese_sim', 'Chinese_tra',
                      'Spanish', 'French', 'Vietnamese', 'Thai', 'Indonesian'],
       'Code' : ['au', 'ko', 'en', 'zh-CN', 'zh-TW', 'es', 'fr', 'vi', 'th', 'id'],
       'Note' : ['언어감지', '한국어', '영어', '중국어_간체', '중국어_번체',
                    '스페인어', '프랑스어', '베트남어', '태국어', '인도네시아어']}
print("-" * 35)
df = pd.DataFrame(Code)
print(df)
print("-" * 35)

#ko<->en, ko<->zh-CN, ko<->zh-TW, ko<->es, ko<->fr,
#ko<->vi, ko<->th, ko<->id, en<->ja, en<->fr 조합만 가능
# -----------------------------------------
auto_t = input("언어 자동사용을 사용하시겠습니까? : (Y or N)")

#선택하는 것 또한 가능하다.
if auto_t == "N":
    stat_O = True
    
    while stat_O:
        try:
            origin_lang = int(input("번역을 원하는 언어의 번호를 선택하여 주세요. : "))
        except ValueError:
            print("다시 선택해 주시기 바랍니다.")
            continue
        except IndexError:
            print("다시 선택해 주시기 바랍니다.")
            continue
                    
        if origin_lang < 0 or origin_lang > 9:
            print("다시 선택해 주시기 바랍니다.")
            continue
        
        print("\n선택한 언어입니다 : \n") 
        print(df.loc[origin_lang])
        origin_lang_c = df.loc[origin_lang][1]
        if origin_lang == 0:
            print("입력한 언어가 한국어일 경우 영어가, 영어일 경우 한국어가 자동으로 번역됩니다.")
        
        re_origin = input("바꾸시겠습니까? : (Y or N)")
        if re_origin == "N":
            stat_O = False
        elif re_origin == "Y":
            continue

 
    stat_T = True
    while stat_T:
        try:
            trans_lang = int(input("번역하고 싶은 언어의 번호를 선택하여 주세요. : "))
        except ValueError:
            print("다시 선택해 주시기 바랍니다.")
            continue
        except IndexError:
            print("다시 선택해 주시기 바랍니다.")
            continue
                    
        if origin_lang < 0 or origin_lang > 9:
            print("다시 선택해 주시기 바랍니다.")
            continue
        
        
        print("\n선택한 언어입니다 : \n") 
        print(df.loc[origin_lang])
        trans_lang_c = df.loc[trans_lang][1]
                            
        if trans_lang == 0:
            print("입력한 언어가 한국어일 경우 영어가, 영어일 경우 한국어가 자동으로 번역됩니다.")
            
        re_trans = input("바꾸시겠습니까? : (Y or N)")
        if re_trans == "N":
            stat_T = False
        elif re_trans == "Y":
            continue
         

else: 
    # 자동 선택이 가능하다.
    print("언어 자동감지 사용 : ")
    print("입력한 언어가 한국어일 경우 영어가, 영어일 경우 한국어가 자동으로 번역됩니다.")
    origin_lang = 0 
    origin_lang_c = df.loc[origin_lang][1]
    trans_lang = 0
    trans_lang_c = df.loc[trans_lang][1]
    print("설정 : " + origin_lang_c + " => " + trans_lang_c)
    
#----------------------------------------
#계속해서 번역 가능하게 할 수 있음.
stat_S = True
while stat_S:
    Text = input("번역하고 싶은 내용을 적어주세요. (프로그램 종료코드 : stat_Stop | 코드목록보기 : list_code): \n")
    if Text == "stat_stop":
        stat_S = False    
        break
    elif Text == "list_code":
        
        list_code = {'Code' : ['stat_stop', 'list_code'],
                     'Mean_en' : ['Stop the program', 'list of code'],
                     'Mean_kr' : ['프로그램을 정지한다.', '코드의 리스트를 보여준다.']}            
        df_code = pd.DataFrame(list_code)
        print("-" * 70)
        print(df_code)
        print("-" * 70)
        continue
# -----------------------------------------
    #자동 언어 탐색
    encQuery = urllib.parse.quote(Text)
    data_au = "query=" + encQuery
    url_au = "https://openapi.naver.com/v1/papago/detectLangs"
    request_au = urllib.request.Request(url_au)
    request_au.add_header("X-Naver-Client-Id",client_ID)
    request_au.add_header("X-Naver-Client-Secret",client_PW)
    response_au = urllib.request.urlopen(request_au, data=data_au.encode("utf-8"))
    rescode_au = response_au.getcode()
    if(rescode_au==200):
        response_au_body = response_au.read()
        auto_t = response_au_body.decode('utf-8')
        auto_d_t = json.loads(auto_t)
        auto_lang = auto_d_t["langCode"]
        
    else:
        print("Error Code:" + rescode_au)
    
# -----------------------------------------
    #언어 지정
    your_language = origin_lang_c
    target_language = trans_lang_c

    if origin_lang_c == "au":
        if auto_lang == "ko":
            your_language = auto_lang
            target_language = "en"
        elif auto_lang == "en":
            your_language = auto_lang
            target_language = "ko"
        else:
            your_languagev = auto_lang
            target_language = "en"
            

    #언어 번역
    want_Text = urllib.parse.quote(Text)

    data_tr = "source="+your_language+"&target="+target_language+"&text="+want_Text
    url_tr = "https://openapi.naver.com/v1/papago/n2mt"

    request_tr = urllib.request.Request(url_tr)
    request_tr.add_header("X-Naver-Client-Id",client_ID)
    request_tr.add_header("X-Naver-Client-Secret",client_PW)
    response_tr = urllib.request.urlopen(request_tr, data=data_tr.encode("utf-8"))
    rescode_tr = response_tr.getcode()

    if(rescode_tr==200):
        response_tr_body = response_tr.read()
        trans_Text = response_tr_body.decode('utf-8')

    
        #결과부분 슬라이싱
        result_Text = trans_Text[95:-2]

        #str형식을 dict형식으로 변환
        result_d_Text = json.loads(result_Text)
    
        you_lang = result_d_Text["srcLangType"]

        tar_lang = result_d_Text["tarLangType"]

        translate = result_d_Text["translatedText"]
        
        print("-" * 100)
        print("Original [" + you_lang + "] : " + Text) 
        print("=> Translation [" + tar_lang + "] : " + translate)
        print("-" * 100)
        
    else:
        print("Error Code:" + rescode_tr)


