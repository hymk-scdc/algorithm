# 1717 집합의 표현
'''
자료구조 중 노드 구조로 확인
집합의 대표값 하나인 부모 노드끼리만 비교하여 진행
(화요일에 이거 다시 코드 짜보기)
'''
n, m = map(int, input().split())
li = []
for _ in range(m) :
   o, a, b = map(int, input().split())
   if o == 0 :
       a_idx = '없음'
       b_idx = '없음'
       for j in range(len(li)):
           if a in li[j] :
               a_idx = j
           if b in li[j] :
                b_idx = j
       if b_idx == '없음' and a_idx != '없음' :
           li[a_idx] = li[a_idx].union({b})
       elif a_idx == '없음' and b_idx == '없음' :
           li.append({a,b})
       elif a_idx == '없음' and b_idx != '없음' :
           li[b_idx] = li[b_idx].union({a})
       else :
           if a_idx != b_idx:
               set_a, set_b = li[a_idx], li[b_idx]
               li.remove(set_a)
               li.remove(set_b)
               li.append(set_a.union(set_b))
   else :
       ans = 'NO'
       for j in range(len(li)):
           if a in li[j] and b in li[j] :
               ans = 'YES'
               break

       print(ans)






