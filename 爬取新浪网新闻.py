import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.sina.com.cn/'
resp = requests.get(url)
resp.encoding = 'utf-8'


main_page = BeautifulSoup(resp.text, "html.parser")
divs = main_page.find('ul', class_="list-a news_top").find_all('a')

titles = []

j = 0
for i in divs:
    j += 1
    title = str(j) + '.' + i.get_text()
    href = i.get('href')
    titles.append(title)

print(titles)




# 要发送的消息内容
payload = {
    "msgtype": "text",
    "text": {
        "content": f"{titles}"
    }
}

# 企业微信机器人 Webhook 地址
webhook_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=ec1c2a9d-ff57-4290-afef-1415c43cfea5"
# 发送 POST 请求
response = requests.post(
    url=webhook_url,
    headers={"Content-Type": "application/json"},
    data=json.dumps(payload)
)

# 打印返回结果
print("发送状态:", response.status_code)
print("响应内容:", response.text)
