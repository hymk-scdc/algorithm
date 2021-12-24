# 1654 : 랜선 자르기
K, N = map(int, input().split(" "))
lines = []
for i in range(K):
    lines.append(int(input()))

maxline = max(lines)

def get_max(n, start, mid, end, yn):
    cnt_lines = 0
    for i in lines:
        cnt_lines += i//mid
    if mid == maxline:
        print(mid)
        return
    '''
    print('mid',mid)
    print('cnt_lines',cnt_lines)
    print('yn',yn)
    print('----')'''

    if cnt_lines < n:
        if yn == 1:
            print(mid-1)
            return
        get_max(n, start, (start+mid)//2, mid, yn=0)
    else:
        #print(mid+1,"~" ,end, 'yn=1')
        #print('----')
        get_max(n, start, mid+1, end, yn=1)


get_max(N, 1, (1+maxline)//2, maxline, 0)
