# ๐ป์คํฐ๋ ์ฌํญ 

## ๐๐ปโโ๏ธ ์๊ณ ๋ฆฌ์ฆ ๊ธฐ์ด 

### 1. ์๊ณ ๋ฆฌ์ฆ๊ณผ ์์ถ๋ ฅ 

#### [2442](https://www.acmicpc.net/problem/2442)

#### [2443](https://www.acmicpc.net/problem/2443)

### 2. ์๋ฃ๊ตฌ์กฐ 1 

#### 10828 

- ์์ธ : ์๊ฐ์ด๊ณผ 

- ํด๊ฒฐ 

  - `input()` ๋์  `sys.stdin.readline()` 

  - for ๋ฌธ์ ์๋ ์กฐ๊ฑด๋ฌธ๋ค์ ๋ชจ๋ ํจ์๋ก ์ ์ํด์ ์ฌ์ฉ 

    

#### 10799

- ์๊ฑฐ๋ ๊ทธ๋ฆผ ๊ทธ๋ฆฌ๋ฉด์ ๋ค์ ๊ณต๋ถํด์ผ ํ  ๋ฏ 



#### 1406

- ์์ธ : ์๊ฐ์ด๊ณผ 

- ํด๊ฒฐ 

  - for ๋ฌธ์ ์๋ ์กฐ๊ฑด๋ฌธ๋ค์ ๋ชจ๋ ํจ์๋ก ์ ์ํด์ ์ฌ์ฉ 
  - ํจ์ ์ ์ ์, global ์ ์ธํด์ฃผ๊ณ  ๋ณ์๋ช ์ฌ์ฉํ๊ธฐ - ๊ทผ๋ฐ ์ 10828 ํ  ๋, stack ๋ฆฌ์คํธ๋ ์ ์ธํ์ง ์๊ณ ๋ ์ฌ์ฉ์ด ๊ฐ๋ฅํ๋๊ฐ? 
  - `input()` ๋์  `sys.stdin.readline()` 

  => ์ฌ๊ธฐ๊น์งํด๋ ์๊ฐ์ด๊ณผ๋ก ํ๋ฆผ 

  - stack 2๊ฐ๋ก ๋๋ ์ ์ ๊ทผ 
  - `insert`๋ณด๋ค `pop()`๊ณผ `append()`๋ฅผ ์ฌ์ฉํด์ ์ฐ๋ ๊ฒ์ด ๋ ์ข์ 
  - ํ์ง๋ง ์ฝ๋ ๊ตฌ์กฐ 99% ๋๊ฐ์๋ฐ ๋ง๊ณ  ํ๋ฆฌ๊ณ ๊ฐ ๊ฐ๋ฆผ ํ์ธ ํโผ
  - ์กฐ๊ฑด ์ค ๋, try๋ except๋ก ์ฝ๊ฒ ๊ฐ๋ ค๊ณ  ํ์ง๋ง๊ณ , ๊ผผ๊ผผํ๊ฒ ๋ค ์์ธ์ฒ๋ฆฌ ํด์ฃผ๊ธฐ!!! 



#### 10820 ๋ฌธ์์ด 

- ๋ด์ฅํจ์ : `isupper()` ๊ฐ์ ๊ฑฐ ์ฌ์ฉํ  ์๋ ์์ 









### 3. ๋ค์ด๋๋ฏน ํ๋ก๊ทธ๋๋ฐ 

### ๊ฐ๋ ์ดํด 

#### ์กฐ๊ฑด 

- ํ๋์ problem์ด ๋ ์์ subproblem์ผ๋ก ์ชผ๊ฐ์ง ๋
- subproblem๋ค์ ํด๊ฒฐ๋ก ๋ ํฐ subproblem์ ํด๊ฒฐํ  ์ ์์ ๋ 
- subproblem์ด ๊ฒน์น  ๋ 

**์์**

ํผ๋ณด๋์น ์์ด O(2^n)

Fn = Fn-1 + Fn-2 

 ```python
 def fib_naive(n) : 
     if n==0 : 
         return 1 
     elif n == 1 : 
         return 1 
     else : 
         fib = fib_naive(n-1) + fib_naive(n-2)
         return fib 
     
  # O(2^n) 
 %%timeit # ์๊ฐ ์ฌ๋ ๊ฒ 
 fib_naive(35)
 ```

