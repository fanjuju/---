import requests
import allure
from api.myprocess.task import Task

@allure.feature("供方开拓待办理列表页面")
class TestTask:
    def setup_class(self):
        self.seesion = requests.Session()
        self.task = Task()

    @allure.story("供方开拓待办理列表")
    @allure.title("供方开拓待办理列表查看")
    def test_task(self):

        result = self.task.task(self.seesion)
        res = result.json()

        assert res['data']['subCode'] == 10000