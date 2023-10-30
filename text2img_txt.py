from PIL import Image, ImageDraw, ImageFont
import random
import string
import sys

# 获取传递的参数
color = sys.argv[1] # 第一个参数
txt =  sys.argv[2] # 第二个参数

def generate_imgname(length):
    # 从所有大小写字母和数字中生成随机字符串
    characters = string.ascii_letters + string.digits
    imgname = ''.join(random.choice(characters) for _ in range(length))
    return imgname

# 生成长度为12的随机字符串
imgname = generate_imgname(12)

def generate_image(text):
    # 设置字体样式和大小
    font = ImageFont.truetype("字体文件！！！", 50)
    
    # 将文本按照 "-" 进行分割
    lines = text.split('-')
    
    # 计算每一行的文本尺寸
    line_sizes = [font.getsize(line) for line in lines]
    
    # 计算图片的宽度和高度
    img_width = max(line_size[0] for line_size in line_sizes) + 100
    img_height = sum(line_size[1] for line_size in line_sizes) + 50 * (len(lines) + 1)
    
    # 创建一个空白图片
    image = Image.new("RGB", (img_width, img_height), "white")
    
    # 创建一个可绘制对象
    draw = ImageDraw.Draw(image)
    
    # 在图片上逐行绘制文本
    y_text = 50
    for i, line in enumerate(lines):
        draw.text((50, y_text), line, fill=color, font=font)
        y_text += line_sizes[i][1] + 50
    
    # 保存图片
    image.save("地址！！！" + imgname + ".png", format="PNG")

# 调用函数生成图片
generate_image(txt)

# 生成图片的路径
print("https://你的输出地址" + imgname + ".png")
