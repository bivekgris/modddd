
from queue import LifoQueue

def parenthesis(x):
    s1=LifoQueue(maxsize=0)
    l1=["[","{","("]
    
    for i in x:
        if i in l1:
            s1.put(i)
        else:
            top=s1.get()
            if top=="(":
                if i!=")":
                    return False
                
            if top=="{":
                if i!="}":
                    return False
            
            if top=="[":
                if i!="]":
                    return False
                
    return s1.empty()

a="[{}{})(]"
parenthesis(a)