- array์ ๋ด์์ ํด๊ฒฐํ๋ค 

  ```python
  fib_arry = [1,1]
  
  def fib_recur_dp(n) : 
      if n < len(fib_arry) : 
          return fib_arry[n]
      else : 
          fib = fib_recur_dp(n-1) + fib_recur_dp(n-2)
          fib_arry.append(fib)
          return fib
  ```

  => ํ์ง๋ง, ํฐ ์๋ฅผ ๋ฃ๊ฒ๋๋ฉด ๋ฐํ์ ์๋ฌ๊ฐ ๋์ค๊ฒ ๋จ (maximum recursion depth ์ด๊ณผ)

  => ์ด๋ฌํ topdown ๋ฐฉ์์ ์คํ์ ๋ฆฌ๋ฐ์ด ์์ 
  ์๋ฅผ ๋ค์ด, f(10000)์ ํ๋ฉด f(9999) f(9998) ... f(2)๊น์ง ๋ชจ๋ ๊ณ์ฐํด์ผ ํจ 

- bottom up ๋ฐฉ์์ ์ฌ์ฉํ๋ค. (๊ฐ์ฅ ์์ subproblem๋ถํฐ ์์)

  for loop์ผ๋ก array๋ฅผ ์ฑ์๋๊ฐ๋ค. 

  ```python
  def fib_dp(n) : 
      if n==0 : 
          return 1 
      elif n==1 : 
          return 1
      fib_array = [1,1]
      
      for i in range(2, n+1) : 
          num = fib_array[i-1] + fib_array[i-2]
          fib_array.append(num)
      return fib_array[n]
  ```

  => O(n)๊ณผ O(1)์ด ๊ฑธ๋ฆผ 

  => ์๋ํ๋ฉด, F(3)์ ๊ตฌํ๊ธฐ ์ํด์  ๊ฐ์ฅ ์ต๊ทผ ๊ฒ์ธ F(2)์ F(1)๋ง ๋ณด๋ฉด ๋จ 

  => F(n)์ ๊ตฌํ๊ธฐ ์ํด์๋ ๊ฐ์ฅ ์ต๊ทผ ๊ฒ ๋ ๊ฐ๋ง ๋ณด๋ฉด ๋จ 

  => ๊ทธ๋์ ๊ทธ ์์ ๊ฒ๋ค์ ์ง์ธ ์ ์์ 





#### 1463 

ํ๋ฆผ 

#### 11726 

- ํฉํ ๋ฆฌ์ผ ํจ์, ์ฌ๊ทํจ์๋ก ๊ตฌํํด์ ์ฌ์ฉํ๋๋ ๋ฐํ์ ์๋ฌ ๋จ 









----




## โฑ ์๊ฐ๋ณต์ก๋

### input vs sys.stdin.readline()

- input ๋ณด๋ค sys.stdin.readline()์ด ๋ ๋น ๋ฅด๋ค

```python
import sys # from sys import stdin
n = int(sys.stdin.readline()) # stdin.readline(), ํ ์ค์ ์ฌ๋ฌ ๊ฐ ์๋ ฅ ๊ฐ๋ฅ 
```

- sys.stdin.readline() :  ์ฅฌํผํฐ ๋ธํธ๋ถ์์ ์คํ ์๋จ... 



### list

| Operation     | Example         | Big-O      | Notes                     |
| ------------- | --------------- | ---------- | ------------------------- |
| Index         | l[i]            | O(1)       |                           |
| Store         | l[i] = 0        | O(1)       |                           |
| Length        | len(l)          | O(1)       |                           |
| Append        | l.append(5)     | O(1)       |                           |
| Pop           | l.pop()         | O(1)       | l.pop(-1) ๊ณผ ๋์ผ         |
| Clear         | l.clear()       | O(1)       | l = [] ๊ณผ ์ ์ฌ            |
| Slice         | l[a:b]          | O(b-a)     | l[:] : O(len(l)-0) = O(N) |
| Extend        | l.extend(โฆ)     | O(len(โฆ))  | ํ์ฅ ๊ธธ์ด์ ๋ฐ๋ผ          |
| Construction  | list(โฆ)         | O(len(โฆ))  | ์์ ๊ธธ์ด์ ๋ฐ๋ผ          |
| check ==, !=  | l1 == l2        | O(N)       | ๋น๊ต                      |
| Insert        | ใฃ.insert(i, v) | O(N)       | i ์์น์ v๋ฅผ ์ถ๊ฐ         |
| Delete        | del l[i]        | O(N)       |                           |
| Remove        | l.remove(โฆ)     | O(N)       |                           |
| Containment   | x in/not in l   | O(N)       | ๊ฒ์                      |
| Copy          | l.copy()        | O(N)       | l[:] ๊ณผ ๋์ผ - O(N)       |
| Pop           | l.pop(i)        | O(N)       | l.pop(0):O(N)             |
| Extreme value | min(l)/max(l)   | O(N)       | ๊ฒ์                      |
| Reverse       | l.reverse()     | O(N)       | ๊ทธ๋๋ก ๋ฐ๋๋ก             |
| Iteration     | for v in l:     | O(N)       |                           |
| Sort          | l.sort()        | O(N Log N) |                           |
| Multiply      | k*l             | O(k N)     | [1,2,3] * 3 ยป O(N**2)     |

