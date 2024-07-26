使用环境变量来存储敏感信息如 API 密钥是一种安全的做法。以下是如何在你的 Flask 应用中使用环境变量来存储和访问 OpenAI API 密钥的步骤：1. 设置环境变量在你的系统中设置环境变量。不同的操作系统和终端设置环境变量的方式可能有所不同。以下是一些常见的方法：在 Linux 或 macOS 中：打开终端。使用 export 命令设置环境变量。例如：export OPENAI_API_KEY='your_openai_api_key'为了确保每次启动终端时环境变量都被设置，可以将上面的 export 命令添加到你的 ~/.bashrc、~/.zshrc 或其他配置文件中。在 Windows 中：打开“系统属性”对话框（可以通过搜索“环境变量”找到）。在“环境变量”对话框中，点击“新建”按钮，添加一个新的系统变量或用户变量：变量名：OPENAI_API_KEY变量值：your_openai_api_key2. 修改 Flask 应用以使用环境变量在你的 app.py 文件中，修改代码以从环境变量中读取 API 密钥。可以使用 os 模块来访问环境变量：from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__)

# 从环境变量中读取 OpenAI API 密钥
API_KEY = os.getenv('OPENAI_API_KEY')
API_URL = 'https://api.openai.com/v1/chat/completions'

def get_gpt_response(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-4',  # 或者 'gpt-3.5-turbo'，根据你使用的模型
        'messages': [
            {'role': 'user', 'content': prompt}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['message']['content'].strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']
    response = get_gpt_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)3. 运行 Flask 应用在设置好环境变量后，运行 Flask 应用：python app.py验证访问 http://127.0.0.1:5000 并确保一切正常。如果环境变量没有设置或不正确，Flask 应用可能会报错，提示找不到 API 密钥。确保环境变量在你的运行环境中已正确设置并可用。这样，你就可以安全地管理你的 API 密钥，而不需要将其硬编码到你的代码中。
