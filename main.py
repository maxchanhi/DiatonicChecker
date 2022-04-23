inputTET = input("Enter n-TET to check is it fit Blackwood's 5w+2h system:")
TET = int(inputTET)
w = 1
countint = []
while w < TET:
    h = (TET-(5*w))/2
    h_int = h.is_integer()
    if h_int == True and w>h>0:
        print("If it is",TET,"-TET,","there are",w,"step(s) in a whole tone, and", int(h), "step(s) in a half tone.")
        countint.append(h_int)
    else:
        pass
    w +=1
if len(countint) == 0:
    print(TET,"-TET does not fit into the Blackwood's 5w+2h system.")
else:
    pass


