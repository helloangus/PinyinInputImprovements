import math


def evaluation(chinese, pinyin):

    # 统计所有字母出现次数
    stat = {}
    for i in range(ord('a'), ord('z') + 1):
        stat[chr(i)] = pinyin.count(chr(i))
    print(stat)

    # 将所有键位分成三排
    # 定义键位修正参数
    k1 = 1.0
    k2 = 0.9
    k3 = 1.1
    k_i = {'q': k1, 'w': k1, 'e': k1, 'r': k1, 't': k1, 'y': k1, 'u': k1, 'i': k1, 'o': k1, 'p': k1,
            'a': k2, 's': k2, 'd': k2, 'f': k2, 'g': k2, 'h': k2, 'j': k2, 'k': k2, 'l': k2, 
            'z': k3, 'x': k3, 'c': k3, 'v': k3, 'b': k3, 'n': k3, 'm': k3
    }

    firstRowKey = {}
    for i in range(ord('a'), ord('z')+1):
        if k_i[chr(i)] == k1:
            firstRowKey[chr(i)] = stat[chr(i)]
    secondRowKey = {}
    for i in range(ord('a'), ord('z')+1):
        if k_i[chr(i)] == k2:
            secondRowKey[chr(i)] = stat[chr(i)]
    thirdRowKey = {}
    for i in range(ord('a'), ord('z')+1):
        if k_i[chr(i)] == k3:
            thirdRowKey[chr(i)] = stat[chr(i)]


    # 计算输入效率
    # 平均单字击键数
    numOfLetter_ch = len(chinese)
    numOfLetter_py = len(pinyin)
    N_avg = numOfLetter_py / numOfLetter_ch
    print('Number of Chinese characters: %d' % numOfLetter_ch)
    print('Number of English letters: %d' % numOfLetter_py)
    print('Average number of single word keystrokes: %.4f' % N_avg)

    # 平均单字耗时
    t0 = 0.8

    sum_first = 0
    for i in firstRowKey:
        sum_first += firstRowKey[i]
    sum_second = 0
    for i in secondRowKey:
        sum_second += secondRowKey[i]
    sum_third = 0
    for i in thirdRowKey:
        sum_third += thirdRowKey[i]
    sum_hit = sum_first * k1 + sum_second * k2 + sum_third * k3
    t_total = sum_hit * t0
    T_avg = t_total / numOfLetter_ch
    print('Average typing time of single word: %.4f' % T_avg)


    # 计算均衡性
    pFirst_avg = sum_first / len(firstRowKey)
    stdFirst = 0
    for i in firstRowKey:
        stdFirst += math.pow((firstRowKey[i] / pFirst_avg - 1), 2)
    stdFirst = math.sqrt(stdFirst / (len(firstRowKey) - 1))

    pSecond_avg = sum_second / len(secondRowKey)
    stdSecond = 0
    for i in secondRowKey:
        stdSecond += math.pow((secondRowKey[i] / pSecond_avg - 1), 2)
    stdSecond = math.sqrt(stdSecond / (len(secondRowKey) - 1))

    pThird_avg = sum_third / len(thirdRowKey)
    stdThird = 0
    for i in thirdRowKey:
        stdThird += math.pow((thirdRowKey[i] / pThird_avg - 1), 2)
    stdThird = math.sqrt(stdThird / (len(thirdRowKey) - 1))

    B = stdFirst + stdSecond + stdThird
    print('Balance: %0.4f' % B)