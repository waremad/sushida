def unshift(self):
    dec = {"A":"a","B":"b","C":"c","D":"d","E":"e","F":"f","G":"g",
           "H":"h","I":"i","J":"j","K":"k","L":"l","M":"m","N":"n",
           "O":"o","P":"p","Q":"q","R":"r","S":"s","T":"t","U":"u",
           "V":"v","W":"w","X":"x","Y":"y","Z":"z",
           "!":"1","\"":"2","#":"3","$":"4","%":"5",
           "&":"6","\'":"7","(":"8",")":"9",
           "=":"-","~":"^","|":"\\",
           "`":"@","{":"[",
           "+":";","*":":","}":"]",
           "<":",",">":".","?":"/","_":"\\",}
    if self in list(dec.keys()):
        return dec[self]
    else:
        return self

assert unshift("") == ""
assert unshift("A") == "a" 
assert unshift("C") == "c"
assert unshift("I") == "i"
assert unshift("J") == "j"
assert unshift("L") == "l"
assert unshift("O") == "o"
assert unshift("S") == "s"
assert unshift("U") == "u"
assert unshift("V") == "v"
assert unshift("Z") == "z"

assert unshift("!") == "1"
assert unshift("?") == "/"