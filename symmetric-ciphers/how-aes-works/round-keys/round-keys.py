def bytes2matrix(text):
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    result = []
    for row in matrix:
        for i in range(len(row)):
            result.append(row[i])
    return result

def add_round_key(s, k):
    assert len(s) == len(k)
    
    result = []
    for i in range(len(s)):
        result.append([])
        assert len(s[i]) == len(k[i])
        row_s = s[i]
        row_k = k[i]
        for j in range(len(row_s)):
            result[i].append(row_s[j] ^ row_k[j])
    return result
    
state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

print(bytes(matrix2bytes(add_round_key(state, round_key))).decode('utf-8'))