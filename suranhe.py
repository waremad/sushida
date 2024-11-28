from sura import sura

def suranhe(self):
    if self == "":
        return ""
    self = sura(self)
    self = "".join(self)
    return self

assert suranhe("") == ""
assert suranhe("ゆるして\\nくれめんす") == "ゆるして\nくれめんす"