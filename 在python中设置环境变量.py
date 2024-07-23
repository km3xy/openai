openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ]
)

print(response.choices[0].message['content'])运行脚本在 QPython 中运行你



的脚本，可以看到模型的回复。总结通过这种方法，你可以在 QPython 中设置环境变量并调用 OpenAI API。如果你有更多需要定制的环境变量，建议使用 .env 文件并通过 python-dotenv 来管理。这样可以使你的代码更加灵活和易于维护。





在qpython中安装openai   容易报错




选用aidlux来替代qpython


