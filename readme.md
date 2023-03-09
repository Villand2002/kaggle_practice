## kaggle_note
ここでは、kaggleのための機械学習などを通じて得た知見をまとめていく。

### カテゴリ変数の処理
カテゴリ変数とは,数値以外の型を持つデータである。一般的にはone-hot-encodingなどを用いて数値データとして利用できるようにする。
***
```python
import sklearn.preprocessing as sp
```
***
このライブラリでone-hot-encodingが可能である.

### 欠損値の処理について