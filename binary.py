def getFirstLast(a,b):
    f, l = "", ""; 
    if (len(a) >= len(b)):
        f,l = a, b; 
    else:
        f,l = b,a; 
    return f,l

def binaryStrToInts(a):
    return [int(i) for i in a]

def addToResult(result, val1, val2):
    r = val1 + val2
    carry = -1
    append = "" 
    if (r == 3):
        carry,append = 1,"1"
    if (r == 2):
        carry,append = 1,"0"
    if (r == 0):
        carry,append = 0,"0" 
    if (r == 1):
        carry,append = 0,"1"

    return carry,append+result

def getSafe(i, arr):
    if (i >= 0):
        return arr[i]
    return 0 

def addBinary(a,b):
    first,last = getFirstLast(a,b)
    first = binaryStrToInts(first) 
    last = binaryStrToInts(last) 

    i = len(first)-1
    j = len(last)-1
    
    result = ""; 
    carry = 0 
    while True:
        val1,val2 = getSafe(i, first), getSafe(j, last) 
        val1 += carry
        carry, result = addToResult(result, val1, val2)
        
        i -= 1 
        j -= 1

        if i < 0 and j < 0:
            break
    if carry == 1:
        result = "1" + result 

    return result 
        
assert addBinary("1010","1011") == "10101"
assert addBinary("1", "11") == "100"
assert addBinary("1","1") == "10"
assert addBinary("11", "1") == "100"
assert getSafe(1, [1,2]) == 2
assert getSafe(-1, [1,2]) == 0
assert addToResult("", 2, 1) == (1, "1")
assert addToResult("", 1, 1) == (1, "0")
assert addToResult("1", 1, 1) == (1, "01")
assert addToResult("", 1, 0) == (0, "1")
assert addToResult("", 0, 0) == (0, "0")
assert getFirstLast("111", "11") == ("111", "11") 
assert getFirstLast("11", "111") == ("111", "11")
assert binaryStrToInts("1010") == [1,0,1,0]
