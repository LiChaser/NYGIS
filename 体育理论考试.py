import requests
import re

def get_score(s3_data,token):
    url = 'http://****.****.edu.cn/WeiXin/Handle/WeiXin.ashx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090a13) XWEB/9129 Flue',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://ygty.****.edu.cn',
        'Referer': 'http://ygty.****.edu.cn/WeiXin/EXPaper.aspx',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': f'userinfos=userid={token}&userroleid=9'
    }

    data = {
        's1': token,
        's2': 'EXHand',
        's3': s3_data
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.text)
    score = re.search(r'\d+', response.text).group()
    print("得分:"+score)

    return score

def find_correct_answers(token):
    prev_data = '4'   ##这里的prev就是第一个参数,这里默认第一个不参与验证爆破，如果需要满分,通过调整这里的prev_data参数看第一个输出得分是否能达到4即可。
    prev_score = 0

    for j in range(1, 51):
        send_data = ''
        step = False
        for i in range(1, 5):
            if step:
                break
            send_data = prev_data + '|' + str(i)
            print(send_data + (50 - j) * '|')
            score = int(get_score(send_data + (50 - j) * '|',token))
            if score > prev_score:
                prev_data = send_data
                prev_score = score
                step = True

        print(prev_data)

# 调用函数查找正确答案
token=input('请输入你的token:\n')
find_correct_answers(token)
