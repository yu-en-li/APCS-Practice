import os
import datetime

# 設定路徑與錨點
BASE_DIR = os.getcwd()
README_PATH = os.path.join(BASE_DIR, "README.md")
START_TAG = "<!-- PROGRESS_START -->"
END_TAG = "<!-- PROGRESS_END -->"

CATEGORIES = {
    "01": {"name": "01_Basic_Syntax", "total": 15},
    "02": {"name": "02_Data_Structures", "total": 25},
    "03": {"name": "03_Basic_Algorithms", "total": 35},
    "04": {"name": "04_Advanced_Topics", "total": 25}
}

CAT_INFO = {
    "01": "I/O, if-else, for/while, function",
    "02": "Array, Vector, String, Struct",
    "03": "Sort, Binary Search, Greedy, BF, Two Pointers, Math",
    "04": "Recursion, Stack/Queue, DFS, BFS, DP, Graph & Tree"
}

def count_unique_problems():
    counts = {}
    for key, info in CATEGORIES.items():
        root_folder = os.path.join(BASE_DIR, info["name"])
        unique_problems = set()
        if os.path.exists(root_folder):
            for dirpath, dirnames, filenames in os.walk(root_folder):
                for f in filenames:
                    if f.endswith(('.cpp', '.py')):
                        problem_id = f.split('_')[0]
                        unique_problems.add(problem_id)
        counts[key] = len(unique_problems)
    return counts

def get_latest_update(folder_name):
    folder_path = os.path.join(BASE_DIR, folder_name)
    mtimes = []
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.endswith(('.cpp', '.py')):
                mtimes.append(os.path.getmtime(os.path.join(root, f)))
    return datetime.datetime.fromtimestamp(max(mtimes)).strftime('%Y-%m-%d') if mtimes else "N/A"

def update_readme():
    counts = count_unique_problems()
    
    # 整合連結與進度的新表格
    table_rows = ["| 階段大分類 | 核心主題 | 進度 (題數) | 完成率 | 最近更新 | 目前狀態 |",
                  "| :--- | :--- | :---: | :---: | :---: | :---: |"]
    
    total_done = 0
    total_all = 0
    
    for key, info in CATEGORIES.items():
        d = counts[key]
        t = info["total"]
        total_done += d
        total_all += t
        
        last_update = get_latest_update(info["name"])
        percent = int((d / t) * 100) if t > 0 else 0
        status = "🔥 進行中" if 0 < d < t else ("✅ 完成" if d >= t else "⚪ 未開始")
        
        # 核心：直接將分類名稱變成連結
        folder_link = f"[**{info['name']}**](./{info['name']}/)"
        
        table_rows.append(f"| {folder_link} | {CAT_INFO[key]} | {d}/{t} | {percent}% | {last_update} | {status} |")

    total_percent = int((total_done / total_all) * 100) if total_all > 0 else 0
    table_rows.append(f"| **總計 (Total)** | **全題庫** | **{total_done}/{total_all}** | **{total_percent}%** | - | **🔥 進行中** |")
    
    new_table = "\n".join(table_rows)

    with open(README_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_content = []
    in_tag = False
    
    for line in lines:
        if START_TAG in line:
            new_content.append(line)
            new_content.append(new_table + "\n")
            in_tag = True
            continue
        if END_TAG in line:
            new_content.append(line)
            in_tag = False
            continue
        if not in_tag:
            # 刪除舊的「知識體系結構」區塊 (如果你有舊的錨點或標題要刪，可在這裡過濾)
            if "## 🏗️ 知識體系結構" not in line:
                new_content.append(line)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_content)
    
    print("成功：表格已整合導航連結並更新！")

if __name__ == "__main__":
    update_readme()