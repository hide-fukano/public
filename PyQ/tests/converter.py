def list_to_dict(data, key='id'):
    """
    辞書のリストを、辞書に変換する関数。
    辞書のリスト data を受け取り、各辞書の `"id"` キーの値を
    キーにした新しい辞書を返す。

    キーにする値は key 引数で変更できる (デフォルトで `"id"`)

    >>> list_to_dict([{'id': 1, 'name': 'name1'},
    ...               {'id': 2, 'name': 'name2'}], key='id')
    {1: {'id': 1, 'name': 'name1'}, 2: {'id': 2, 'name': 'name2'}}

    ファイルやRDBから読み込んだデータ(辞書のリストで取れる場合が多い)を、
    ID値やコードでアクセスしやすくするために使います。

    >>> data = list_to_dict([{...}, ...])
    >>> data[12]  # IDが12番のデータを取得
    """
    ret = {}
    for row in data:
        ret[row[key]] = row
    return ret
