import os
from os import path
from aip import AipSpeech
APP_ID = '15380593'
API_KEY = 'bC5co6MAUsgCrrB3HZqmmVG0'
SECRET_KEY = '7gQj25h6vIW17ZpYu3l82fRxI9kesNjT'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


#
#tex	String	合成的文本，使用UTF-8编码，请注意文本长度必须小于1024字节	是
#cuid	String	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内	否
#spd	String	语速，取值0-15，默认为5中语速	否
#pit	String	音调，取值0-15，默认为5中语调	否
#vol	String	音量，取值0-15，默认为5中音量	否
#per	String	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女	否
#
def get_bd_voice(str):
    result  = client.synthesis(str, 'zh', 1, {
        'spd': 2,
        'pit': 2,
        'vol': 5,
        'per': 4,
    })


    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f: #保存覆盖到当前路径
            f.write(result)
        return os.getcwd()+'\auido.mp3'
    else:
        return "failure"