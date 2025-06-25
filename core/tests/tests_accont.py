from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Account

class AccountModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste_user', password='123456')
        self.account = Account.objects.create(user=self.user, account_number='12345', balance=1000.00, theme='dark')

    def test_criacao_conta(self):
        self.assertEqual(self.account.user.username, 'teste_user')
        self.assertEqual(self.account.account_number, '12345')
        self.assertEqual(self.account.balance, 1000.00)
        self.assertEqual(self.account.theme, 'dark')

    def test_str_representacao(self):
        self.assertEqual(str(self.account), 'teste_user - 12345')
