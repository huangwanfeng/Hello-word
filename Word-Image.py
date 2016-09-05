# -*- coding: utf-8 -*-
from docx import Document
from PIL import Image, ImageDraw
from io import BytesIO

document = Document()
p = document.add_paragraph()
r = p.add_run()
img_size = 20
for x in range(255):
    im = Image.new("RGB", (img_size,img_size),"white") #图形颜色模式、尺寸、填充色

