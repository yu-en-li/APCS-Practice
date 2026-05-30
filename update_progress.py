import os

# --- 設定路徑 ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(BASE_DIR, "README.md")

# --- 定義標籤 ---
START_TAG = "``"
END_TAG = "``"

def count_solved(folder_name):
    folder_path = os.path.join(BASE_DIR, folder_name)
    solved_ids = set()
    if os.path.exists(folder_path):
        for root, dirs, files in os.walk(folder_path):
            # 忽略系統與設定資料夾
            dirs[:] = [d for d in dirs if d not in ['.git', '.vscode', '.venv', '__pycache__']]
            for file in files:
                if file.endswith(('.cpp', '.py')):
                    solved_ids.add(file.split('_')[0])
    return len(solved_ids)

def generate_bar(solved, target):
    percent = int((solved / target) * 100) if target > 0 else 0
    filled = percent // 10
    bar = "█" * filled + "░" * (10 - filled)
    return f"`{bar} {percent}%`"

def update():
    # 準備新表格數據
    CATEGORIES = {
        "01_Basic_Syntax": {"name": "01 基礎語法", "topics": "I/O, 判斷式, 迴圈, 函式", "target": 15},
        "02_Data_Structures": {"name": "02 資料結構", "topics": "Array, Vector, String, Struct", "target": 20},
        "03_Basic_Algorithms": {"name": "03 基礎演算法", "topics": "排序, 二分搜, 貪心, 數論", "target": 35},
        "04_Advanced_Topics": {"name": "04 進階主題", "topics": "遞迴, Stack/Queue, DFS, DP", "target": 25}
    }
    
    # 建立新表格的文字內容
    lines = ["| 階段大分類 | 核心主題 | 已解題數 / 目標題數 | 學習進度條 | 目前狀態 |",
             "| :--- | :--- | :---: | :--- | :---: |"]
    total_s, total_t = 0, 0
    for k, v in CATEGORIES.items():
        s = count_solved(k)
        total_s += s; total_t += v['target']
        status = "🟢 已達標" if s >= v['target'] else ("🟢 進行中" if s > 0 else "⚪ 未開始")
        lines.append(f"| {v['name']} | {v['topics']} | `{s} / {v['target']}` | {generate_bar(s, v['target'])} | {status} |")
    lines.append(f"| **總計 (Total)** | **全題庫** | **{total_s} / {total_t}** | {generate_bar(total_s, total_t)} | **🔥 進行中** |")
    
    new_table = "\n" + "\n".join(lines) + "\n"

    # --- 關鍵替換邏輯 ---
    with open(README_PATH, "r", encoding="utf-8") as f:
        old_lines = f.readlines()
    
    final_lines = []
    in_block = False 
    found_start = False
    
    for line in old_lines:
        if START_TAG in line:
            final_lines.append(line)
            final_lines.append(new_table) # 寫入新表格
            in_block = True               # 開啟過濾模式
            found_start = True
        elif END_TAG in line:
            final_lines.append(line)      # 寫入結束標籤
            in_block = False              # 關閉過濾模式，恢復正常寫入
        elif not in_block:
            # 只有當我們不在表格區塊內時，才保留原本 README 的內容
            final_lines.append(line)
            
    if not found_start:
        print("❌ 錯誤：找不到 ，請先確認 README.md 內容。")
        return

    # 寫回檔案
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(final_lines)
    print("✅ 更新成功：已替換舊內容並寫入最新進度。")

if __name__ == "__main__":
    update()