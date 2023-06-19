import pytest
import MainMenu
from Pages import LoginPage
from Pages.Useful import BrowseInCollegePage as Browse, DirectoriesPage as Directory, GeneralPage as General, BusinessSolutionsPage as Business

from Util import db_helper as db


class TestUsefulLinks:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Setup code executed before each test
        self.menu = MainMenu.MainMenu()
        self.login = LoginPage.Login()

    def test_navigation_browse_in_college(self, monkeypatch, capsys, mocker):
        inputs = [22, 14]
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))

        # Mocking the get_user method to return a user with matching credentials
        user = ["john", "Password123"]
        with mocker.patch.object(db, 'get_user', return_value=user):
            self.menu.main_menu_options()

        # Capturing printed output and asserting expected result
        captured = capsys.readouterr()
        assert "under construction" in captured.out