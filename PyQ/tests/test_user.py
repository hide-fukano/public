import unittest

from user import User


class TestUser(unittest.TestCase):
    def test_fullname(self):
        # 前提となるデータの用意
        """
        DBには苗字、名前、メールアドレスが入っているが、fullnameは苗字と名前のデータのみ
        必要としている
        """
        user = User('Hiroki', 'Kiyohara', '')
        actual = user.fullname()
        # actualの次には、比較する正解例を入れる
        self.assertEqual(actual, "Hiroki Kiyohara")

    # スタッフかどうかを判別できているかテスト
    def test_role_staff(self):
        user = User('', '', 'hiroki@my-company.com')
        actual = user.role()
        self.assertEqual(actual, 'staff')

    def test_role_viewer(self):
        user = User('', '', 'hiroki@other-company.com')
        actual = user.role()
        self.assertEqual(actual, 'viewer')
