PS='{-s num &<2-10>|-M num &<2-10>|-m num num |-d num num}'
PS2='[-h][-n name][-r {x|y|z}*[x|y|z]*]'
PS3='[-d|-z|-f]'
PS4='[-h][-d]'
PS5='[-h][-n name]'
PS6='[-n name]'
PS7='[-r {x|y|z}[x|y|z]]'
PS8='[-r [x|y|z]]'
PtoR={'num':'-?\d*.','x':'[A-Z]','y':'[a-z]','z':'[0-9]','name':'[A-Za-z0-9]+'}
SYMBOLS = {'{': '}', '[': ']'}
SYMBOLS_L, SYMBOLS_R = SYMBOLS.keys(), SYMBOLS.values()
import re
def check(s):
    expect=[]
    arr = []
    pos=[]
    pnum=1   #标记一对括号对里参数的个数
    length=len(s)
    i=0
    frontisor=False   #判断此参数前面是否还有同等地位参数
    while i<length:
        c=s[i]
        if(len(pos)>0):
            nowpos = pos[-1]
        if c in SYMBOLS_L:
            arr.append(c)
            expect.append(SYMBOLS[c])
            pos.append(len(arr)-1)
        elif c in SYMBOLS_R:
            frontisor=False
            if c==expect[-1]:

                if i+1 < length: #判断是否带有*标志
                    if s[i+1]=='*':
                        if c == ']':
                            temp = ''
                            for j in range(nowpos + 1, len(arr)):
                                temp = temp + arr[j]
                            temp = "(" + temp + "){0," + str(pnum) + "}"
                            for j in range(nowpos, len(arr)):
                                arr.pop()
                            arr.append(temp);
                            pnum = 1
                        elif c == '}':
                            temp = ''
                            for j in range(nowpos + 1, len(arr)):
                                temp = temp + arr[j]
                            temp = "(" + temp + "){1,"+str(pnum)+"}"
                            for j in range(nowpos, len(arr)):
                                arr.pop()
                            arr.append(temp);
                            pnum=1

                    else:
                        if c == ']':
                            temp = ''
                            for j in range(nowpos + 1, len(arr)):
                                temp = temp + arr[j]
                            temp = "(" + temp + "){0,1}";
                            for j in range(nowpos, len(arr)):
                                arr.pop()
                            arr.append(temp);
                        elif c == '}':
                            temp = ''
                            for j in range(nowpos + 1, len(arr)):
                                temp = temp + arr[j]
                            temp = "(" + temp + ")";
                            for j in range(nowpos, len(arr)):
                                arr.pop()
                            arr.append(temp);
                else:
                    if c==']':
                        temp=''
                        for j in range(nowpos+1,len(arr)):
                            temp=temp+arr[j]
                        temp="("+temp+"){0,1}";
                        for j in range(nowpos,len(arr)):
                            arr.pop()
                        arr.append(temp);
                    elif c=='}':
                        temp=''
                        for j in range(nowpos+1,len(arr)):
                            temp=temp+arr[j]
                        temp="("+temp+")";
                        for j in range(nowpos,len(arr)):
                            arr.pop()
                        arr.append(temp);
                expect.pop()
                pos.pop()
            else:
                return False
        elif c =='-':        #操作判断
            if i+1<length:
                k=0
                for j in  range(i+1,length):
                    #print(j,length)
                    if s[j].isalpha():
                        c=c+s[j]
                    else:
                        break
                    k=k+1
                i=i+k
                if(frontisor):
                    temp = arr[-1]+"("+c+")"
                    arr.pop()
                    arr.append(temp)
                elif s[i+1] in SYMBOLS_R:
                    arr.append(c)
                else:
                    arr.append("(" + c + ")")
                    '''
                if (s[i + 1] == '|'):
                    pnum = pnum + 1
                    temp = arr[-1] + '|'
                    frontisor=True
                    arr.pop()
                    arr.append(temp)
                    '''
            else:
                return False
        elif c.isalpha():       #参数判断
            j=i
            while(s[i+1].isalpha() or s[i+1]=='-'):
                i=i+1
            if(i>j):
                parameter=s[j:i+1]
            else:
                parameter=c
            if (frontisor):
                temp = arr[-1] + "(" + PtoR[parameter] + ")"
                arr.pop()
                arr.append(temp)
            else:
                arr.append("(" + PtoR[parameter] + ")")
            #print(s[i+1])
            '''
            if(i+1<length and s[i+1]=='|'):
                pnum=pnum+1
                frontisor=True
                temp=arr[-1]+'|'
                arr.pop()
                arr.append(temp)
            '''
        elif c=="&":

            j=i+1
            while(s[i]!='>'):
                i=i+1
            temp=s[j+1:i]
            (begin,end)=temp.split('-')
            pwithiter=arr[-1]+"{"+begin+","+end+"}"
            arr.pop()
            arr.append(pwithiter)
        elif c=="|":
            frontisor=True
            temp = ''
            for j in range(nowpos + 1, len(arr)):
                temp = temp + arr[j]
            for j in range(nowpos+1, len(arr)):
                arr.pop()
            temp=temp+'|'
            arr.append(temp);
            pnum = pnum+1
        i=i+1

    REG=''
    for k in arr:
        REG=REG+k
    print(REG)
    return True

ans=check(PS3)
print(ans)