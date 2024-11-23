import os
import shutil
import re

# 原始資料夾的路徑
source_dir = "/home/andy/AILab/AIfinal/gaze_redirection-master/face_dataset"
# 篩選後的目標資料夾
destination_dirN30P = "/home/andy/AILab/AIfinal/gaze_redirection-master/train_eyes_patch/N30P"
destination_dirN15P = "/home/andy/AILab/AIfinal/gaze_redirection-master/train_eyes_patch/N15P"
destination_dir0P = "/home/andy/AILab/AIfinal/gaze_redirection-master/train_eyes_patch/0P"
destination_dir15P = "/home/andy/AILab/AIfinal/gaze_redirection-master/train_eyes_patch/15P"
destination_dir30P = "/home/andy/AILab/AIfinal/gaze_redirection-master/train_eyes_patch/30P"

# 確保目標資料夾存在，若不存在則建立
os.makedirs(destination_dirN30P, exist_ok=True)
os.makedirs(destination_dirN15P, exist_ok=True)
os.makedirs(destination_dir0P, exist_ok=True)
os.makedirs(destination_dir15P, exist_ok=True)
os.makedirs(destination_dir30P, exist_ok=True)

patternN30P = re.compile(r"(?<![-\d])-30P(?![\d])")
patternN15P = re.compile(r"(?<![-\d])-15P(?![\d])")
pattern0P = re.compile(r"(?<![-\d])0P(?![\d])")
pattern15P = re.compile(r"(?<![-\d])15P(?![\d])")
pattern30P = re.compile(r"(?<![-\d])30P(?![\d])")

# 遍歷原始資料夾中的所有子資料夾
for folder_name in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder_name)
    # 確保遍歷的是資料夾
    if os.path.isdir(folder_path):
        # 遍歷該資料夾中的檔案
        for file_name in os.listdir(folder_path):
            # 檢查檔案名稱是否精確包含 "0P"
            if patternN30P.search(file_name):
                # 定義原始檔案和目標檔案的完整路徑
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_dirN30P, file_name)
                # 複製檔案到目標資料夾
                shutil.copy2(source_file, destination_file)
            
            elif patternN15P.search(file_name):
                # 定義原始檔案和目標檔案的完整路徑
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_dirN15P, file_name)
                # 複製檔案到目標資料夾
                shutil.copy2(source_file, destination_file)

            elif pattern0P.search(file_name):
                # 定義原始檔案和目標檔案的完整路徑
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_dir0P, file_name)
                # 複製檔案到目標資料夾
                shutil.copy2(source_file, destination_file)

            elif pattern15P.search(file_name):
                # 定義原始檔案和目標檔案的完整路徑
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_dir15P, file_name)
                # 複製檔案到目標資料夾
                shutil.copy2(source_file, destination_file)

            elif pattern30P.search(file_name):
                # 定義原始檔案和目標檔案的完整路徑
                source_file = os.path.join(folder_path, file_name)
                destination_file = os.path.join(destination_dir30P, file_name)
                # 複製檔案到目標資料夾
                shutil.copy2(source_file, destination_file)

print("successfully classified")