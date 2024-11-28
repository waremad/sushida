from yokei import yokei

#文字区切り
def sura(self):
    self = yokei(self)
    mini = ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ"]
    y = []

    if self == "":
        return [""]
    self = list(self)
    for i in range(len(self)):
        if self[i] in mini:
            y[-1] = y[-1] + self[i]
        else:
            if y == []:
                y.append(self[i])
            else:
                if (y[-1])[-1] == "っ" or (y[-1])[-1] == "\\":
                    y[-1] = y[-1] + self[i]
                else:
                    y.append(self[i])
    for i in range(len(y)):
        if y[i] == "\\n":
            y[i] = "\n"
    return y

assert sura("") == [""]
assert sura("てすと") == ["て","す","と"]
assert sura("あいあんまん") == ["あ","い","あ","ん","ま","ん"]
assert sura("しゃもじ") == ["しゃ","も","じ"]
assert sura("かーどりーだー") == ["か","ー","ど","り","ー","だ","ー"]
assert sura("かっとあんどしゃっふる") == ["か","っと","あ","ん","ど","しゃ","っふ","る"]
assert sura("きてぃさん") == ["き","てぃ","さ","ん"]

assert sura("てすと") == ["て","す","と"]
assert sura("てっど") == ["て","っど"]
assert sura("かーど") == ["か","ー","ど"]
assert sura("てっっど") == ["て","っど"]
assert sura("しゃゃいん") == ["しゃ","い","ん"]
assert sura("っしゃいん") == ["しゃ","い","ん"]
assert sura("っゃしゃいん") == ["しゃ","い","ん"]
assert sura("しゃいんっ") == ["しゃ","い","ん"]
assert sura("かれてゃ") == ["か","れ","てゃ"]
assert sura("（わら）") == ["（","わ","ら","）"]
assert sura("くれ\nめんす") == ["く","れ","\n","め","ん","す",]
assert sura("ゆるして\\nくれめんす") == ["ゆ","る","し","て","\n","く","れ","め","ん","す"]