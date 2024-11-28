def yokei(self):
    if self == "":
        return ""

    mini = ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ","っ"]

    while self[0] in mini:
        self = self[1:]

    while self[-1] == "っ":
        self = self[:-1]
    
    self = list(self)
    y = []
    for i in range(len(self)):
        if i != 0:
            if self[i] in mini and self[i] == self[i-1]:
                pass
            else:
                y.append(self[i])
        else:
            y.append(self[i])
#    print(y)
    y = "".join(y)
#    print(y)
    return y

assert yokei("") == ""
assert yokei("てすと") == "てすと"
assert yokei("てっど") == "てっど"
assert yokei("かーど") == "かーど"
assert yokei("てっっど") == "てっど"
assert yokei("しゃゃいん") == "しゃいん"
assert yokei("っしゃいん") == "しゃいん"
assert yokei("っゃしゃいん") == "しゃいん"
assert yokei("しゃいんっ") == "しゃいん"

assert yokei("ゆるして\\nくれめんす") == "ゆるして\\nくれめんす"