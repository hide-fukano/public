class User:
    """ Webサービス中の「ユーザー」を表すクラス

    first_name, last_name, email など、会員登録時のユーザーの情報を持っている。
    """
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def role(self):
        """ ユーザーの役割を文字列で返す。

        emailアドレスが会社のドメインで終わっていればスタッフ
        `'staff'` と判定する。
        一般ユーザーは `'viewer'` とする
        """
        if self.email.endswith('@my-company.com'):
            return 'staff'
        else:
            return 'viewer'
