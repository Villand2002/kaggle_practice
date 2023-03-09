## 便利であると思ったpythonの構文などをまとめる.

### 内包表記

例1
***
```python
num=[1,2,3]
dict={key:key*2 for key in num}
print(dict)
print("\n")
```
***

結果:{1: 2, 2: 4, 3: 6}
例2
***
```python
index=["a","b","c"]
values=[1,2,3]
dict2={key:value for key,value in zip(index,values)}

#zip関数で複数のfor文を並列実行する.
print(dict2)
print("\n")
```
***


### 変数多数の関数

例
***
```python
def func(num,*args):
    print(f"入力numの部分は,{num}である\n")
    print(f"入力*argsの部分は,{args}である")
    
func(1,2,3,4,5)    
```
***

結果:入力numの部分は,1である
     入力*argsの部分は,(2, 3, 4, 5)である
    
#このようにすることで,変数の数を限定しなくてもよくなる.print関数などで使う際には*を外す必要がある. 
    
### 型限定
c言語のように関数に入れる型を限定することができる.

例
***
```python
def test(num:int, alox:list):
    list2=[]
    # k=len(alox)
    for i in range(len(alox)):
        list2.append(num*alox[i])
    print(list2)    
        
test(2,[1,2,3,4,5])        
```
***

### enumerateについて


要素と添え字を同時に取り出したくなった時に用いられる.

例
***
```python
list = ['a', 'b', 'c']

for i, v in enumerate(list):
    print(i, v)
    
#結果    
# 0 a
# 1 b
# 2 c    
```
***

one-hot-encodingなどで使われることがある.

#組み込み関数
#map関数    

例