## โ ๋ฌธ๋ฒ 



**for๋ฌธ**

- for i in range(4) : print(i) # 0, 1, 2, 3
- for i in range(4) : print(~i) # -1, -2, -3, -4
- input().split()์ ํ์ ์์ ๋ ๋ง๊ณ ๋ list()๋ก ๊ฐ์ธ์ค ํ์ ์ ์ฉํ์!!! 
- **๐ซ๐ซ์ถ๋ ฅ ํํ ๊ผญ ์ข ํ์ธํ๊ณ  ์ ์ถํ์!!!!!!!!!!!!!!!!!!!!!!!!!!!!!๐ข๐ข**



<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream


**์กฐ๊ฑด๋ฌธ**

```python
if 'a' < 'b' < 'c' : print('๋๋ค')
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
**์กฐ๊ฑด๋ฌธ**

```python
if 'a' < b < 'c' : print("๋จ")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
```



<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
=======


>>>>>>> Stashed changes
## ๐ Reference 

- [๋ฆฌ์คํธ ์๊ฐ๋ณต์ก๋](https://wayhome25.github.io/python/2017/06/14/time-complexity/)

  

----



# ๐ ์ผ๊ธฐ 

## 0818

.... 3๋ฌธ์  ํ์๋๋ฐ ์ 1์๊ฐ์ด ์ง๋์์ฃ ...??? ใใใ 
์๋ฃ๊ตฌ์กฐ ๊ณต๋ถํ๊ณ  ํ์ด์ผ ํ๋๋ด๋๋ค. 
์ ๋ค ์๊ฐ์ด๊ณผ๋ก ๊ฑธ๋ฆฌ๋ ๊ฑฐ์ฃ  
์ฌํ๋๋ค ๐ฅ



## 0819

์.. ์คํ์ ์ฌ๋ฌ ๊ฐ ํ์ฉํ๋ ๊ฒ์ด ํ์ํ๋ค๋ ๊ฒ์ ์๊ฒ ๋์์ 

ํ์ง๋ง, ๋ถ๋ช ์ฝ๋ ๊ตฌ์ฑ์ ๋๊ฐ์๋ฐ, ๋ณ์๋ช๋ง ๋ค๋ฅธ ๊ฒ ๊ฐ์๋ฐ ์ด๋ ํ ์ฐจ์ด์ ์์ ๋ง๊ณ  ํ๋ฆฌ๊ณ (์๊ฐ์ด๊ณผ๋ ์๋๊ณ !!!)๊ฐ ๊ฒฐ์ ๋๋์ง๊ฐ ๊ถ๊ธํ๋ค. ๋ฏธ๊ฒฝ์ด๋ ๊ฐ์ด ์์๋ด๋ด์ผ์ง 



## 0820 

์ค๋์ ํ๋ถํฐ ๋ฑ๊น์ง ํ์

ํผ ๋ฌธ์  ์๋ ๋ช ๊ฐ ์๋๋ฐ ํ ์๊ฐ์ ํ๋ฑ ๊ฐ๋๊ตฐ ... 

์๊ฐ์ ๋ฌ๋ ค๋ผ~~ 

๊ทธ๋๋ ๊ธฐ์ด๋ฅผ ์ก๊ณ  ๊ฐ๋ ๊ธฐ๋ถ์ด๋ผ ์ข๋ค!! ๐ช๐ป๐ช๐ป



## 0827 

์ ... DP ํ์๋ค!!! ์ง์ง ์๊ณ ๋ฆฌ์ฆ ๊ณต๋ถ ์ด์ฌํ ํด์ผ์ง 


# ๐ํ๋ก๊ทธ๋๋จธ์ค

## 3์ง๋ฒ ๊ณ์ฐํ๊ธฐ 
<div> int(tmp,3) ํ๋ฉด ์์์ 3์ง๋ฒ์ผ๋ก ๊ณ์ฐํด์ค </div>