'''开拓申请--新增'''
import pytest
from faker import Faker
import config
from tools.getlogger import GetLog

log = GetLog().get_logger()
fake = Faker(locale="zh_CN")

class ApplyOpen:
    def __init__(self):
        self.url = config.IP + "/api/v1/boot/common/supplier/applyOpen"

    def apply_open_success(self,session):
        json = {
            "id": "",
            "type": 1,
            "materialId": 4,
            "orgName": "柯桥基地",
            "orgId": 32,
            "applyUserId": "2090",
            "applyUserName": "测试甲",
            "applyTime": "2021-01-26",
            "supName": fake.name(),
            "remark": "8888",
            "suggest": "22",
            "importApplyOpenId": "",
            "userId": config.userId,
            "userName": config.userName
        }
        resp_apply= session.post(self.url,json = json)
        # log.info("请求的参数是：{0}".format(json))
        # log.info("请求的参数是：{0}".format(json['remark']))
        return resp_apply


    # def apply_open_fail_01(self,session):
    #     json = {
    #         "id": "",
    #         "type": 1,
    #         "materialId": 4,
    #         "orgName": "柯桥基地",
    #         "orgId": 32,
    #         "applyUserId": "2090",
    #         "applyUserName": "测试甲",
    #         "applyTime": "2021-01-26",
    #         "supName":"",
    #         "remark": "8888",
    #         "suggest": "22",
    #         "importApplyOpenId": "",
    #         "userId": config.userId,
    #         "userName": config.userName
    #     }
    #     resp_apply = session.post(self.url,json = json)
    #     log.info("请求的参数是：{0}".format(json))
    #     return resp_apply
    #
    # def apply_open_fail_02(self, session):
    #     json = {
    #         "id": "",
    #         "type": 1,
    #         "materialId": "",
    #         "orgName": "柯桥基地",
    #         "orgId": 32,
    #         "applyUserId": "2090",
    #         "applyUserName": "测试甲",
    #         "applyTime": "2021-01-26",
    #         "supName": "供应商BBC",
    #         "remark": "8888",
    #         "suggest": "22",
    #         "importApplyOpenId": "",
    #         "userId": config.userId,
    #         "userName": config.userName
    #     }
    #     resp_apply = session.post(self.url, json=json)
    #     log.info("请求的参数是：{0}".format(json))
    #     return resp_apply



    # def apply_open_fail(self,session,materialId,supName,remark):
    #     json = {
    #         "id": "",
    #         "type": 1,
    #         "materialId": materialId,
    #         "orgName": "柯桥基地",
    #         "orgId": 32,
    #         "applyUserId": "2090",
    #         "applyUserName": "测试甲",
    #         "applyTime": "2021-01-26",
    #         "supName": supName,
    #         "remark": remark,
    #         "suggest": "22",
    #         "importApplyOpenId": "",
    #         "userId": config.userId,
    #         "userName": config.userName
    #     }
    #     resp_apply= session.post(self.url,json = json)
    #     # log.info("请求的参数是：{0}".format(json))
    #     # log.info("请求的参数是：{0}".format(json['remark']))
    #     return resp_apply