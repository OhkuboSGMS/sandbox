def main():
    # ひらがなをユニコードの値から列挙
    for c in range(0x3041, 0x3096):
        print(chr(c))

    # カタカナ
    for c in range(0x30A1, 0x30FA):
        # Unicode数値を文字列に変換
        print(chr(c))

    # CJK
    for c in range(0x4E00,0x9FFF):
        print(chr(c))


def cjk():
    for c in range(0x4E00,0x9FFF):
        yield chr(c)