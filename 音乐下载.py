import requests
import re
import os
def main(id,name):
    URL = requests.get('http://antiserver.kuwo.cn/anti.s?type=convert_url&rid='+id+'&format=aac|mp3&response=url')
    print(URL.text)
    Data = requests.get(str(URL.text)).content
    print('1.aac后缀\n2.mp3后缀\n温馨提示!  若不进行选择将默认为aac文件')
    suffix = int(input('选择:'))
    if suffix == 2:
        with open(name+'.aac',mode='wb') as f:
            f.write(Data)
        os.system('ffmpeg -i '+name+'.aac '+name+'.mp3')
        os.remove(name+'.aac')
        print('OK')
    else:
        with open(name+'.aac',mode='wb') as f:
            f.write(Data)
        print('Ok')
print('1.歌名下载\n2.歌曲id下载')
SELECT = int(input('请选择：'))
if SELECT == 1:
    Name = input('歌名：')
    url = 'http://search.kuwo.cn/r.s?all='+Name+'&ft=music& itemset=web_2013&client=kt&pn={1}&rn={2}&rformat=json&encoding=utf8'
    a =requests.get(url)
    a.encoding='utf-8'
    s = re.findall('(MUSIC_\d+)',a.text)
    print(a.text,'\n',s[0])
    main(s[0],Name)
elif SELECT == 2:
    ID = input('音乐id:')
    NAME = input('保存名称：')
    main(name=NAME,id=ID)