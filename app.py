from flask import Flask, render_template, request
import requests
import json
from collections import defaultdict, Counter

app = Flask(__name__)

# 设置 Token 值

TOKEN = ""

# 设置 Cookie
cookies = {
    "GZCTF_Token": TOKEN,
}

@app.route('/')
def index():
    # 发送请求
    #设置请求地址url
    base_url = ""  #设置为实际的 域名或IP URL https://xxxx.top

    path = "/api/game/2/details"
    url = base_url + path
    response = requests.get(url, cookies=cookies)

    # 处理响应
    if response.status_code == 200:
        data = response.json()  # 将响应内容解析为JSON

        # 提取题目信息和已解决次数
        challenges = data.get('challenges', {})
        challenge_counts = defaultdict(lambda: {'solved': 0, 'count': 0, 'tags': ''})
        tag_counts = Counter()
        total_count = 0
        labels = []
        dataset_data = []
        blood_names = {}  # 创建一个新的字典来存储一血名称

        for category, category_challenges in challenges.items():
            for challenge in category_challenges:
                title = challenge.get('title')
                solved = challenge.get('solved', 0)
                tags = challenge.get('tag')

                labels.append(title)
                dataset_data.append(solved)

                challenge_counts[title]['solved'] += solved
                challenge_counts[title]['count'] += 1
                challenge_counts[title]['tags'] = tags

                tag_counts[tags] += 1
                total_count += 1

                bloods = challenge.get('bloods', [])
                for blood in bloods:
                    blood_name = blood.get('name')
                    if title in blood_names:
                        blood_names[title].append(blood_name)  # 将一血名称添加到对应的题目标题的列表中
                    else:
                        blood_names[title] = [blood_name]  # 创建新的一血名称列表，并将一血名称添加到其中

        # 按照已解决次数进行排序
        sorted_challenges = sorted(challenge_counts.items(), key=lambda x: x[1]['solved'], reverse=True)
        return render_template('index.html', challenges=sorted_challenges, tag_counts=tag_counts, total_count=total_count, blood_names=blood_names, labels=json.dumps(labels), dataset_data=json.dumps(dataset_data))    
    return "请求失败"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)