#coding:utf-8
import requests
weathre_url='http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weathre_data=requests.get(weathre_url).json()
print(weathre_data['title'])
for weathre in weathre_data['forecasts']:
    print(weathre['dateLabel'] + u'の天気は,' + weathre['telop'])
