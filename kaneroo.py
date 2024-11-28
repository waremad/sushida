from sura import sura
import copy

def kanaroo(self):

    dec12 = {
    'あ': ['a'], 'い': ['i'], 'う': ['u', 'wu'], 'え': ['e'], 'お': ['o'],
    'か': ['ka', 'ca'], 'き': ['ki'], 'く': ['ku', 'qu', 'cu'], 'け': ['ke'], 'こ': ['ko', 'co'],
    'さ': ['sa'], 'し': ['si', 'shi', 'ci'], 'す': ['su'], 'せ': ['se', 'ce'], 'そ': ['so'],
    'た': ['ta'], 'ち': ['ti', 'chi'], 'つ': ['tu', 'tsu'], 'て': ['te'], 'と': ['to'],
    'な': ['na'], 'に': ['ni'], 'ぬ': ['nu'], 'ね': ['ne'], 'の': ['no'],
    'は': ['ha'], 'ひ': ['hi'], 'ふ': ['hu', 'fu'], 'へ': ['he'], 'ほ': ['ho'],
    'ま': ['ma'], 'み': ['mi'], 'む': ['mu'], 'め': ['me'], 'も': ['mo'],
    'や': ['ya'], 'ゆ': ['yu'], 'よ': ['yo'],
    'ら': ['ra'], 'り': ['ri'], 'る': ['ru'], 'れ': ['re'], 'ろ': ['ro'],
    'わ': ['wa'], 'を': ['wo'], 'ん': ['n', 'nn','xn'],
    'が': ['ga'], 'ぎ': ['gi'], 'ぐ': ['gu'], 'げ': ['ge'], 'ご': ['go'],
    'ざ': ['za'], 'じ': ['zi', 'ji'], 'ず': ['zu'], 'ぜ': ['ze'], 'ぞ': ['zo'],
    'だ': ['da'], 'ぢ': ['di'], 'づ': ['du'], 'で': ['de'], 'ど': ['do'],
    'ば': ['ba'], 'び': ['bi'], 'ぶ': ['bu'], 'べ': ['be'], 'ぼ': ['bo'],
    'ぱ': ['pa'], 'ぴ': ['pi'], 'ぷ': ['pu'], 'ぺ': ['pe'], 'ぽ': ['po'],

    'きゃ': ['kya', 'kixya', 'kilya'], 'きぃ': ['kyi', 'kixi', 'klxi', 'kilyi', 'kixyi'], 'きゅ': ['kyu', 'kixyu', 'kilyu'], 'きぇ': ['kye', 'kixe', 'kile', 'kixye', 'kilye'], 'きょ': ['kyo', 'kixyo', 'kilyo'],
    'くぁ': ['qa', 'kuxa', 'kula', 'quxa', 'qula', 'cuxa', 'cula'], 'くぃ': ['qi', 'kuxi', 'kuli', 'quxi', 'quli', 'cuxi', 'culi', 'kuxyi', 'kulyi', 'quxyi', 'qulyi', 'cuxyi', 'culyi'], 'くぅ': ['kwu', 'kuxu', 'kulu', 'quxu', 'qulu', 'cuxu', 'culu'], 'くぇ': ['qe', 'kuxe', 'kule', 'quxe', 'qule', 'cuxe', 'cule', 'kuxye', 'kulye', 'quxye', 'qulye', 'cuxye', 'culye'], 'くぉ': ['qo', 'kuxo', 'kulo', 'quxo', 'qulo', 'cuxo', 'culo'],
    'ぎゃ': ['gya', 'gixya', 'gilya'], 'ぎぃ': ['gyi', 'gixyi', 'gixi', 'gilyi', 'gili'], 'ぎゅ': ['gyu', 'gixyu', 'gilyu'], 'ぎぇ': ['gye', 'gixye', 'gixe', 'gilye', 'gile'], 'ぎょ': ['gyo', 'gixyo', 'gilyo'],
    'ぐぁ': ['gwa', 'guxa', 'gula'], 'ぐぃ': ['gwi', 'guxi', 'guxyi', 'guli', 'gulyi'], 'ぐぅ': ['gwu', 'guxu', 'gulu'], 'ぐぇ': ['gwe', 'guxye', 'guxe', 'gulye', 'gule'], 'ぐぉ': ['gwo', 'guxo', 'gulo'],
    'しゃ': ['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'], 'しぃ': ['syi', 'sixi', 'sili', 'cixi', 'cili', 'sixyi', 'shixi', 'silyi', 'shili', 'cixyi', 'cilyi', 'shixyi', 'shilyi'], 'しゅ': ['syu', 'shu', 'sixyu', 'silyu', 'cixyu', 'cilyu', 'shilyu', 'shixyu'], 'しぇ': ['sye', 'she', 'sixye', 'shixye', 'sixe', 'shixe', 'silye', 'shilye', 'sile', 'shile', 'cixye', 'cixe', 'cilye', 'cile'], 'しょ': ['syo', 'sho', 'sixyo', 'shixyo', 'silyo', 'shilyo', 'cixyo', 'cilyo'],
    'すぁ': ['swa', 'suxa', 'sula'], 'すぃ': ['swi', 'suxi', 'suxyi', 'suli', 'sulyi'], 'すぅ': ['swu', 'suxu', 'sulu'], 'すぇ': ['swe', 'suxye', 'suxe', 'sulye', 'sule'], 'すぉ': ['swo', 'suxo', 'sulo'],
    'じゃ': ['zya', 'ja', 'jya', 'zixya', 'jixya', 'zilya', 'jilya'], 'じぃ': ['zyi', 'zixyi', 'jixyi', 'zixi', 'jixi', 'zilyi', 'jilyi', 'zili', 'jili'], 'じゅ': ['zyu', 'ju', 'jyu', 'zixyu', 'jixyu', 'zilyu', 'jilyu'], 'じぇ': ['zye', 'je', 'zixye', 'jixye', 'zixe', 'jixe', 'zilye', 'jilye', 'zile', 'jile'], 'じょ': ['zyo', 'jo', 'jyo', 'zixyo', 'jixyo', 'zilyo', 'jilyo'],
    'ちゃ': ['tya', 'cha', 'cya', 'tixya', 'chixya', 'tilya', 'chilya'], 'ちぃ': ['tyi', 'tixi', 'tili', 'tixyi', 'chixi', 'tilyi', 'chili', 'chilyi', 'chixyi'], 'ちゅ': ['tyu', 'chu', 'tixyu', 'chixyu', 'tilyu', 'chilyu'], 'ちぇ': ['tye', 'che', 'tixye', 'chixye', 'tixe', 'chixe', 'tilye', 'chilye', 'tile', 'chile'], 'ちょ': ['tyo', 'cho', 'tixyo', 'chixyo', 'tilyo', 'chilyo'],
    'てゃ': ['tha', 'texya', 'telya'], 'てぃ': ['thi', 'texyi', 'texi', 'telyi', 'teli'], 'てゅ': ['thu', 'texyu', 'telyu'], 'てぇ': ['the', 'texye', 'texe', 'telye', 'tele'], 'てょ': ['tho', 'texyo', 'telyo'],
    'とぁ': ['twa', 'toxa', 'tola'], 'とぃ': ['twi', 'toxi', 'toxyi', 'toli', 'tolyi'], 'とぅ': ['twu', 'toxu', 'tolu'], 'とぇ': ['twe', 'toxye', 'toxe', 'tolye', 'tole'], 'とぉ': ['two', 'toxo', 'tolo'],
    'ぢゃ': ['dya', 'dixya'], 'ぢぃ': ['dyi', 'dixyi', 'dixi', 'dilyi', 'dili'], 'ぢゅ': ['dyu', 'dixyu', 'dilyu'], 'ぢぇ': ['dye', 'dixye', 'dixe', 'dilye', 'dile'], 'ぢょ': ['dyo', 'dixyo', 'dilyo'],
    'でゃ': ['dha', 'dexya', 'delya'], 'でぃ': ['dhi', 'dexi', 'deli', 'dexyi', 'delyi'], 'でゅ': ['dhu', 'dexyu', 'delyu'], 'でぇ': ['dhe', 'dexye', 'dexe', 'delye', 'dele'], 'でょ': ['dho', 'dexyo', 'delyo'],
    'どぁ': ['dwa', 'doxa', 'dola'], 'どぃ': ['dwi', 'doxi', 'doli', 'doxyi', 'dolyi'], 'どぅ': ['dwu', 'doxu', 'dolu'], 'どぇ': ['dwe', 'doxye', 'doxe', 'dolye', 'dole'], 'どぉ': ['dwo', 'doxo', 'dolo'],
    'にゃ': ['nya', 'nixya', 'nilya'], 'にぃ': ['nyi', 'nixyi', 'nixi', 'nilyi', 'nili'], 'にゅ': ['nyu', 'nixyu', 'nilyu'], 'にぇ': ['nye', 'nixye', 'nixe', 'nilye', 'nile'], 'にょ': ['nyo', 'nixyo', 'nilyo'],
    'ひゃ': ['hya', 'hixya', 'hilya'], 'ひぃ': ['hyi', 'hixyi', 'hixi', 'hilyi', 'hili'], 'ひゅ': ['hyu', 'hixyu', 'hilyu'], 'ひぇ': ['hye', 'hixye', 'hixe', 'hilye', 'hile'], 'ひょ': ['hyo', 'hixyo', 'hilyo'],
    'ふぁ': ['fa', 'fuxa', 'huxa', 'fula', 'hula'], 'ふぃ': ['fi', 'fuxi', 'huxi', 'fuxyi', 'huxyi', 'fuli', 'huli', 'fulyi', 'hulyi'], 'ふぅ': ['fwu', 'fuxu', 'huxu', 'fulu', 'hulu'], 'ふぇ': ['fe', 'fuxe', "huxe", 'fuxye', "huxye", 'fule', "hule", 'fulye', "hulye"], 'ふぉ': ['fo', 'fuxo', 'huxo', 'fulo', 'hulo'],
    'びゃ': ['bya', 'bixya', 'bilya'], 'びぃ': ['byi', 'bixyi', 'bixi', 'bilyi', 'bili'], 'びゅ': ['byu', 'bixyu', 'bilyu'], 'びぇ': ['bye', 'bixye', 'bixe', 'bilye', 'bile'], 'びょ': ['byo', 'bixyo', 'bilyo'],
    'ぴゃ': ['pya', 'pixya', 'pilya'], 'ぴぃ': ['pyi', 'pixyi', 'pixi', 'pilyi', 'pili'], 'ぴゅ': ['pyu', 'pixyu', 'pilyu'], 'ぴぇ': ['pye', 'pixye', 'pixe', 'pilye', 'pile'], 'ぴょ': ['pyo', 'pixyo', 'pilyo'],
    'みゃ': ['mya', 'pixya', 'pilya'], 'みぃ': ['myi', 'mixyi', 'mixi', 'milyi', 'mili'], 'みゅ': ['myu', 'mixyu', 'milyu'], 'みぇ': ['mye', 'mixye', 'mixe', 'milye', 'mile'], 'みょ': ['myo', 'mixyo', 'milyo'],
    'りゃ': ['rya', 'rixya', 'rilya'], 'りぃ': ['ryi', 'rixyi', 'rixi', 'rilyi', 'rili'], 'りゅ': ['ryu', 'rixyu', 'rilyu'], 'りぇ': ['rye', 'rixye', 'rixe', 'rilye', 'rile'], 'りょ': ['ryo', 'rixyo', 'rilyo'],
    'うぁ': ['wha', 'uxa', 'ula', 'wuxa', 'wula'], 'うぃ': ['wi', 'uxi', 'uxyi', 'uli', 'ulyi', 'wuxi', 'wuxyi', 'wuli', 'wulyi'], 'うぇ': ['we', 'uxe', 'uxye', 'ule', 'ulye', 'wuxe', 'wuxye', 'wule', 'wulye'], 'うぉ': ['who', 'uxo', 'ulo', 'wuxo', 'wulo'],
    'ゔぁ':['va', 'vuxa', 'vula'], 'ゔぃ':['vi', 'vuxi', 'vuxyi', 'vuli', 'vulyi'], 'ゔ':['vu'], 'ゔぇ':['ve', 'vuxe', 'vuxye', 'vule', 'vulye'], 'ゔぉ':['vo', 'vuxo', 'vulo'],
    'ゔゃ':['vya', 'vuxya', 'vulya'], 'ゔゅ':['vyu', 'vuxyu', 'vulyu'], 'ゔょ':['vyo', 'vuxyo', 'vulyo'],
    'ふゃ': ['fya', 'huxya', 'hilya', 'fuxya', 'filya'], 'ふゅ': ['fyu', 'huxyu', 'hulyu', 'fuxyu', 'fulyu'], 'ふょ': ['fyo', 'huxyo', 'hulyo', 'fuxyo', 'fulyo'],
    'くゃ': ['qya', 'kuxya', 'kulya', 'quxya', 'qulya', 'cuxya', 'culya'], 'くゅ': ['qyu', 'kuxyu', 'kulyu', 'quxyu', 'qulyu', 'cuxyu', 'culyu'], 'くょ': ['qyo', 'kuxyo', 'kulyo', 'quxyo', 'qulyo', 'cuxyo', 'culyo'],

    "ゃ":["xya","lya"],"ゅ":["xyu","lyu"],"ょ":["xyo","lyo"],
    "ぁ":["xa","la"],"ぃ":["xi","li","xyi","lyi"],"ぅ":["xu","lu"],"ぇ":["xe","le", "xye","lye"],"ぉ":["xo","lo"],
    "っ":["xtu","xtsu","ltu","ltsu"],"ゎ":["xwa","lwa"],"ゕ":["xka","lka"],"ゖ":["xke","lke"],

    "！": ["!"], "”": ["\""], "＃": ["#"], "＄": ["$"], "％": ["%"], "＆": ["&"], "’": ["\'"], "（": ["("], "）": [")"],
    "１": ["1"], "２": ["2"], "３": ["3"], "４": ["4"], "５": ["5"], "６": ["6"], "７": ["7"], "８": ["8"], "９": ["9"], "０": ["0"],
    "＝": ["="], "～": ["~"], "｜": ["|"],
    "ー": ["-"], "＾": ["^"], "￥": ["\\"],
    "‘": ["`"], "｛": ["{"],
    "＠": ["@"], "「": ["["],
    "＋": ["+"], "＊": ["*"], "｝": ["}"],
    "；": [";"], "：": [":"], "」": ["]"],
    "＜": ["<"], "＞": [">"], "？": ["?"], "＿": ["_"],
    "、": [","], "。": ["."], "・": ["/"], "￥": ["\\"]
    }
