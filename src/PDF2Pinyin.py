import os
import re
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from xpinyin import Pinyin


def extractChinese(pdfPath):
    # 提取PDF中汉字
    output_string = StringIO()
    with open(pdfPath, 'rb') as in_file:
        # 创建一个PDF文档解析器对象
        parser = PDFParser(in_file)
        # 创建一个PDF文档对象存储文档结构
        # 提供密码初始化，没有就不用传该参数
        doc = PDFDocument(parser)
        # 创建一个PDF资源管理器对象来存储共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个pdf设备对象
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        # 创建一个PDF解析器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # 处理文档当中的每个页面
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    # print(output_string.getvalue())

    # 匹配所有unicode中文
    lines = str(output_string.getvalue())
    chinese = ''.join(re.findall('[\u4e00-\u9fa5]', lines))
    return chinese

    # print(chinese)


def ChineseToPinyin(chinese, sampleName):
    # 汉字转拼音
    pinyin = ' ' + Pinyin().get_pinyin(chinese, ' ') + ' '

    # 汉字转拼音首字母大写
    pinyin_list = Pinyin().get_pinyin(chinese).split('-')
    pinyin_initials = ''
    for i in range(0, len(pinyin_list)):
        pinyin_initials = pinyin_initials + pinyin_list[i].capitalize()
    
    return (pinyin, pinyin_initials)