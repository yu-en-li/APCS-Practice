import os
import json

# 設定路徑與錨點
BASE_DIR = os.getcwd()
README_PATH = os.path.join(BASE_DIR, "README.md")
START_TAG = "<!-- PROGRESS_START -->"
END_TAG = "<!-- PROGRESS_END -->"

# 你的目錄配置與目標題數
CATEGORIES = {
    "01": {"name": "01_Basic_Syntax", "total": 15},
    "02": {"name": "02_Data_Structures", "total": 25},
    "03": {"name": "03_Basic_Algorithms", "total": 35},
    "04": {"name": "04_Advanced_Topics", "total": 25}
}

def generate_progress_bar(done, total):
    percent = int((done / total) * 100) if total > 0 else 0
    filled = int(percent / 10)
    bar = "█" * filled + "░" * (10 - filled)
    return f"`{bar} {percent}%`"

def count_unique_problems():
    counts = {}
    for key, info in CATEGORIES.items():
        root_folder = os.path.join(BASE_DIR, info["name"])
        unique_problems = set()
        
        if os.path.exists(root_folder):
            # os.walk 遞迴掃描所有子資料夾
            for dirpath, dirnames, filenames in os.walk(root_folder):
                for f in filenames:
                    # 統計 .cpp 或 .py
                    if f.endswith(('.cpp', '.py')):
                        # 以檔名主體作為識別，確保同一題的不同副檔名只算一次
                        # 使用 split('_')[0] 可以確保 a001_hello 與 a001_test 視為同一題
                        problem_id = f.split('_')[0] 
                        unique_problems.add(problem_id)
        
        counts[key] = len(unique_problems)
    return counts

def update_readme():
    counts = count_unique_problems()
    
    # 動態組裝表格
    table_rows = ["| 階段大分類 | 核心主題 | 已解題數 / 目標題數 | 學習進度條 | 目前狀態 |",
                  "| :--- | :--- | :---: | :--- | :---: |"]
    
    total_done = 0
    total_all = 0
    
    # 填入各分類資料
    cat_info = {
        "01": "I/O, if-else, for/while, function",
        "02": "Array, Vector, String, Struct",
        "03": "Sort, Binary Search, Greedy, Brute Force, Two Pointers, Math",
        "04": "Recursion, Stack/Queue, DFS, BFS, DP, Graph & Tree"
    }
    
    for key, info in CATEGORIES.items():
        d = counts[key]
        t = info["total"]
        total_done += d
        total_all += t
        status = "🔥 進行中" if 0 < d < t else ("✅ 完成" if d >= t else "⚪ 未開始")
        bar = generate_progress_bar(d, t)
        table_rows.append(f"| {info['name']} | {cat_info[key]} | `{d} / {t}` | {bar} | {status} |")

    total_bar = generate_progress_bar(total_done, total_all)
    table_rows.append(f"| **總計 (Total)** | **全題庫** | **{total_done} / {total_all}** | {total_bar} | **🔥 進行中** |")
    
    new_table = "\n".join(table_rows)

    # 讀取並更新 README
    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_content = []
    in_tag = False
    found_start = False

    for line in lines:
        if START_TAG in line:
            new_content.append(line)
            new_content.append(new_table + "\n")
            found_start = True
            in_tag = True
            continue
        if END_TAG in line:
            new_content.append(line)
            in_tag = False
            continue
        if not in_tag:
            new_content.append(line)

    if not found_start:
        print("錯誤：找不到錨點，請確保 README.md 內有 <!-- PROGRESS_START --> 與 <!-- PROGRESS_END -->")
        return

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_content)
    
    print("成功：進度表格已自動統計並更新！")

if __name__ == "__main__":
    update_readme()