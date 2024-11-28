def readtxt(filename='odai.txt'):
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            row = line.strip().split(',')  # カンマで行を分割
            result.append(row)  # 分割した結果をリストに追加
#    print(result)
    result = dict(result)
    return result


#print(readtxt())