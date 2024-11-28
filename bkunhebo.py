

def bkunhebo(ls,lsp,eve):
    if ls == [[""]]:
        return False
    if lsp[1] != 0:
        return False
    if lsp[0] == 0:
        return False
    bool1 = False
    lls = ls[lsp[0]-1]
    for i in range(len(lls)):
#        print(i,ls,lsp,eve)
        if len(lls[i]) > len(lls[0]):
            if lls[i][len(lls[0])] == eve:
                bool1 = True
    return bool1

assert bkunhebo([[""]],[0,0],"x") == False
assert bkunhebo([["a"],["a"]],[0,0],"x") == False
assert bkunhebo([["a"],["i"],["bo"],["u"]],[2,1],"x") == False
assert bkunhebo([["a"],["n","nn","xn"],["bo"],["u"]],[3,0],"x") == False

assert bkunhebo([["a"],["n","nn","xn"],["bo"],["u"]],[2,0],"n") == True
assert bkunhebo([["a"],["n","nn","xn"],["n","nn","xn"],["u"]],[3,0],"n") == True
