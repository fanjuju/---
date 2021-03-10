'''供方开拓审核--待办理列表--办理'''
import config
class ApplyOpenProcess:
    def __init__(self):
        self.url = config.IP + "/api/v1/boot/common/front/process/completeBatch"
        self.pId = config.pId
        self.taskId = config.taskId

    def apply_open_process(self,session):
        data = [{
            "actType": "general",
            "pId": self.pId,
            "taskId": self.taskId,
            "userId": "204",
            "userName": "二二",
            "var": {
                "keys": "firstPass,firstBackReason",
                "values": "true,wwww",
                "types": "B,S"
            }
        }]
        resp_applyopenprocess = session.post(self.url,json = data)
        return resp_applyopenprocess
