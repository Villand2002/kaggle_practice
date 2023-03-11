# 便利であると思ったpythonの構文などをまとめる.

## 内包表記

num=[1,2,3]
dict={key:key*2 for key in num}
print(dict)
print("\n")
# 結果:{1: 2, 2: 4, 3: 6}


index=["a","b","c"]
values=[1,2,3]
dict2={key:value for key,value in zip(index,values)}

#zip関数で複数のfor文を並列実行する.
print(dict2)
print("\n")


## 多変数の関数

def func(num,*args):
    print(f"入力numの部分は,{num}である\n")
    print(f"入力*argsの部分は,{args}である")
    
func(1,2,3,4,5)    


# 結果:入力numの部分は,1である
#  入力*argsの部分は,(2, 3, 4, 5)である
    
#このようにすることで,変数の数を限定しなくてもよくなる.print関数などで使う際には*を外す必要がある. 
    
## 型限定
# c言語のように関数に入れる型を限定することができる.


def test(num:int, alox:list):
    list2=[]
    # k=len(alox)
    for i in range(len(alox)):
        list2.append(num*alox[i])
    print(list2)    
        
test(2,[1,2,3,4,5])        

## enumerateについて


# 要素と添え字を同時に取り出したくなった時に用いられる.


list = ['a', 'b', 'c']

for i, v in enumerate(list):
    print(i, v)
    
#結果    
# 0 a
# 1 b
# 2 c    

# one-hot-encodingなどで使われることがある.

## 高階関数

### map関数    
# 
# 第一引数に関数、第二引数にシーケンスを指定する.加工元となるを第リストなどを第二引数に指定し、それをどのように加工するのかというところが第一引数によって指定する.

sample1_list = [i for i in range(5)]
def multi(x):
    y = x*2
    return y
sample2_list = map(multi, sample1_list)
print((sample2_list))
#[0, 2, 4, 6, 8]



### filter関数    
# filter関数はリストやタプルの要素のうち関数を適用した結果が True となるものだけを返す関数である.


a = [-1, 3, -5, 7, -9]


(x for x in a if abs(x) > 5)  # => 上記 filter と同じ結果


### reduce関数    

#  reduce関数はリストやタプルの要素を足しあわせたりかけあわせたりする関数である.

import functools
from functools import reduce

lst=[1,2,3,4,5]
print(functools.reduce(lambda a,b:a+str(b),lst,""))
# 1234
