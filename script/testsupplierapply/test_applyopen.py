# encode = 'utf-8'
import config
import pytest
import requests
import allure
from api.supplierapply.applyOpen import ApplyOpen
from tools.read_yml import read_yaml_data
import os

# data_list = [
#     ["", "测试供应商A", "备注信息"],
#     [32, "", "备注信息"],
#     [32, "测试供应商A", ""]
# ]


# ids = ["缺少物料类型","缺少供应商名称","缺少备注信息"]


@allure.feature("供应商引入列表功能")
class TestApplyOpen:

    def setup_class(self):
        self.session = requests.Session()
        self.applyopen = ApplyOpen()

    # @allure.story("供应商引入_新增")
    # @allure.title("供应商新增成功")
    # def test_apply_success(self):
    #     '''实现的功能：供应商引入模块中新增一个供应商'''
    #     result_apply = self.applyopen.apply_open_success(self.session)
    #     # res = result_apply.json()
    #     # print(res)
    #     assert result_apply.json()['data']['subCode'] == 10000

    # @allure.story("供应商引入_新增")
    # @allure.title("供应商新增失败")
    # def test_apply_fail_01(self):
    #     '''实现的功能：供应商新增时，未填写供应商名称，新增失败'''
    #     resp_apply = self.applyopen.apply_open_fail_01(self.session)
    #     assert resp_apply.json()["data"]["subCode"] == 400
    #     assert resp_apply.json()["data"]["success"] == False
    #     assert "试验厂家不能为空" in resp_apply.json()["data"]["subMsg"]
    #
    # @allure.story("供应商引入_新增")
    # @allure.title("供应商新增失败")
    # def test_apply_fail_02(self):
    #     '''实现的功能：供应商新增时，未填写引入原料，新增失败'''
    #     resp_apply = self.applyopen.apply_open_fail_02(self.session)
    #     assert resp_apply.json()["data"]["subCode"] == 400
    #     assert resp_apply.json()["data"]["success"] == False
    #     assert "试验原料不能为空" in resp_apply.json()["data"]["subMsg"]

    # 第一种：
    # cur_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print(cur_path)
    # yaml_path = os.path.join(os.path.dirname(cur_path), "data\\test_data.yml")
    # data_list = read_yaml_data(yaml_path)["data_list"]

    data_list = [
        ["", "测试供应商A", "备注信息"],
        [32, "", "备注信息"],
        [32, "测试供应商A", ""]
    ]

    @allure.story("供应商引入_新增")
    @allure.title("供应商新增失败")
    @pytest.mark.parametrize("materialId,supName,remark", data_list)
    def test_apply_fail(self,materialId,supName,remark):
        json = {
            "id": "",
            "type": 1,
            "materialId": materialId,
            "orgName": "柯桥基地",
            "orgId": 32,
            "applyUserId": "2090",
            "applyUserName": "测试甲",
            "applyTime": "2021-01-26",
            "supName": supName,
            "remark": remark,
            "suggest": "22",
            "importApplyOpenId": "",
            "userId": config.userId,
            "userName": config.userName
        }
        resp_apply = self.session.post(self.applyopen.url, json=json)
        assert resp_apply.json()["data"]["subCode"] == 400
        assert resp_apply.json()["data"]["success"] == False

# 第二种：多个请求参数
    data_list = [
        [{"materialId":"","supName": "测试供应商A", "remark":"备注信息"},{"subCode":400,"success":False}],
        [{"materialId":32,"supName": "", "remark":"备注信息"},{"subCode":400,"success":False}],
        [{"materialId":32,"supName": "测试供应商A", "remark":""},{"subCode":400,"success":False}]
    ]

    @allure.story("供应商引入_新增")
    @allure.title("供应商新增失败")
    @pytest.mark.parametrize("input_result,expect", data_list)
    def test_apply_fail(self,input_result,expect):
        json = {
            "id": "",
            "type": 1,
            "materialId": input_result["materialId"],
            "orgName": "柯桥基地",
            "orgId": 32,
            "applyUserId": "2090",
            "applyUserName": "测试甲",
            "applyTime": "2021-01-26",
            "supName": input_result["supName"],
            "remark": input_result["remark"],
            "suggest": "22",
            "importApplyOpenId": "",
            "userId": config.userId,
            "userName": config.userName
        }
        resp_apply = self.session.post(self.applyopen.url, json=json)
        assert resp_apply.json()["data"]["subCode"] == expect["subCode"]
        assert resp_apply.json()["data"]["success"] == expect["success"]

if __name__ == '__main__':
    pytest.main(["test_applyopen.py"])