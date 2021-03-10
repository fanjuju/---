'''供应商引入列表'''
import config
class SuplmportList:
    def __init__(self):
        self.url = config.IP + 'api/v1/boot/common/supplier/supImportList'

    def suplmport_list(self,session,certificationStatus,materialId):
        json = {
            "type": 1,
            "page": 1,
            "size": 10,
            "materialType": "",
            "materialId": materialId,
            "supName": "",
            "certificationStatus":certificationStatus,
            "mateTestStatus": "",
            "inspectStatus": "",
            "userId": "2090",
            "userName": "测试甲"
        }
        list_data = session.post(self.url,json = json)
        return list_data

