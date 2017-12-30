"""
test_ で始めるpythonファイルにテストを書く
unittest.TestCase を継承したクラスを作る
クラスの各メソッドは def test_ で始めて、その中で動作確認する
確認には self.assertEqual を使って、期待した値と比較する

確認する流れは以下です

前提の用意。データの作成
テスト対象 converter 関数の呼び出し
返り値や、他に変更された値が正しいか確認
「入力 => テスト対象 => 出力」
つまり「テスト対象の入出力」が何であるかを常に意識してテストを書く

"""

# コードテストを行うモジュール"unittest"をインポート
import unittest


"""
converter.pyからlist_to_dictという関数を呼び出す
"""
from converter import list_to_dict


class TestListToDict(unittest.TestCase):
    # テストメソッド一つ目
    def test__default_key(self):
        """
        デフォルトの、idの値をキーにする場合
        idの数値をもとに、期待した値を比較する
        """
        actual = list_to_dict(
            [{'id': 1, 'name': 'ロッシ'},
             {'id': 2, 'name': 'マルケス'},
             {'id': 3, 'name': 'ロレンソ'}],
        )
        self.assertEqual(actual, {
            1: {'id': 1, 'name': 'ロッシ'},
            2: {'id': 2, 'name': 'マルケス'},
            3: {'id': 3, 'name': 'ロレンソ'},
        })
        """
        idが1のactualには、id=1, name=ロッシが入っているか

        """

    def test__with_key(self):
        """
        key ="code"を指定して、codeの値をキーにする場合
        """
        actual = list_to_dict(
            [{'code': 'Val', 'name': 'ロッシ'},
             {'code': 'Mar', 'name': 'マルケス'},
             {'code': 'Lor', 'name': 'ロレンソ'}],
            key='code'
        )
        self.assertEqual(actual, {
            'Val': {'code': 'Val', 'name': 'ロッシ'},
            'Mar': {'code': 'Mar', 'name': 'マルケス'},
            'Lor': {'code': 'Lor', 'name': 'ロレンソ'},
        })

    def test__duplicate_key(self):
        """
        keyに重複がある場合
        """
        actual = list_to_dict(
            [{'id': 1, 'name': 'ロッシ'},
             {'id': 2, 'name': 'マルケス'},
             {'id': 2, 'name': 'ロレンソ'}],
        )
        self.assertEqual(actual, {
            1: {'id': 1, 'name': 'ロッシ'},
            2: {'id': 2, 'name': 'ロレンソ'},
        })


















        
