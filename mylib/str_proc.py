def char_n_gram(target, n):
    """文字列を文字n_gramにより分割する
    Args:
        target (str): 分割対象の文字列
        n (int): 区切り幅（文字）
    Retuns:s
        n_gram (str list): n文字ずつ区切られた文字列のリスト
    """
    return [ target[i:i+n] for i in range(len(target) - n + 1) ]

def word_n_gram(target, n):
    """文字列を単語n_gramにより分割する
    Args:
        target (str): 分割対象の文字列
        n (int): 区切り幅（単語）
    Retuns:
        n_gram (str list): n単語ずつ区切られた文字列のリスト
    """
    target = target.split()
    return [ target[i:i+n] for i in range(len(target) - n + 1) ]