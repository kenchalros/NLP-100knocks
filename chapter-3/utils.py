import gzip
import json

def extract_UK():
    """イギリスに関する記事を取得する
    Args:
    Returns:
        イギリスに関する記事を持つ辞書配列
    """
    contents = {}
    index = 0
    with gzip.open('jawiki-country.json.gz', 'rt') as jf:
        for line in jf:
            data = json.loads(line)
            if 'イギリス' in data['title']:
                contents[index] = data['text']
                index += 1
    return contents
