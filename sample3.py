#coding:utf-8
from janome.tokenizer import Tokenizer
def kaiseki(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    for token in tokens:
        print token
if __name__=="__main__":
    text=u"今日の天気を教えてください"
    kaiseki(text)