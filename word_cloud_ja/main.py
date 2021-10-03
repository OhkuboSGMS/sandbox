# coding:utf-8
from janome.tokenizer import Tokenizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter, defaultdict


# 名詞だけ抽出、単語をカウント
def counter(texts):
    t = Tokenizer()
    words_count = defaultdict(int)
    words = []
    for text in texts:
        tokens = t.tokenize(text)
        for token in tokens:
            # 品詞から名詞だけ抽出
            pos = token.part_of_speech.split(',')[0]
            # if pos in ['名詞']:
            #     必要ない単語を省く(実際の結果を見てから不必要そうな単語を記載しました)
                # if token.base_form not in ["こと", "よう", "そう", "これ", "それ"]:
            words_count[token.base_form] += 1
            words.append(token.base_form)
    return words_count, words


with open('phrase.txt', encoding='UTF-8') as f:
    texts = f.readlines()
    texts = list(map(lambda x:x.strip(),texts))

print(texts)
# words_count, words = counter(texts)
text = ' '.join(texts)
print(text)
# fontは自分の端末にあるものを使用する
fpath = "KleeOne-Regular.ttf"
wordcloud = WordCloud(background_color="black",
                      font_path=fpath, width=1024, height=500).generate(text)

wordcloud.to_file("./wordcloud_sample.png")
