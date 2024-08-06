
工具termux




要实现每次保存的图片名称递增1，
可以在代码中使用一个文件来记录上一次保存的编号，

并在每次运行时读取、更新并保存该编号。

下面是修改后的代码示例：

import openai
import requests
import os

# 设置你的API密钥
openai.api_key = "api密钥"

# 获取用户输入的描述
user_input = input("请输入你想生成的图像描述：")

# 生成图像
response = openai.Image.create(
    prompt=user_input,
    n=1,  # 创建图像的数量
    size="1024x1024"  # 图像的大小
)

# 获取生成的图像URL
image_url = response['data'][0]['url']

# 下载图像并保存到本地
image_data = requests.get(image_url).content

# 读取上一次的编号
counter_file = 'counter.txt'
if os.path.exists(counter_file):
    with open(counter_file, 'r') as file:
        counter = int(file.read().strip())
else:
    counter = 0

# 增加编号
counter += 1

# 保存图像并在文件名中包含递增的编号
file_name = f'generated_image_{counter}.png'
with open(file_name, 'wb') as handler:
    handler.write(image_data)

# 更新编号
with open(counter_file, 'w') as file:
    file.write(str(counter))

print(f"图像已保存为 {file_name}")

在这段代码中，counter.txt 

文件用于存储上一次的编号。每次运行代码时，

它会读取该文件中的编号，递增1，

并将更新后的编号写回文件中，以便下次使用。

这样生成的图像文件名会每次递增1










