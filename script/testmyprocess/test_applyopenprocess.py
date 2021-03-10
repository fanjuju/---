import requests
import allure

from api.myprocess.applyOpenProcess import ApplyOpenProcess

@allure.feature("开拓审核待办理列表功能")
class TestOpenProcess:
    def setup_class(self):
        self.seesion = requests.Session()
        self.applyopenprocess = ApplyOpenProcess()

    @allure.story("开拓审核待办理列表_点击办理")
    @allure.title("开拓审核办理成功")
    def test_apply_open_process(self):
        '''实现的功能：供应商引入的供应商进行开拓审核'''
        result_applyopenprocess = self.applyopenprocess.apply_open_process(self.seesion)
        res = result_applyopenprocess.json()
        # print(res)
        assert "成功" in  res['data']['subMsg']