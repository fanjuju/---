import config
import yaml
import os



def read_yaml_data(yaml_path):
    '''读取yaml文件'''
    # 打开yaml文件，并执行读取操作    r:读 w:写 a:追加
    f = open(yaml_path,"r",encoding="utf-8")
    cfg = f.read()
    print(cfg)

    # 转换成python dict
    d = yaml.load(cfg)
    # print(d)   # 获取字典
    print(d["data_list"])   # 读取键（data_list）对应的值就是所需要的list数据
    return d

if __name__ == '__main__':

    # config.ABS_PATH  是调取config文件当前所在的文件夹路径
    yaml_path = os.path.join(config.ABS_PATH, "data\\test_data.yml")
    print(config.ABS_PATH)
    print(yaml_path)

    read_yaml_data(yaml_path)