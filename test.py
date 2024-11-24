import os
import shutil

# 設定 eyespatch_dataset 資料夾的路徑
dataset_path = "/home/andy/AILab/AIfinal/gaze_redirection-master/eyespatch_dataset"  # 替換成你的實際路徑
all_folder = os.path.join(dataset_path, "all")

# 創建新的資料夾 "all"
if not os.path.exists(all_folder):
    os.makedirs(all_folder)

# 取得子資料夾列表
subfolders = ["N30P", "N15P", "0P", "15P", "30P"]

# 複製每個子資料夾的內容到 "all" 資料夾
for subfolder in subfolders:
    subfolder_path = os.path.join(dataset_path, subfolder)
    if os.path.exists(subfolder_path):  # 確保子資料夾存在
        for file_name in os.listdir(subfolder_path):  # 遍歷子資料夾中的所有檔案
            src_file = os.path.join(subfolder_path, file_name)
            dest_file = os.path.join(all_folder, file_name)
            if os.path.isfile(src_file):  # 確保是檔案而非資料夾
                shutil.copy(src_file, dest_file)  # 複製檔案
            elif os.path.isdir(src_file):  # 若遇到子資料夾也可以選擇是否處理
                print(f"Skipping directory {src_file}")

print("All files copied to the 'all' folder.")