#wuう quく　fuふ　c　かしくせこ
#fyoふょ cya ちゃ　qyaくゃ

    decany = {}

    self = sura(self)
#    print(self)
    if self == [""]:
        return [[""]]
    y = []
    for i in self:
#        print(i)
        inp = []
        ing = i
        if i[0] == "っ":
            ing = ing[1:]
        if ing in list(dec12.keys()):
            inp = copy.copy(dec12[ing])
        else:
            if len(ing) == 1:
                inp = copy.copy([ing])
            elif len(ing) == 2:
                if ing[0] in dec12:
                    tt = dec12[ing[0]]
                    for j in tt:
                        for k in dec12[ing[1]]:
                            inp.append(j + k)
                else:
                    inp = copy.copy([ing])
            else:
                print("???kanaroo???")
#        print(i,i[0] == "っ")
        if i[0] == "っ":
            for j in range(len(inp)):
#                print(inp,j)
                inp.append("xtu" + inp[j])
                inp[j] = inp[j][0] + inp[j]
#        print(inp)
        y.append(inp)
#        print(y)
#    print(y)
    return y

assert kanaroo("") == [[""]]
assert kanaroo("てすと") == [["te"],["su"],["to"]]
assert kanaroo("あいあんまん") == [["a"],["i"],["a"],['n','nn','xn'],["ma"],['n','nn','xn']]
assert kanaroo("しゃもじ") == [['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'],["mo"],["zi","ji"]]
assert kanaroo("かーどりーだー") == [["ka", "ca"],["-"],["do"],["ri"],["-"],["da"],["-"]]
assert kanaroo("かっとあんどしゃっふる") == [["ka", "ca"],["tto", "xtuto"],["a"],['n','nn','xn'],["do"],['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'],["hhu","ffu","xtuhu","xtufu"],["ru"],]
assert kanaroo("きてぃさん") == [['ki'], ['thi', 'texyi', 'texi', 'telyi', 'teli'], ['sa'], ['n','nn', 'xn']]

