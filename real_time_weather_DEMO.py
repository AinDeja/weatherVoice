import os
import urllib.request
import json
import bd_voice_PB
from datetime import date
from os import path
from playsound import playsound



#返回高德地图天气数据
def get_city_weather(city_id,search_type):
    if search_type == 0: # 实时天气
        url_weather = 'https://restapi.amap.com/v3/weather/weatherInfo?city='+city_id+'&extensions=base&key=c16c8cca95224a9d05141cc9ce0fd8f6'
    elif search_type == 1: # 预报天气
        url_weather = 'https://restapi.amap.com/v3/weather/weatherInfo?city='+city_id+'&extensions=all&key=c16c8cca95224a9d05141cc9ce0fd8f6'
    else:
        return -1
    #url_weather = 'https://free-api.heweather.com/v5/'+search+'?city='+index+'&key=和风天气KEY'
    response_url = urllib.request.urlopen(url_weather)
    context = response_url.read()
    get_weather_json = json.loads(context.decode('utf-8'))
    f = open("temp.txt", 'w')
    f.write(context.decode('utf-8'))
    f.close()
    if search_type == 0:
        weather = get_weather_json
        #print(weather)
        #weather = weather_json["HeWeather5"][0]['daily_forecast'][0]
    else:
        weather = get_weather_json
    return weather


#获取JSON中具体天气数据
def get_weather(city_id,search_type):
    _weather = get_city_weather(city_id,search_type)

    provi = _weather['lives'][0]['province']    #省份名      
    cityn = _weather['lives'][0]['city']        #城市名      
    adcod = _weather['lives'][0]['adcode']      #区域编码      
    weath = _weather['lives'][0]['weather']     #天气现象（汉字描述）      
    tempe = _weather['lives'][0]['temperature'] #实时气温，单位：摄氏度      
    windd = _weather['lives'][0]['winddirection']#风向描述  
    windp = _weather['lives'][0]['windpower']   #风力级别，单位：级      
    humid = _weather['lives'][0]['humidity']    #空气湿度      
    repor = _weather['lives'][0]['reporttime']  #数据发布的时间
    tempe=tempe.replace("-","零下")
    return "当前所在城市为{},当前天气为{},{}度,户外刮{}风,强度为{}级,空气湿度为{}，数据更新时间为{}.".format(cityn,weath,tempe,windd,windp,humid,repor)
                              

weather=get_weather('410102',0) #city_id 城市ID,search_type 天气类型 0：实时  1：预测
print(weather)
re=bd_voice_PB.get_bd_voice(weather) #通过百度API将文字转换为语音  re返回为语音mp3文件全路径
print(re)

# 播放转换后的语音 linux下
#try:
	# os.system('/usr/bin/mplayer -cache-min 80 -volume 80 "%s"' %(re))

#except Exception as e:
#    print('Exception',e)

# 播放转换后的语音 windows下
# 调用import playsound
playsound('auido.mp3')