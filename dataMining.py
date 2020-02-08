import math
import random
import operator


min_sup = 0.09
min_conf = 0.8
def transition():
    list_ans = []
    map_ans = {}
    for i in range(1,801,1):
        list_data = []
        for j in range(0,random.randint(2,5),1):
            list_data.append(random.randint(1,50))
        list_ans.append(list_data)
    for i in range(801,1001,1):
        list_data = []
        for j in range(0,random.randint(6,8),1):
            list_data.append(random.randint(1,50))
        list_ans.append(list_data)
    random.shuffle(list_ans)
    for i in range(1,1001,1):
        map_ans[i] = list_ans[i-1]
    return map_ans

def AR():
    map_sum = {}
    map_data = {}
    map_1 = {}
    map_2 = {}
    list_1 = []
    list_2 = []
    list_3 = []
    for key,valueOfkey in transition().items():
        map_data[key] = valueOfkey
    for key,valueOfkey in map_data.items():
        for i in range (1,51,1):
            if i in valueOfkey:
                map_sum[i] = map_sum.get(i,0) + 1
    for key,valueOfkey in map_sum.items():
        if (map_sum.get(key)/1000) > min_sup:
            list_1.append(key)
    for i in range(1,1001,1):
        for j in range(0,len(list_1),1):
            for k in range(j+1,len(list_1),1):
                if(list_1[j] and list_1[k] in map_data.get(i)):
                    map_1[(list_1[j],list_1[k])] = map_1.get((list_1[j],list_1[k]),0) + 1
    for key,valueOfkey in map_1.items():
        if (map_1.get(key)/1000) > min_sup:
            list_2.append(key)
    for i in range(1,10,1):
        for j in range(0,len(list_2),1):
            for k in range(j+1,len(list_2),1):
                check1 = operator.itemgetter(0)
                check2 = operator.itemgetter(1)
                if(check1(list_2[j]) == check1(list_2[k])):
                    if(check1(list_2[j]) and check2(list_2[j]) and check2(list_2[k]) in map_data.get(i)):
                        map_2[(check1(list_2[j]),check2(list_2[j]),check2(list_2[k]))] = map_2.get((check1(list_2[j]),check2(list_2[j]),check2(list_2[k])),0) + 1               
    for key,valueOfkey in map_2.items():
        if (map_2.get(key)/1000) > min_sup:
            list_3.append(key)
    return list_3

print(AR())
    