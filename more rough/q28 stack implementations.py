# stack Implementation
def isempty(stk):
    if stk==[]:
        return True
    else: return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isempty(stk): return 'Underflow'
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if isempty(stk): return 'Underflow'
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
    if isempty(stk): return 'Underflow'
    else:
        top=len(stk)-1
        print(stk[top],'<---Top')
        for a in range(top-1,-1,-1):
            print(stk[a])
stack=[]
top=None
while True:
    print('\n'*2,'Stack operations')
    print('1.Push')
    print('2.Pop')
    print('3.Peek')
    print('4.Display stack')
    print('5.Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        item=int(input('Enter item:'))
        Push(stack,item)
    elif ch==2:
        item=Pop(stack)
        if item=='underflow':
            print('Underflow!')
        else:
            print('Popped item is:',item)
    elif ch==3:
        item==Peek(stack)
        if item=='Underflow':
            print('Underflow')
        else:
            print('Top most item is:',item)
    elif ch==4:
        Display(stack)
    elif ch==5:
        break
    else:print('Invalid choice!')
