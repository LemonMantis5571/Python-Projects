def findOccurence(s):
    string = s
    print(string.find("b"))
    print(string.find("c"))
    a = string.find("b")
    b = string.find("c")
    return [a,b]

[a,b] = findOccurence("aaabbbccc")
