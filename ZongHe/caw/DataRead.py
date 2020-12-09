'''
文件读写
'''
import configparser
import os
import yaml


def get_project_path():
    # __file__存储当前文件路径
    path = os.path.realpath(__file__)
    # 上一级目录
    path = os.path.dirname(path)
    # 再上一级目录
    path = os.path.dirname(path)
    return path + "\\"


def read_ini(file_path, key):
    '''

    :param file_path: ini文件路径
    :param key:    要读取的key值
    :return:  key对应的value
    '''

    file_path = get_project_path() + file_path
    config = configparser.ConfigParser()
    config.read(file_path)  # 读文件
    # 通过key获取value, "env"是section,与ini中[env]对应
    value = config.get("env", key)
    return value


def read_yaml(file_path):
    file_path = get_project_path() + file_path
    with open(file_path, "r", encoding='utf-8') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        return content


if __name__ == '__main__':
    # 绝对路径:放在别的电脑可能不行   C:\ApiAutoTest\ZongHe\data_env\env.ini
    # 相对路径 C:\ApiAutoTest\ZongHe(去掉)
    a = read_ini(r"data_env\env.ini", "url")
    print(a)
    a = read_ini(r"data_env\env.ini", "db")
    print(a)
    a = read_yaml(r"data_case\register_fail.yaml")
    print(a)
    print(a[0])
