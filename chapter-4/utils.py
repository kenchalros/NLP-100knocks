def summarize_mecab(mecab_src):
    mecab_result = []
    with open(mecab_src, mode='r') as f:
        # 余分なEOSの削除
        els = [ s for s in f.readlines() if s != 'EOS\n' ]
        for mecab_line in els:
            el = mecab_line.split('\t')
            surface = el[0]
            base = el[2]
            # 品詞再分類の切り分け
            # 再分類がない場合ば空文字をセット
            el_pos = el[3].split('-')
            if len(el_pos) == 1:
                pos = el_pos[0]
                pos1 = ''
            else:
                pos = el_pos[0]
                pos1 = el_pos[1]
            obj = {
                'surface': surface,
                'base': base,
                'pos': pos,
                'pos1': pos1,
            }
            mecab_result.append(obj)
    return mecab_result