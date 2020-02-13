import math
import random
import operator



min_sup = 5
min_conf = 0.2
check1 = operator.itemgetter(0)
check2 = operator.itemgetter(1)
check3 = operator.itemgetter(2)

def items():
    item=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX"]
    return item

def transition():
    list_ans = []
    map_ans = {}
    for i in range(1,801,1):
        list_data = []
        for j in range(0,random.randint(2,5),1):
            list_data.append(random.choice(items()))
        list_ans.append(list_data)
    for i in range(801,1001,1):
        list_data = []
        for j in range(0,random.randint(6,8),1):
            list_data.append(random.choice(items()))
        list_ans.append(list_data)
    # random.shuffle(list_ans)
    for i in range(1,1001,1):
        map_ans[i] = list_ans[i-1]
    return map_ans

def GG():
    transaction2=[["M","O","N","K","E","Y"],["D","O","N","K","E","Y"],["M","A","K","E"],["M","U","C","K","Y"],["C","O","O","K","I","E"]]
    return transaction2

def mapGG():
    zzz = 1
    mapGG = {}
    for i in GG():
        mapGG[zzz] = i
        zzz += 1
    return mapGG

def AR():
    item=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX"]
    map_sum = {}
    map_data = {}
    map_1 = {}
    map_2 = {}
    map_ans = {}
    list_1 = []
    list_2 = []
    list_3 = []
    for key,valueOfkey in transition().items():
        map_data[key] = valueOfkey
    for key,valueOfkey in map_data.items():
        for i in item:
            for j in valueOfkey:
                if (i == j):
                    map_sum[i] = map_sum.get(i,0) + 1
    for key,valueOfkey in map_sum.items():
        if map_sum.get(key) >= min_sup:
            list_1.append(key)
    for i in range(1,len(map_data)+1,1):
        for j in range(0,len(list_1),1):
            for k in range(j+1,len(list_1),1):
                if(list_1[j] in map_data.get(i) and list_1[k] in map_data.get(i)):
                    map_1[(list_1[j],list_1[k])] = map_1.get((list_1[j],list_1[k]),0) + 1
    for key,valueOfkey in map_1.items():
        if map_1.get(key) >= min_sup:
            list_2.append(key)
    for i in range(1,len(map_data)+1,1):
        for j in range(0,len(list_2),1):
            for k in range(j+1,len(list_2),1):
                if(check1(list_2[j]) == check1(list_2[k])):
                    if(check1(list_2[j]) in map_data.get(i) and check2(list_2[j]) in map_data.get(i) and check2(list_2[k]) in map_data.get(i)):
                        map_2[(check1(list_2[j]),check2(list_2[j]),check2(list_2[k]))] = map_2.get((check1(list_2[j]),check2(list_2[j]),check2(list_2[k])),0) + 1
    for key,valueOfkey in map_2.items():
        if map_2.get(key) >= min_sup:
            list_3.append(key)
            map_ans[key] = valueOfkey      

    return map_ans

def prob():
    map_ar = {}
    map_gg = {}
    map_probconf = {}
    map_conf = {}
    list_conf = []
    for key,valueOfkey in AR().items():
        map_ar[key] = valueOfkey
    for key,valueOfkey in transition().items():
        map_gg[key] = valueOfkey
    for key,valueOfkey in map_ar.items():
        map_sumkey = {}
        map_sumvalue = {}
        for i in range(1,len(map_gg)+1,1):
            if(check1(key) in map_gg.get(i) and check2(key) in map_gg.get(i) and check3(key) in map_gg.get(i)):
                map_sumkey[(check1(key),check2(key),"->",check3(key))] = map_sumkey.get((check1(key),check2(key),"->",check3(key)),0) + 1
            if(check1(key) in map_gg.get(i) and check2(key) in map_gg.get(i)):
                map_sumvalue[(check1(key),check2(key))] = map_sumvalue.get((check1(key),check2(key)),0) + 1
            if(check1(key) in map_gg.get(i) and check3(key) in map_gg.get(i)):
                map_sumvalue[(check1(key),check3(key))] = map_sumvalue.get((check1(key),check3(key)),0) + 1
            if(check2(key) in map_gg.get(i) and check3(key) in map_gg.get(i)):
                map_sumvalue[(check2(key),check3(key))] = map_sumvalue.get((check2(key),check3(key)),0) + 1
            if(check1(key) in map_gg.get(i)):
                map_sumvalue[(check1(key))] = map_sumvalue.get((check1(key)),0) + 1
            if(check2(key) in map_gg.get(i)):
                map_sumvalue[(check2(key))] = map_sumvalue.get((check2(key)),0) + 1
            if(check3(key) in map_gg.get(i)):
                map_sumvalue[(check3(key))] = map_sumvalue.get((check3(key)),0) + 1
        for key1,valueOfkey1 in map_sumkey.items():
            for key2,valueOfkey2 in map_sumvalue.items():
                map_probconf[key2] = map_probconf.get(key2,0) + map_sumkey.get(key1)/map_sumvalue.get(key2)
        for key3,valueOfkey3 in map_probconf.items():
            if(valueOfkey3 >= min_conf):
                map_conf[key3] = valueOfkey3
    print(map_ar)
    return map_conf
    

print(prob())
    