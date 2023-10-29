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
    # 创建一个空白图片
    image = Image.new("RGB", (500, 200), "white")
    
    # 创建一个可绘制对象
    draw = ImageDraw.Draw(image)
    
    # 设置字体样式和大小
    font = ImageFont.truetype("SmileySans-Oblique.ttf", 50)
    
    # 在图片上绘制文本
    draw.text((50, 50), text, fill=color, font=font)
    
    # 保存图片
    image.save("output/" + imgname + ".png", format="PNG")
    
# 调用函数生成图片
generate_image(txt)

# 生成图片的路径（可用于服务器）
print("output/" + imgname + ".png")