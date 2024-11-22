import os
import shutil
import re

# 原始資料夾的路徑
source_dir = "gaze_redirection-master/Columbia Gaze Data Set"
# 篩選後的目標資料夾
destination_dir = "/home/andy/AILab/AIfinal/gaze_redirection-master/train_eyes_patch"

# 確保目標資料夾存在，若不存在則建立
os.makedirs(destination_dir, exist_ok=True)

pattern = re.compile(r"(?<![-\d])0P(?![\d])")

# 遍歷原始資料夾中的所有子資料夾
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    # 確保遍歷的是資料夾
    if os.path.isdir(folder_path):
        # 遍歷該資料夾中的檔案
        for file_name in os.listdir(folder_path):
            # 檢查檔案名稱是否精確包含 "0P"
            if pattern.search(file_name):
                # 定義原始檔案和目標檔案的完整路徑
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_dir, file_name)
                # 複製檔案到目標資料夾
                shutil.copy2(source_file, destination_file)

print(f"所有包含 '0P' 的檔案已成功複製到：{destination_dir}")