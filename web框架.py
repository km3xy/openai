HTML 不能像嵌入 PHP 代码那样直接嵌入 Python 代码。

但是，你可以使用一个 Web 框架（例如 Flask 或 Django）来实现相似的效果。

通过 Flask 框架，你可以在 HTML 文件中使用 Jinja2 模板引擎来嵌入 Python 代码。以下是一个简单的示例，展示了如何使用 Flask 和 Jinja2 模板来实现这一点。

安装 Flask确保你的 QPython 环境已经安装 Flask。你可以尝试之前的方法安装 Flask。创建 Flask 应用创建一个 Python 文件 app.py：from flask import Flask, render_template, request

import os
import requests

app = Flask(__name__)

API_KEY = os.getenv('OPENAI_API_KEY')
API_URL = 'https://api.openai.com/v1/chat/completions'

def get_gpt_response(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': prompt}]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['message']['content'].strip()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = get_gpt_response(user_input)
        return render_template('index.html', response=response)
    return render_template('index.html', response=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)创建一个模板文件 templates/index.html：<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat with GPT</title>
</head>
<body>
    <h1>Chat with GPT</h1>
    <form method="POST">
        <label for="user_input">Enter your message:</label>
        <input type="text" id="user_input" name="user_input">
        <button type="submit">Submit</button>
    </form>
    {% if response %}
    <h2>Response:</h2>
    <p>{{ response }}</p>
    {% endif %}
</body>
</html>运行 Flask 应用在你的 QPython 环境中运行 app.py：/data/user/0/org.qpython.qpy/files/bin/qpython3.sh "/storage/emulated/0/Android/data/org.qpython.qpy/files/app.py" && exit访问 http://<你的Android设备IP>:5000/ 即可看到你的应用界面，输入消息后可以得到 GPT 的回复。这种方式利用了 Flask 和 Jinja2 模板引擎，实现了类似 PHP 嵌入 HTML 的效果，但实际上是通过服务器端渲染实现的。
