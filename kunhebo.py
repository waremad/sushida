

def kunhebo(ls,lsp,eve):
    if ls == [[""]]:
        return False
    bool1 = False
    for i in range(len(ls[lsp[0]])):
#        print(i,ls,lsp,eve)
        if len((ls[lsp[0]])[i]) >= lsp[1]+1:
            if (ls[lsp[0]])[i][lsp[1]] == eve:
                bool1 = True
    return bool1

assert kunhebo([[""]],[0,0],"x") == False
assert kunhebo([["a"],["a"]],[0,0],"x") == False
assert kunhebo([["a"],["a"]],[1,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[0,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[0,1],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[1,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[1,1],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[2,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[2,1],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[3,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[3,1],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[4,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[5,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[6,0],"x") == False
assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[6,1],"x") == False

assert kunhebo([["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"]],[3,0],"j") == True

assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[0,0],"j") == True
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[1,0],"j") == True
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[2,0],"j") == True
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[4,1],"s") == True
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[6,0],"f") == True

assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[0,1],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[0,2],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[1,1],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[1,2],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[2,1],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[2,2],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[3,0],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[3,1],"j") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[4,0],"s") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[5,0],"s") == False
assert kunhebo([["zye","je"],["zye","je"],["zye","je"],["no"],["tu","tsu"],["-"],["hu","fu"],["-"],]
               ,[6,1],"f") == False