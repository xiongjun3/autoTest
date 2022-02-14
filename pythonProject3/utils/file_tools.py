import os.path
import yaml


class FileTool:
    # 类方法，可以不用实例化，而直接调用该方法
    @classmethod
    def get_interface_dir(cls):
        # os.path.abspath(__file__) 获取当前文件的绝对路径
        # os.path.dirname 获取当前文件或者目录所在的目录
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def read_yaml(cls,file_name):
        # 获取
        _path = FileTool.get_interface_dir()
        # os.sep.join()根据文件名拼装出来当前文件夹的绝对路径
        yaml_file = os.sep.join([_path,"data",file_name + ".yaml"])
        with open(yaml_file, encoding="utf-8") as f:
            # 使用yaml把文件流转换成python对象返回回去
            return yaml.safe_load(f)


if __name__ == "__main__":
    print(FileTool.read_yaml("secrets"))
