'''供方开拓审核-待办理列表'''
import config
from tools.getlogger import GetLog

log = GetLog().get_logger()
class Task:
    def __init__(self):
        self.url = config.IP + "/api/v1/boot/act/list/task"

    def task(self,session):
        data = {
            "actType": "general",
            "project": "buy",
            "processTypeId": config.materialType,
            "page": 1,
            "size": 10,
            "materialType": "",
            "materialId": "",
            "keyword": config.supName,
            "userId": "204",
            "userName": "二二"
        }
        result = session.post(self.url, json =data)
        res = result.json()
        name = res['data']['result']['records'][0]['name']
        print(name)
        config.pId = res['data']['result']['records'][0]['processInstanceId']
        config.taskId = res['data']['result']['records'][0]['task']['id']
        log.info("供应商名称是：{0},pId的值是：{1}，taskId的值是：{2}".format(name,config.pId,config.taskId))

        return result