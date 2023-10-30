# text2img_txt 把自定义的文本生成图文
把自定义的文本生成图片文字

# 注意
下载一个ttf字体文件放到目录

参数默认为color（颜色）和txt（内容）

访问为php文件?参数访问（color必须在前，txt在后）

需要服务器拥有python及其pil拓展

文本用-进行换行

# 不需要访问
可以删除一下代码之后就可以直接本地py +文件调用
<pre><code>
import sys
# 获取传递的参数
color = sys.argv[1] # 第一个参数
txt =  sys.argv[2] # 第二个参数
</code></pre>

注意color和txt参数
