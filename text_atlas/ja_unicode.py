# ひらがなをユニコードの値から列挙
for c in range(0x3041, 0x3096):
    print(chr(c))

# カタカナ
for c in range(0x30A1, 0x30FA):
    # Unicode数値を文字列に変換
    print(chr(c))
