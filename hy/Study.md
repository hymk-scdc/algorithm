# 💻스터디 사항 

## 🙋🏻‍♀️ 알고리즘 기초 

### 1. 알고리즘과 입출력 

#### [2442](https://www.acmicpc.net/problem/2442)

#### [2443](https://www.acmicpc.net/problem/2443)

### 2. 자료구조 1 

#### 10828 

- 원인 : 시간초과 

- 해결 

  - `input()` 대신 `sys.stdin.readline()` 

  - for 문에 있던 조건문들을 모두 함수로 정의해서 사용 

    

#### 10799

- 요거는 그림 그리면서 다시 공부해야 할 듯 



#### 1406

- 원인 : 시간초과 

- 해결 

  - for 문에 있던 조건문들을 모두 함수로 정의해서 사용 
  - 함수 정의 시, global 선언해주고 변수명 사용하기 - 근데 왜 10828 할 때, stack 리스트는 선언하지 않고도 사용이 가능했는가? 
  - `input()` 대신 `sys.stdin.readline()` 

  => 여기까지해도 시간초과로 틀림 

  - stack 2개로 나눠서 접근 
  - `insert`보다 `pop()`과 `append()`를 사용해서 쓰는 것이 더 좋음 
  - 하지만 코드 구조 99% 똑같은데 맞고 틀리고가 갈림 확인 필‼
  - 조건 줄 때, try나 except로 쉽게 가려고 하지말고, 꼼꼼하게 다 예외처리 해주기!!! 



### 3. 다이나믹 프로그래밍 

### 개념 이해 

#### 조건 

- 하나의 problem이 더 작은 subproblem으로 쪼개질 때
- subproblem들의 해결로 더 큰 subproblem을 해결할 수 있을 때 
- subproblem이 겹칠 때 

**예시**

피보나치 수열 O(2^n)

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
 %%timeit # 시간 재는 것 
 fib_naive(35)
 ```

- array에 담아서 해결한다 

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

  => 하지만, 큰 수를 넣게되면 런타임 에러가 나오게 됨 (maximum recursion depth 초과)

  => 이러한 topdown 방식은 스택의 리밋이 있음 
  예를 들어, f(10000)을 하면 f(9999) f(9998) ... f(2)까지 모두 계산해야 함 

- bottom up 방식을 사용한다. (가장 작은 subproblem부터 시작)

  for loop으로 array를 채워나간다. 

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

  => O(n)과 O(1)이 걸림 

  => 왜냐하면, F(3)을 구하기 위해선 가장 최근 것인 F(2)와 F(1)만 보면 됨 

  => F(n)을 구하기 위해서도 가장 최근 것 두 개만 보면 됨 

  => 그래서 그 앞에 것들은 지울 수 있음 





#### 1463 

틀림 

#### 11726 

- 팩토리얼 함수, 재귀함수로 구현해서 사용했더니 런타임 에러 남 









----




## ⏱ 시간복잡도

### input vs sys.stdin.readline()

- input 보다 sys.stdin.readline()이 더 빠르다

```python
import sys # from sys import stdin
n = int(sys.stdin.readline()) # stdin.readline(), 한 줄에 여러 개 입력 가능 
```

- sys.stdin.readline() :  쥬피터 노트북에서 실행 안됨... 



### list

| Operation     | Example         | Big-O      | Notes                     |
| ------------- | --------------- | ---------- | ------------------------- |
| Index         | l[i]            | O(1)       |                           |
| Store         | l[i] = 0        | O(1)       |                           |
| Length        | len(l)          | O(1)       |                           |
| Append        | l.append(5)     | O(1)       |                           |
| Pop           | l.pop()         | O(1)       | l.pop(-1) 과 동일         |
| Clear         | l.clear()       | O(1)       | l = [] 과 유사            |
| Slice         | l[a:b]          | O(b-a)     | l[:] : O(len(l)-0) = O(N) |
| Extend        | l.extend(…)     | O(len(…))  | 확장 길이에 따라          |
| Construction  | list(…)         | O(len(…))  | 요소 길이에 따라          |
| check ==, !=  | l1 == l2        | O(N)       | 비교                      |
| Insert        | ㅣ.insert(i, v) | O(N)       | i 위치에 v를 추가         |
| Delete        | del l[i]        | O(N)       |                           |
| Remove        | l.remove(…)     | O(N)       |                           |
| Containment   | x in/not in l   | O(N)       | 검색                      |
| Copy          | l.copy()        | O(N)       | l[:] 과 동일 - O(N)       |
| Pop           | l.pop(i)        | O(N)       | l.pop(0):O(N)             |
| Extreme value | min(l)/max(l)   | O(N)       | 검색                      |
| Reverse       | l.reverse()     | O(N)       | 그대로 반대로             |
| Iteration     | for v in l:     | O(N)       |                           |
| Sort          | l.sort()        | O(N Log N) |                           |
| Multiply      | k*l             | O(k N)     | [1,2,3] * 3 » O(N**2)     |


## ❗ 문법 

- for i in range(4) : print(i) # 0, 1, 2, 3
- for i in range(4) : print(~i) # -1, -2, -3, -4

- input().split()은 확신있을 때 말고는 list()로 감싸준 후에 적용하자!!! 
- **🚫🚫출력 형태 꼭 좀 확인하고 제출하자!!!!!!!!!!!!!!!!!!!!!!!!!!!!!💢💢**

## 📕 Reference 

- [리스트 시간복잡도](https://wayhome25.github.io/python/2017/06/14/time-complexity/)

  

----



# 📝 일기 

## 0818

.... 3문제 풀었는데 왜 1시간이 지나있죠...??? ㅋㅅㅋ 
자료구조 공부하고 풀어야 하나봅니다. 
왜 다 시간초과로 걸리는 거죠 
슬픕니다 😥



## 0819

음.. 스택을 여러 개 활용하는 것이 필요하다는 것을 알게 되었음 

하지만, 분명 코드 구성은 똑같은데, 변수명만 다른 것 같은데 어떠한 차이점에서 맞고 틀리고(시간초과도 아니고!!!)가 결정되는지가 궁금하다. 미경이랑 같이 알아내봐야지 



## 0820 

오늘은 큐부터 덱까지 했음

푼 문제 수는 몇 개 없는데 한 시간은 후딱 가는군 ... 

시간아 달려라~~ 

그래도 기초를 잡고 가는 기분이라 좋다!! 💪🏻💪🏻



## 0827 

와 ... DP 풀었다!!! 진짜 알고리즘 공부 열심히 해야지 
