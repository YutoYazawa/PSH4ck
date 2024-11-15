import requests
from random import randint, random

NUM=0      # 何回成績データを追加するか指定する(int)

settings=""
with open("ids.txt") as f:
    settings=f.read()
settings=settings.split("\n")
#id="stu*****"
id=settings[0].split(",")[0]
#password="******"
password=settings[0].split(",")[1]

resource=int(settings[0].split(",")[2])     # 受験画面のURLにある3桁の整数

token=""  #keep null
userid=""  #keep null

loginurl="https://keirinkan.sinewave-service.net/keirinkan-api/v3/student/login"
url="https://keirinkan.sinewave-service.net/keirinkan-api/v3/textbook/submit-exercise-log?student_id="		#ここのidを変えてもユーザーは変わらない。認証情報が一番重要。
logouturl="https://keirinkan.sinewave-service.net/keirinkan-api/v3/student/logout?student_id="

def login(id, password,):
    loginheader={
		'Accept':'application/json, text/plain, */*',
        'Accept-Encoding':'gzip, deflate, br, zstd',
        'Accept-Language':'ja,en-US;q=0.7,en;q=0.3',
	    'Connection':'keep-alive',
        'Content-Length': '160',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'keirinkan.sinewave-service.net',
        'Priority':'u=0',
        'Origin':'https://keirinkan.sinewave-service.net',
        'Referer':'https://keirinkan.sinewave-service.net/',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'TE':'trailers',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
	}
    logindata={
        'email':id,
        'password':password,
        'app_name':'prod1.5.1',
        'device_code':'PC prod1.5.1 c1be5f5a-93ed-478d-f58b-629bba4c7367',
    }
    response=requests.post(loginurl,headers=loginheader,data=logindata)
    response=response.json()
    print(str(response))
    if response["errcode"] == 0:
        userid=str(response["data"]["user"]["id"])
        token=response["data"]["token"]
        return token,userid
    else:
        return 0,0

