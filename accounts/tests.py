from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create your tests here.
class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_login(self):
        # ログインページを開く
        self.selenium.get("http://localhost:8000" + reverse_lazy("account_login"))

        # メールアドレスランの入力
        username_input = self.selenium.find_element(By.NAME, "login")
        username_input.send_keys("utaka0705@gmail.com")

        # パスワード欄の入力
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys("edano19990705")

        # ログインボタンのクリック
        button = self.selenium.find_element(By.XPATH, '//*[@id="wrapper"]/div/div/div/form/button')
        button.click()

        # 指定秒数待機（ページ遷移のため）
        time.sleep(3)

        # ページタイトルの検証
        self.assertEqual("日記一覧|Private Diary", self.selenium.title)