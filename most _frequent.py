import operator
def my_fun():
    t=""
    dic={}
    s="mississippi"
    for i in s:
        if i not in t:
            a=s.count(i)
            t=t+i
            dic.update({i:a})
    s=dict(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
    return s
a=my_fun()
for x,y in a.items():
    print(x,"=",y)
    
    
    
    
    
    
    


    
    
    



