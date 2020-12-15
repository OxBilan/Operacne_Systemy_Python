
def eval_expr(t,d={}):

    t=t.split()
    n=len(t)
    st =[]
    pocet=0
    
    for i in range(n):

        if t[i] in d:

            pocet+=1

    if pocet == 0:

        return 0

    for i in range(n):
            
        if t[i] in d:

            st.append(int(d[t[i]]))

        if t[i].isdigit():
       
            st.append(int(t[i]))
    
        elif t[i]=="+":
    
            a=st.pop()
            b=st.pop()
            st.append(int(a)+int(b))
    
        elif t[i]=="*":
     
            a=st.pop()
            b=st.pop()
            st.append(int(a)*int(b))
    
        elif t[i]=="/":
    
            a=st.pop()
            b=st.pop()
            st.append(int(b)/int(a))
    
        elif t[i]=="-":
    
            a=st.pop()
            b=st.pop()
            st.append(int(b)-int(a))
    
    return st.pop()


def to_infix(t):

    t=t.split()
    n=len(t)
    st =[]

    for i in range(n):

        if t[i].isdigit():

            st.append(int(t[i]))

        elif t[i]=="+":

            a=st.pop()
            b=st.pop()
            st1="( {} + {} )".format(b,a)
            st.append(st1)

        elif t[i]=="-":

            a=st.pop()
            b=st.pop()
            st2="( {} - {} )".format(b,a)
            st.append(st2)

        elif t[i]=="*":
        
            a=st.pop()
            b=st.pop()
            st3="( {} * {} )".format(b,a)
            st.append(st3)

        elif t[i]=="/":

            a=st.pop()
            b=st.pop()
            st4="( {} / {} )".format(b,a)
            st.append(st4)

    print(st.pop())
