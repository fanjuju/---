import pytest
import requests
import allure
from api.supplierapply.supImportList import SuplmportList

@allure.feature("供应商引入列表查看")
class TestSuplmportList:
    def setup_class(self):
        self.session = requests.Session()
        self.suplmportlist = SuplmportList()

    @allure.story("供应商引入列表")
    @allure.title("供应商引入列表")
    @pytest.mark.parametrize("mateTestStatus",[1,2,3,4,5])
    @pytest.mark.parametrize("certificationStatus", [1, 2, 3, 4])
    def test_suplmport_list(self,certificationStatus,mateTestStatus):

        resp_list = self.suplmportlist.suplmport_list(self.session,certificationStatus,mateTestStatus)
        resp = resp_list.json()
        # print(resp)
        assert resp['data']['success'] == True
