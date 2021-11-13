'''# mylist = [3 3 E32(3) E3(1/3) E43 N]
# output : 3 3 1: 3 2 3 2: 3 (1/39) 3: 4 3
# mylist 변수명
myinput = ['3', '3', 'E32(3)', 'E3(1/3)', 'E43', 'N']

mylist = list(map(int, myinput[:2]))

for i in range(1, len(myinput[2:])+1):
    if myinput[i+1] == "N":
        mylist.append(0)
        break
    else:
        mylist.append(i)
        splited = myinput[i+1].split("(") # E3(1/3)
        for j in splited[0]:
            if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                mylist.append(int(j))
        if len(splited) == 2:
            temp = splited[1].replace(")", "")
            temp = temp.split('/')
            if len(temp)==2:
                mylist.append(float(temp[0])/float(temp[1]))
            else:
                mylist.append(float(temp[0]))

'''


##

# file = [3 3 E32(3) E3(1/3) E43 N]
# output : 3 3 1: 3 2 3 2: 3 (1/39) 3: 4 3
# file 변수명

myinput = ['3', '3', 'E32(3)', 'E3(1/3)', 'E43', 'N']

mylist = list(map(int, myinput[:2]))

for i in myinput[2:]:
    if i == "N":
        mylist.append(0)
        break
    else:
        splited = i.split("(") # E3, (1/3)
        firstnum = []
        for j in splited[0]:
            if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                firstnum.append(int(j))
        if len(splited) == 1: # 괄호 없음
            mylist.append(3)
            mylist += firstnum
        else: # 괄호 있음
            if len(splited[0]) ==2: # 숫자하나, 괄호 있음:
                mylist.append(2)
                mylist += firstnum
            else:
                mylist.append(1)

            temp = splited[1].replace(")", "")
            temp = temp.split('/')
            if len(temp)==2:
                mylist.append(float(temp[0])/float(temp[1]))
            else:
                mylist.append(float(temp[0]))



while(1):
    file_name = input("Enter the data file name : ")
    f = open("./"+file_name+".txt", 'r')
    line = f.readlines()

    myinput = []
    for i in line:
        myinput.append(i.replace("\n",""))
    f.close()

    ##

    mylist = list(map(int, myinput[:2]))

    for i in range(1, len(myinput[2:])+1):
        if myinput[i+1] == "N":
            mylist.append(0)
            break
        else:
            mylist.append(i)
            splited = myinput[i+1].split("(") # E3(1/3)
            for j in splited[0]:
                if j in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    mylist.append(int(j))
            if len(splited) == 2:
                temp = splited[1].replace(")", "")
                temp = temp.split('/')
                if len(temp)==2:
                    mylist.append(float(temp[0])/float(temp[1]))
                else:
                    mylist.append(float(temp[0]))
    ##


    cnt=0
    row=mylist[cnt];cnt+=1
    col=mylist[cnt];cnt+=1
    if row!=col :
        print("please input square matrix(row=col)")
        break
    mat = [ [0 for i in range(col)] for j in range(row)]
    for i in range(row):
        for j in range(col):
            if i==j:
                mat[i][j]==1
            else:
                mat[i][j]==0
    if mylist[cnt]==1:
        cnt+=1
        a=mylist[cnt];cnt+=1
        b=mylist[cnt];cnt+=1
        if a>row or b>row :
            ("please write correct ERO")
            break
        c=mylist[cnt];cnt+=1
        mat[b-1][a-1] = mat[b-1][a-1] + mat[a-1][a-1]*c
        for i in range(row):
            for j in range(col):
                print(mat[i][j], ' ')
            print()

    elif mylist[cnt]==2:
        cnt+=1
        a=mylist[cnt];cnt+=1
        if a>row :
            ("please write correct ERO")
            break
        c=mylist[cnt];cnt+=1
        mat[a-1][a-1]=mat[a-1][a-1]*c

    elif mylist[cnt]==3:
        cnt+=1
        a=mylist[cnt];cnt+=1
        b=mylist[cnt];cnt+=1
        if a>row or b>row :
            ("please write correct ERO")
            break
        mat[a-1][b-1]=mat[b-1][b-1]
        mat[b-1][a-1]=mat[a-1][a-1]
        mat[a-1][a-1]=0
        mat[b-1][b-1]=0
    else :
        break
    break