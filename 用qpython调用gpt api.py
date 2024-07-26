必须开启vpn，才能通过requests来调用openai  gpt  api

用qpython自带的编辑器，编辑代码保存运行即可,


把写好的代码粘贴到qpython自带的编辑器里，点运行按钮
运行即可，运行时需要填写一个文件名称.py

随便起一个名字保存运行即可看到运行效果，


如果你希望通过 requests 模块来调用 OpenAI 的 GPT API，并且在你的 Python 脚本中实现一个聊天机器人，你可以参考以下示例代码：botappo.py 示例代码import requests

# 设置 API 密钥和端点
api_key = 'your_openai_api_key'//这里改成自己的gpt api
api_url = 'https://api.openai.com/v1/chat/completions'

# 聊天函数
def chat_with_gpt(prompt):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'gpt-4',  # 使用 gpt-4 模型
        'messages': [
            {'role': 'user', 'content': prompt}
        ]
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        return reply
    else:
        return f'Error: {response.status_code} - {response.text}'

# 主对话循环
def main():
    print("你好！我可以帮你聊天，输入 '退出' 来结束对话。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == '退出':
            print("再见！")
            break
        reply = chat_with_gpt(user_input)
        print(f"机器人: {reply}")

if __name__ == '__main__':
    main()关键点安装 requests 模块： 确保你已经在 QPython 中安装了 requests 模块。如果没有，你可以尝试手动下载并安装它，或者用 QPython 提供的其他方法安装。API 密钥： 替换 'your_openai_api_key' 为你实际的 OpenAI API 密钥。运行脚本： 在 QPython 中运行脚本，输入消息与机器人对话，输入 '退出' 结束对话。如果你在执行过程中遇到任何问题，提供具体的错误信息将有助于进一步诊断和解决问题。
