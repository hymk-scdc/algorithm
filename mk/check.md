# Check 

### 2021.08.17
1. map 함수
2. try, except, finally 정리

### 2021.08.18

### 2021.08.19
1. 내장 함수를 어느 정도까지 써도 되는지 모르겠다
2. 시간 초과 - 어떤 로직이 시간복잡도가 높은지 파악하는 것은... 계속 숙제

### 2021.08.22
1. [백준 시간 초과 원인](https://www.acmicpc.net/problem/15552)  
- Python  
  - 원인 : for문 문제를 풀 때 입출력 방식이 느리면 여러 줄을 입력/출력할 때 시간 초과가 날 수 있다
  - 해결 : input 대신 sys.stdin.readline을 사용.  단, 맨 끝의 개행문자까지 입력받으므로 문자열을 저장할 땐 .rstrip()을 추가로 해 주는 것이 좋다.
- 결론 : readline이나 PyPy로 제출하면 대부분 해결
2. [백준 문제 풀이 시 유의사항](https://www.acmicpc.net/blog/view/55)
3. 10828번 문항 
```
import sys
input = sys.stdin.readline
```
위에 추가해서 해결
4. ```if 문자열 == 문자열``` , ```if 문자열[:숫자] == 문자열``` : 연산 시간 차이가 많이 나나?  
5. list에서 인덱싱 슬라이싱보다 append, pop이 빠름