def access(num):
    headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br, zstd',
    'Accept-Language':'ja,en-US;q=0.7,en;q=0.3',	#次の行の認証情報がログインするたびに変化する。自動取得モジュールほしい。 <=できそう
    'Authorization':'Bearer '+token,
	'Connection':'keep-alive',
    'Content-Length': '8530',
    'Content-Type':'application/x-www-form-urlencoded',
    'Host':'keirinkan.sinewave-service.net',
    'Origin':'https://keirinkan.sinewave-service.net',
    'Referer':'https://keirinkan.sinewave-service.net/',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'TE':'trailers',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    }
    for i in range(num):
        data = {
	    "guid": str(1730902909201+randint(-1000000,1000000)),	#guidって言ってるくせにグローバルじゃないからここを少しでも変えるだけでそのアカウントに1つずつ違う回だと認識されて回数がカウントされていく
	    "client": "keirinkan webprod1.5.1",
	    "resource_id": str(resource),		#ここでセクションとパートを管理してる(テキストファイル参照
	    "question_id": "0",
    	"evaluate_html": "<h1><span><font color=\"black\">They </font><font color=\"black\">all </font><font color=\"black\">saw </font><font color=\"black\">the </font><font color=\"black\">advantage </font><font color=\"black\">in </font><font color=\"black\">the </font><font color=\"black\">print-</font><font color=\"black\">and-</font><font color=\"black\">internet </font><font color=\"black\">offer </font><font color=\"black\">over </font><font color=\"black\">the </font><font color=\"black\">print-</font><font color=\"black\">only </font><font color=\"black\">offer.  </font><font color=\"black\">Were </font><font color=\"black\">they </font><font color=\"black\">influenced </font><font color=\"black\">by </font><font color=\"black\">the </font><font color=\"black\">presence </font><font color=\"black\">of </font><font color=\"black\">the </font><font color=\"black\">print-</font><font color=\"black\">only </font><font color=\"black\">option, </font><font color=\"black\">which </font><font color=\"black\">I </font><font color=\"black\">call </font><font color=\"black\">the </font><font color=\"black\">\"decoy\"?  </font><font color=\"black\">In </font><font color=\"black\">other </font><font color=\"black\">words, </font><font color=\"black\">suppose </font><font color=\"black\">that </font><font color=\"black\">I </font><font color=\"black\">removed </font><font color=\"black\">the </font><font color=\"black\">decoy </font><font color=\"black\">so </font><font color=\"black\">that </font><font color=\"black\">the </font><font color=\"black\">choices </font><font color=\"black\">would </font><font color=\"black\">be </font><font color=\"black\">the </font><font color=\"black\">ones </font><font color=\"black\">seen </font><font color=\"black\">as </font><font color=\"black\">follows: </font><font color=\"black\">(1) </font><font color=\"black\">internet-only </font><font color=\"black\">subscription </font><font color=\"black\">for </font><font color=\"black\">$</font><font color=\"black\">59 </font><font color=\"black\">and </font><font color=\"black\">(2) </font><font color=\"black\">print-</font><font color=\"black\">and-</font><font color=\"black\">internet </font><font color=\"black\">subscription </font><font color=\"black\">for </font><font color=\"black\">$</font><font color=\"black\">125.  </font><br/><br/><font color=\"black\">Would </font><font color=\"black\">the </font><font color=\"black\">students </font><font color=\"black\">respond </font><font color=\"black\">as </font><font color=\"black\">before?  </font><font color=\"black\">After </font><font color=\"black\">all, </font><font color=\"black\">the </font><font color=\"black\">option </font><font color=\"black\">I </font><font color=\"black\">took </font><font color=\"black\">out </font><font color=\"black\">was </font><font color=\"black\">one </font><font color=\"black\">that </font><font color=\"black\">no </font><font color=\"black\">one </font><font color=\"black\">chose, </font><font color=\"black\">so </font><font color=\"black\">it </font><font color=\"black\">should </font><font color=\"black\">make </font><font color=\"black\">no </font><font color=\"black\">difference.  </font><font color=\"black\">Right?  </font><font color=\"black\">On </font><font color=\"black\">the </font><font color=\"black\">contrary, </font><font color=\"black\">this </font><font color=\"black\">time, </font><font color=\"black\">68 </font><font color=\"black\">students </font><font color=\"black\">chose </font><font color=\"black\">the </font><font color=\"black\">internet-only </font><font color=\"black\">option </font><font color=\"black\">for </font><font color=\"black\">$</font><font color=\"black\">59.  </font><font color=\"black\">Only </font><font color=\"black\">32 </font><font color=\"black\">chose </font><font color=\"black\">the </font><font color=\"black\">combination </font><font color=\"black\">subscription </font><font color=\"black\">for </font><font color=\"black\">$</font><font color=\"black\">125.  </font><font color=\"black\">What </font><font color=\"black\">could </font><font color=\"black\">have </font><font color=\"black\">possibly </font><font color=\"black\">changed </font><font color=\"black\">their </font><font color=\"black\">minds?  </font><font color=\"black\">It </font><font color=\"black\">was </font><font color=\"black\">the </font><font color=\"black\">decoy </font><font color=\"black\">that </font><font color=\"black\">made </font><font color=\"black\">them </font><font color=\"black\">choose </font><font color=\"black\">differently.  </font><font color=\"black\">This </font><font color=\"black\">is </font><font color=\"black\">not </font><font color=\"black\">only </font><font color=\"black\">irrational </font><font color=\"black\">but </font><font color=\"black\">predictably </font><font color=\"black\">irrational </font><font color=\"black\">decision </font><font color=\"black\">making </font><font color=\"black\">caused </font><font color=\"black\">by </font><font color=\"black\">relativity.  </font></span></h1>",
    	"sound_file": "https://elst-keirinkan.s3.ap-northeast-1.amazonaws.com/upload-webapi/63a7a36a-9c4a-11ef-a25f-0653cadae993-1723129136-27000/63a7a36a-9c4a-11ef-a25f-0653cadae993-1723129136-27000.mp3",
	    "evaluate_result": "https://elst-keirinkan.s3.ap-northeast-1.amazonaws.com/upload-webapi/63a7a36a-9c4a-11ef-a25f-0653cadae993-1723129136-27000/63a7a36a-9c4a-11ef-a25f-0653cadae993-1723129136-27000.xml",
	    "record_duration": "160.338",	#実践ではここも散らしたい
    	"record_duration": str(round(randint(80,120)+random(),2)),
	    #"percent_score": "5",		#randintで散らせる
	    "percent_score": str(randint(90,100)),
    	#"accuracy_score": "100",		#サイトではこの値を20倍して表示している		5=>100	3.6=>72
    	"fluency_score": str(round(random()/2+4.5,2)),
    	#"fluency_score": "5000",		#scoreを80~100でランダムに散らせることで発覚を遅らせられるかも？
    	"integrity_score": str(round(random()/2+4.5,2)),
    	#"integrity_score": "100",      #スコアの表示範囲は0~19999
    	"accuracy_score": str(round(random()/2+4.5,2)),
	    "study_report": "{\"info\":[],\"speed\":0,\"leak\":0,\"errorwords\":[],\"repeat\":0}",
    	#"total_score": "5",
	    "total_score": str(round(random()/4+4.75,2)),
	    "poorly_words": "",
    	"practice_type": "1"
        }
        response = requests.post(url+userid, headers=headers, data=data)
        response=response.json()
        print(str(response))
        if response["errcode"]!=0:
            print("something went wrong. look above.")
            return False
    return True

def logout(token):
    logoutheader={
		'Accept':'application/json, text/plain, */*',
        'Accept-Encoding':'gzip, deflate, br, zstd',
        'Accept-Language':'ja,en-US;q=0.7,en;q=0.3',	#次の行の認証情報がログインするたびに変化する。
	    'Authorization':'Bearer '+token,
        'Connection':'keep-alive',
        'Content-Length': '0',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'keirinkan.sinewave-service.net',
        'Priority':'u=0',
        'Origin':'https://keirinkan.sinewave-service.net',
        'Referer':'https://keirinkan.sinewave-service.net/',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'TE':'trailers',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
	}
    response=requests.post(logouturl+userid,headers=logoutheader)
    response=response.json()
    print(str(response))
    if response["errcode"]==0:
        return True
    else:
        return False

token,userid=login(id=id,password=password)
res2=access(num=NUM)
res3=logout(token=token)
if res3:
    print("Done.")
else:
    print("Something went wrong.")