assert kanaroo("てすと") == [["te"],["su"],["to"]]
assert kanaroo("てっど") == [["te"],["ddo","xtudo"]]
assert kanaroo("かーど") == [["ka","ca"],["-"],["do"]]
assert kanaroo("てっっど") == [["te"],["ddo","xtudo"]]
assert kanaroo("しゃゃいん") == [['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'],["i"],['n','nn','xn'],]
assert kanaroo("っしゃいん") == [['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'],["i"],['n','nn','xn'],]
assert kanaroo("っゃしゃいん") == [['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'],["i"],['n','nn','xn'],]
assert kanaroo("しゃいんっ") == [['sya', 'sha', 'sixya', 'silya', 'cixya', 'cilya', 'shilya', 'shixya'],["i"],['n','nn','xn'],]
assert kanaroo("かれてゃ") == [['ka', 'ca'], ['re'], ['tha', 'texya', 'telya']]
assert kanaroo("かれくゃ") == [['ka', 'ca'], ['re'], ['qya', 'kuxya', 'kulya', 'quxya', 'qulya', 'cuxya', 'culya']]
assert kanaroo("（わら）") == [["("],["wa"],["ra"],[")"],]
assert kanaroo("Androidすまーとふぉん") == [['A'], ['n'], ['d'], ['r'], ['o'], ['i'], ['d'], 
                       ['su'], ['ma'], ['-'], ['to'], ['fo', 'fuxo', 'huxo', 'fulo', 'hulo'], ['n','nn','xn']]
