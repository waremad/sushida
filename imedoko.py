def imadoko(pt,ls):
    if pt[0] == 0:
        return [0,0]
    n = 0
    tx = ""
    while not(len(tx) >= pt[0]+1):
        if len(ls) <= n:
            return "over"
        tx = tx + ls[n][0]
        n = n + 1
    return [n-1,len(ls[n-1][0]) - (len(tx)-pt[0])]

assert imadoko([0,0],[[""]]) == [0,0]
assert imadoko([0,0],[["a"],["a"]]) == [0,0]
assert imadoko([1,0],[["a"],["a"]]) == [1,0]
assert imadoko([0,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [0,0]
assert imadoko([1,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [0,1]
assert imadoko([2,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [1,0]
assert imadoko([3,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [1,1]
assert imadoko([4,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [2,0]
assert imadoko([5,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [2,1]
assert imadoko([6,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [3,0]
assert imadoko([7,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [3,1]
assert imadoko([8,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [4,0]
assert imadoko([9,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [5,0]
assert imadoko([10,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [6,0]
assert imadoko([11,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == [6,1]
assert imadoko([12,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == "over"
assert imadoko([13,0],[["te"],["su"],["to"],["zi","ji"],["e"],["n"],["do"],]) == "over"

testls = [['zye', 'je'], ['zye', 'je'], ['zye', 'je'], ['!'], ['no'], ['tu', 'tsu'], ['-'], ['hu', 'fu'], ['-']]
assert imadoko([2, 0],testls) == [0,2]