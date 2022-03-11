# 零声母替换字典
zeroVowels_dict = {
    "a": "aa",
    "e": "ee",
    "o": "oo",

    "ai": "ai",
    "an": "an",
    "ao": "ao",

    "ou": "ou",
    
    "ei": "ei",
    "en": "en",
    "er": "er",

    "ang": "ah",        
    "eng": "eg"
}

# 声母只修改翘舌音
voewls_dict = {
    "sh": "u",
    "ch": "i",
    "zh": "v"
}

# 介母韵母替换数据字典
finals_dict = {
    "iu": "q",
    "ei": "w",
    "uan": "r",
    "ue": "t",
    "ve": "t",
    "un": "y",
    "uo": "o",
    "ie": "p",

    "ong": "s",
    "iong": "s",
    "ai": "d",
    "en": "f",
    "eng": "g",
    "ang": "h",
    "an": "j",
    "uai": "k",
    "ing": "k",
    "uang": "l",
    "iang": "l",

    "ou": "z",
    "ua": "x",
    "ia": "x",
    "ao": "c",
    "ui": "v",
    "v": "v",
    "in": "b",
    "iao": "n",
    "ian": "m"
}



def solution1(pinyin_org):
    personal_dict = {
        "gong chan": "g c",
        "zhu yi": "z y",
        "jie ji": "j j",
        "she hui": "s h",
        "zi chan": "z c",
        "wu chan": "w c",
        "zi ben": "z b",
        "gong ren": "g r",
        "ge ming": "g m",
        "lao dong": "l d"
    }

    res = pinyin_org
    # 采用个人词库替换
    for key, value in personal_dict.items():
        res = res.replace(key, value)
    
    return res


def solution2(pinyin_org):
    res = pinyin_org
    # 替换零声母音节
    for key, value in zeroVowels_dict.items():
        res = res.replace(' ' + key + ' ', ' ' + value + ' ')
        print('Replace ' + key + ' to ' + value)
    
    # 替换声母
    for key, value in voewls_dict.items():
        res = res.replace(' ' + key, ' ' + value)
        print('Replace ' + key + ' to ' + value)

    # 替换介母韵母
    # 需要从长往短替换，防止错误
    for key, value in finals_dict.items():
        if len(key) == 4:
            res = res.replace(key + ' ', value + ' ')
            print('Replace ' + key + ' to ' + value)
    for key, value in finals_dict.items():
        if len(key) == 3:
            res = res.replace(key + ' ', value + ' ')
            print('Replace ' + key + ' to ' + value)
    for key, value in finals_dict.items():
        if len(key) == 2:
            res = res.replace(key + ' ', value + ' ')
            print('Replace ' + key + ' to ' + value)
    for key, value in finals_dict.items():
        if len(key) == 1:
            res = res.replace(key + ' ', value + ' ')
            print('Replace ' + key + ' to ' + value)

    return res



# 紫光双拼方案
# 零声母替换字典，相当于o+韵母所在按键
ziguang_zeroVowels_dict = {
    "a": "oa",
    "e": "oe",
    "o": "oo",

    "ai": "op",
    "an": "or",
    "ao": "oq",

    "ou": "oz",
    
    "ei": "ok",
    "en": "ow",
    "er": "oj",

    "ang": "os",        
    "eng": "ot"
}

# 声母只修改翘舌音
ziguang_voewls_dict = {
    "sh": "l",
    "ch": "a",
    "zh": "u"
}

# 介母韵母替换数据字典
ziguang_finals_dict = {
    "iu": "j",
    "ei": "k",
    "uan": "l",
    "ue": "n",
    "ve": "n",
    "un": "m",
    "uo": "o",
    "ie": "d",

    "ong": "h",
    "iong": "h",
    "ai": "p",
    "en": "w",
    "eng": "t",
    "ang": "s",
    "an": "r",
    "uai": "y",
    "ing": " ",
    "uang": "g",
    "iang": "g",

    "ou": "z",
    "ua": "x",
    "ia": "x",
    "ao": "q",
    "ui": "n",
    "v": "v",
    "in": "y",
    "iao": "b",
    "ian": "f"
}



def solution3(pinyin_org):
    res = pinyin_org
    # 替换零声母音节
    for key, value in ziguang_zeroVowels_dict.items():
        res = res.replace(' ' + key + ' ', ' ' + value + ' ')
        # print('Replace ' + key + ' to ' + value)
    
    # 替换声母
    for key, value in ziguang_voewls_dict.items():
        res = res.replace(' ' + key, ' ' + value)
        # print('Replace ' + key + ' to ' + value)

    # 替换介母韵母
    # 需要从长往短替换，防止错误
    for key, value in ziguang_finals_dict.items():
        if len(key) == 4:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)
    for key, value in ziguang_finals_dict.items():
        if len(key) == 3:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)
    for key, value in ziguang_finals_dict.items():
        if len(key) == 2:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)
    for key, value in ziguang_finals_dict.items():
        if len(key) == 1:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)

    return res


# 搜狗双拼方案
# 零声母替换字典，相当于o+韵母所在按键
sougou_zeroVowels_dict = {
    "a": "oa",
    "e": "oe",
    "o": "oo",

    "ai": "op",
    "an": "or",
    "ao": "oq",

    "ou": "oz",
    
    "ei": "ok",
    "en": "ow",
    "er": "oj",

    "ang": "os",        
    "eng": "ot"
}

# 声母只修改翘舌音
sougou_voewls_dict = {
    "sh": "u",
    "ch": "l",
    "zh": "v"
}

# 介母韵母替换数据字典
sougou_finals_dict = {
    "iu": "q",
    "ei": "z",
    "uan": "r",
    "ue": "t",
    "ve": "t",
    "un": "p",
    "uo": "o",
    "ie": "x",

    "ong": "s",
    "iong": "s",
    "ai": "l",
    "en": "f",
    "eng": "g",
    "ang": "h",
    "an": "j",
    "uai": "y",
    "ing": " ",
    "uang": "d",
    "iang": "d",

    "ou": "b",
    "ua": "w",
    "ia": "w",
    "ao": "k",
    "ui": "v",
    "v": "y",
    "in": "n",
    "iao": "c",
    "ian": "m"
}



def solution4(pinyin_org):
    res = pinyin_org
    # 替换零声母音节
    for key, value in sougou_zeroVowels_dict.items():
        res = res.replace(' ' + key + ' ', ' ' + value + ' ')
        # print('Replace ' + key + ' to ' + value)
    
    # 替换声母
    for key, value in sougou_voewls_dict.items():
        res = res.replace(' ' + key, ' ' + value)
        # print('Replace ' + key + ' to ' + value)

    # 替换介母韵母
    # 需要从长往短替换，防止错误
    for key, value in sougou_finals_dict.items():
        if len(key) == 4:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)
    for key, value in sougou_finals_dict.items():
        if len(key) == 3:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)
    for key, value in sougou_finals_dict.items():
        if len(key) == 2:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)
    for key, value in sougou_finals_dict.items():
        if len(key) == 1:
            res = res.replace(key + ' ', value + ' ')
            # print('Replace ' + key + ' to ' + value)

    return res