# 单页查询应用

备注：`Excel` 表格的查询已通过测试

## 运行(Windows)

1. 在文件夹中打开 `powershell`(ps)，做法为打开此文件夹，将路径清空后输入 powershell，然后回车，即可打开

2. 输入命令：`.venv/bin/Activate.ps1`，回车

3. 随后，输入命令 `pip install -r requirements.txt` 安装环境（注意，只有第一次运行时需要运行这一步，后续可以直接跳过这一步）

4. 最后，输入命令 `python app.py`，然后在浏览器中访问 `localhost:8080` 即可

## 用法

将需要读取的文件（`.xlsx` 或 `.dbf`）文件放入 `data` 文件夹中，然后重新启动应用即可（参照上方的运行，重新启动一遍 `app.py` 即可）


