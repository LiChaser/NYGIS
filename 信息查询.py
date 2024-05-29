import requests
import re


token=input("请输入你的token：\n")
url = 'http://ygty.tzc.edu.cn/WeiXin/EXTest2.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090a13) XWEB/9129 Flue',
    'Referer': 'http://ygty.tzc.edu.cn/WeiXin/Skip.aspx?code=061MJzGa1mXZvH0Z8dIa18JPe32MJzGa&state=llks',
    'Cookie': f'userinfos=userid={token}&userroleid=9',
    'Connection': 'close',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}

response = requests.get(url, headers=headers)
# 假设response_text是你从网页中获取的HTML文本
# 使用正则表达式提取姓名和成绩
number_pattern=r'学号：(.*?)<br />'
name_pattern = r'姓名：(.*?)<br />'
score_pattern = r'体育理论考试成绩：(\d+?)分'
number = re.search(number_pattern, response.text).group(1)
name = re.search(name_pattern, response.text).group(1)
score = re.search(score_pattern, response.text).group(1)
print("学号:",number)
print("姓名：", name)
print("成绩：", score)