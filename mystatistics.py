import json
import sys

def statistics(datafile):
    with open('ranges.json') as data:
        rg = json.load(data)
    rgval = list(rg.values())

    with open(datafile) as fi:
        data = fi.read().split('\n')

    num = list(map(lambda x:[0]*len(x), rg.values()))
    cnt = 0

    fo = open('result','w')
    sys.stdout = fo

    def count(x): 
        for i,key in zip(range(len(rg)),rg):
            operL,operR = key.split('|')
            for j,r in zip(range(len(rg[key])),rg[key]):
                exec(
                    'if {0} {1} {2} {3} {4}: num[i][j] += 1'.format(r[0],operL,x,operR,r[1]),
                    {'num' : num, 'i' : i, 'j' : j}
                )

    for s in data:
        if s[0:2] == '//': continue
        elif s[0] == '#': print(s)
        elif s == '...':
            for i in range(len(rgval)):
                for j in range(len(rgval[i])):
                    print(rgval[i][j][2],':',num[i][j])
            print('Total:',cnt)
            print('---------------------')
            num = list(map(lambda x:[0]*len(x), rg.values()))
            cnt = 0
        else:
            cnt += 1
            count(float(s))
            
    fo.close()