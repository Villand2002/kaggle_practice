## pythonの構文などをまとめる.

#内包文
num=[1,2,3]
dict={key:key*2 for key in num}
print(dict)
#結果:{1: 2, 2: 4, 3: 6}

index=["a","b","c"]
values=[1,2,3]
dict2={key:value for key,value in zip(index,values)}

#zip関数で複数のfor文を並列実行する.
print(dict2)


# 変数多数
def func(num,*args):
    print(num)
    print(*args)
    
#このようにすることで   変数の数を限定しなくてもよくなる. 
    
#組み込み関数
#map関数    