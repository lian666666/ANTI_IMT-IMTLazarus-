import os

# 重命名文件
file_path = r"C:\\IMTWin\\IMTWin.exe"
new_path = os.path.splitext(file_path)[0] + ".txt"
os.rename(file_path, new_path)

# 创建目录
dir_path = "C:\\ANTI_IMT"
if not os.path.exists(dir_path):
    os.mkdir(dir_path)

# 创建并写入批处理文件
bat_file_path = os.path.join(dir_path, "ANTI_IMT.bat")
with open(bat_file_path, "w") as f:
    f.write('del C:\\IMTWin\\IMTWin.txt & REG DELETE "HKCU\\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v "ANTIIMT" /f')

# 添加到注册表
reg_key = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
reg_cmd = r'reg add "{}" /v ANTIIMT /t REG_SZ /d "{}" /f'.format(reg_key, bat_file_path)
os.system(reg_cmd)

# 重启计算机
os.system("shutdown -r -t 5")