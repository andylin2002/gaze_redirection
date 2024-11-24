import os

# eyespatch 資料夾的路徑

subfolder_path = '/home/andy/AILab/AIfinal/gaze_redirection-master/eyespatch_dataset/30P'
    
# 遍歷子資料夾中的所有檔案
for filename in os.listdir(subfolder_path):
    # 檢查檔案是否以 "left" 或 "right" 開頭
    if filename.startswith("left_") or filename.startswith("right_"):
        # 分離檔案名稱和副檔名
        name_parts = filename.split("_")
        prefix = name_parts[0]
        rest = "_".join(name_parts[1:])  # 取得剩餘部分
        
        # 根據檔案開頭選擇新後綴
        if prefix == "left":
            new_name = rest.replace(".jpg", "_L.jpg")
        elif prefix == "right":
            new_name = rest.replace(".jpg", "_R.jpg")
        else:
            continue  # 如果不是 left 或 right，跳過
        
        # 完整的舊路徑和新路徑
        old_path = os.path.join(subfolder_path, filename)
        new_path = os.path.join(subfolder_path, new_name)
        
        # 重新命名檔案
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

print("Renaming completed!")
