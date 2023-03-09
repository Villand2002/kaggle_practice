## pythonの構文などをまとめる.

#内包文
num=[1,2,3]
dict={key:key*2 for key in num}
print(dict)
print("\n")
#結果:{1: 2, 2: 4, 3: 6}

index=["a","b","c"]
values=[1,2,3]
dict2={key:value for key,value in zip(index,values)}

#zip関数で複数のfor文を並列実行する.
print(dict2)
print("\n")


# 変数多数
def func(num,*args):
    print(f"入力numの部分は,{num}である\n")
    print(f"入力*argsの部分は,{args}である")
    
func(1,2,3,4,5)    
#結果->入力numの部分は,1である
#      入力*argsの部分は,(2, 3, 4, 5)である
    
#このようにすることで,変数の数を限定しなくてもよくなる.print関数などで使う際には*を外す必要がある. 
    
#組み込み関数
#map関数    