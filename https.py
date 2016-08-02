#coding=utf-8

import requests
import json

def getSmsCode(tel):
	res = requests.get("https://slack.com/api/channels.history?token=xoxp-2243966434-52358629782-58614973893-8c4b7e98f3&channel=C0CB3ARKP&count=5&pretty=1")
	#将https请求的返回值存入res
	json_str = res.content   #获取返回值

	datas = json.loads(json_str)   #解析js
	sms = datas['messages']       

	code = ""

	for item in sms:
	  if item.has_key("username") == False or item["username"] != "SMS":
	    continue
	  if item.has_key("text") == True and item["text"].find(tel) >= 0:
	  	code = item["text"][(item["text"].find("code:") + 6):]
	  	break

	return code


  
