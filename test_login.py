import pytest
import MainMenu
from Pages import LoginPage
from Util import db_helper as db


class TestMenu:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()

    def test_sign_in_valid_credentials(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["john", "Password123", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Welcome john!" in captured.out


    def test_sign_in_invalid_username(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["unknown", "password123", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return None (no user found)
        with mocker.patch.object(db, 'get_user', return_value=None):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "no user was found with the username unknown" in captured.out

    def test_sign_in_invalid_password(self, monkeypatch, capsys, mocker):
        # Mocking input to simulate user interaction
        inputs = ["john", "wrongpassword", "4"]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with different password
        user = ["john", "password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.login.sign_in()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "Invalid Password" in captured.out

