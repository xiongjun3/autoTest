import pytest

if __name__ == '__main__':
    # 运行所有测试用例,并生成报告，报告路径./result/
    # pytest.main()中传入指令以执行测试用例
    pytest.main(["test_case.py", "-sv", "--clean-alluredir","--alluredir", "result"])
    browser = "chrome"
    domain = "https://dashboard.qa.axinan.com/"
    data = f"""
    browser={browser}
    domain={domain}
    """
    # 在./result/目录下创建一个environment.properties文件，将环境配置信息写入该文件中
    with open("result/environment.properties","w", encoding="utf-8") as f:
        f.write(data)