import os
import re
import math

from PDF2Pinyin import extractChinese, ChineseToPinyin
from evaluation import evaluation
from improvedSolution import solution1, solution2, solution3, solution4


def main():
    sampleName = 'sample1'
    keyboardHeatMapPath = '../output/' + sampleName + '_keyboardHeatMap.png'
    keyboardHeatMapPath_improved = '../output/' + sampleName + '_keyboardHeatMap_improved.png'
    keyboardHeatMapPath_final = '../output/' + sampleName + '_keyboardHeatMap_final.png'
    samplePath = os.path.join('../samples/', sampleName + '.pdf')

    chinese = extractChinese(samplePath)
    (pinyin_org, pinyin_initials_org) = ChineseToPinyin(chinese, sampleName)

    # 绘制键盘热力图
    pinyin = ''.join(re.findall('[a-z]', pinyin_org))
    pinyinPath = os.path.join('../output/', sampleName + '_pinyin.txt')
    with open(pinyinPath, 'w') as f:
        f.write(pinyin)
    cmd = 'tapmap' + ' ' + '../output/' + sampleName + '_pinyin.txt' + ' ' + keyboardHeatMapPath + ' -c coolwarm'
    res = os.popen(cmd).readlines()
    print(res)

    # 评价均衡性和输入效率
    print("\n\n")
    print("Original pinyin decode")
    evaluation(chinese, pinyin)


    # 全拼方案改进
    print("\n\n")
    print("Recode based on Quanpin")
    recodeQuanpin_org = solution1(pinyin_org)
    recodeQuanpin = ''.join(re.findall('[a-z]', recodeQuanpin_org))
    evaluation(chinese, recodeQuanpin)

    recodeQuanpinPath = '../output/' + sampleName + '_recodeQuanpin.txt'
    with open(recodeQuanpinPath, 'w') as f:
        f.write(recodeQuanpin)

    # 绘制改进后的键盘热力图
    cmd = 'tapmap' + ' ' + '../output/' + sampleName + '_recodeQuanpin.txt' + ' ' + keyboardHeatMapPath_improved + ' -c coolwarm'
    res = os.popen(cmd).readlines()
    print(res)
    print("\n\n")

    
    # 双拼方案改进
    print("\n\n")
    print("Recode based on Shuangpin")
    recodeShuangpin_org = solution2(recodeQuanpin_org)
    recodeShuangpin = ''.join(re.findall('[a-z]', recodeShuangpin_org))
    evaluation(chinese, recodeShuangpin)

    recodeShuangpinPath = '../output/' + sampleName + '_recodeShuangpin.txt'
    with open(recodeShuangpinPath, 'w') as f:
        f.write(recodeShuangpin)
    print("\n\n")

    # 绘制改进后的键盘热力图
    cmd = 'tapmap' + ' ' + '../output/' + sampleName + '_recodeShuangpin.txt' + ' ' + keyboardHeatMapPath_final + ' -c coolwarm'
    res = os.popen(cmd).readlines()
    print(res)

    print("\n\n")
    print("Recode based on ZiguangShuangpin")
    recodeZiguangShuangpin_org = solution3(recodeQuanpin_org)
    recodeZiguangShuangpin = ''.join(re.findall('[a-z]', recodeZiguangShuangpin_org))
    evaluation(chinese, recodeZiguangShuangpin)
    print("\n\n")

    print("\n\n")
    print("Recode based on SougouShuangpin")
    recodeSougouShuangpin_org = solution4(recodeQuanpin_org)
    recodeSougouShuangpin = ''.join(re.findall('[a-z]', recodeSougouShuangpin_org))
    evaluation(chinese, recodeSougouShuangpin)


if __name__ == '__main__':
    main()