assert kanaroo("かべやてん") == [['ka', 'ca'], ['be'], ['ya'], ['te'], ['n', 'nn', 'xn']]
#print(kanaroo("じゅうじのつめをくいこませてかべやてんじょうをはいまわっていた。"))
assert kanaroo("しぉ") == [['sixo', 'silo', 'shixo', 'shilo', 'cixo', 'cilo']]
assert kanaroo("くれ\nめんす") == [['ku', 'qu', 'cu'], ['re'], ['\n'], ['me'], ['n', 'nn', 'xn'], ['su']]
assert kanaroo("ゆるして\nくれめんす") == [['yu'], ['ru'], ['si', 'shi', 'ci'], ['te'], ['\n'], ['ku', 'qu', 'cu'], ['re'], ['me'], ['n', 'nn', 'xn'], ['su']]
assert kanaroo("ゆるして\\nくれめんす") == [['yu'], ['ru'], ['si', 'shi', 'ci'], ['te'], ['\n'], ['ku', 'qu', 'cu'], ['re'], ['me'], ['n', 'nn', 'xn'], ['su']]
assert kanaroo("\\") == [["\\"]]
assert kanaroo(" \\ ") == [[" "],["\\ "]]
assert kanaroo("・・・ーーー・・・") == [["/"],["/"],["/"],["-"],["-"],["-"],["/"],["/"],["/"],]
