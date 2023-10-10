def paranthesis_check(l):
    braces={'{':'}','[':']','(':')'}
    bstack=[]
    if len(l)%2!=0:
        return False
    for i in l:
        if i in braces.keys():
            bstack.append(i)
        if i in braces.values():
            if len(bstack)==0:
                return False
            ele=bstack.pop()
            if braces.get(ele)!=i:
                return False
    if len(bstack)!=0:
        return False
    return True
l=list(input().split())
if paranthesis_check(l):
    print("balanced")
else:
    print("not balanced")
            

    
        
        
