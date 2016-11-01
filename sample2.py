#coding:utf-8
import pandas
open_data='http://city.yokohama.lg.jp/ex/stat/opendata/suikei01/e1yokohama1412.csv'
df=pandas.read_csv(open_data,index_col='市区名')
print(df.head(3))