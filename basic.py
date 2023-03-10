from sklearn.linear_model import LinearRegression
#sklearnを利用する.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
housing=fetch_california_housing()


df=pd.DataFrame(housing.data)
#dfに置換する.

df.columns=housing.feature_names

#カラムを変更

print(df.columns)

# インスタンスを用意する.
model=LinearRegression()
#線形回帰モデルの作成.

#1次元配列をreshape(-1, 1)とすると、その配列を要素とする2次元1列の配列となる。


#1次元配列をreshape(1, -1)とすると、その配列を要素とする2次元1行の配列になる。
