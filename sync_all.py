import os

# --- 設定區：直觀定義結構與目標 ---
CONFIG = {
    "01_Basic_Syntax": {
        "total": 15,
        "subs": {"01_IO_Optimization": 5, "02_Conditionals": 5, "03_Loops": 5, "04_Functions": 5}
    },
    "02_Data_Structures": {
        "total": 25,
        "subs": {"01_Array": 5, "02_Vector": 5, "03_String": 5, "04_Struct": 5}
    },
    "03_Basic_Algorithms": {
        "total": 35,
        "subs": {"01_Sorting": 5, "02_Binary_Search": 5, "03_Greedy": 5, "04_Brute_Force": 5, "05_Two_Pointers": 5, "06_Math_Theory": 5}
    },
    "04_Advanced_Topics": {
        "total": 25,
        "subs": {"01_Recursion": 4, "02_Stack_Queue": 4, "03_DFS": 4, "04_BFS": 4, "05_DP": 4, "06_Graph_Tree": 5}
    }
}

# --- 標籤設定 ---
ROOT_START, ROOT_END = "<!-- ROOT_START -->", "<!-- ROOT_END -->"
L1_START, L1_END = "<!-- L1_START -->", "<!-- L1_END -->"
L2_START, L2_END = "<!-- L2_START -->", "<!-- L2_END -->"

def update_l2_topic(path, sub_name):
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path): return
    files = [f for f in os.listdir(path) if f.endswith(('.cpp', '.py'))]
    table = ["| 題目名稱 | 語言 | 連結 |", "| :--- | :---: | :--- |"]
    for f in sorted(files):
        table.append(f"| {os.path.splitext(f)[0]} | {os.path.splitext(f)[1][1:].upper()} | [連結](./{f}) |")
    
    table_content = "\n".join(table)
    with open(readme_path, "r", encoding="utf-8") as f: content = f.read()
    if L2_START in content:
        parts = content.split(L2_START)
        new_content = f"{parts[0]}{L2_START}\n{table_content}\n{L2_END}{parts[1].split(L2_END)[1]}"
        with open(readme_path, "w", encoding="utf-8") as f: f.write(new_content)

def update_l1_chapter(path, cat_name):
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path): return
    table = ["| 子主題 | 進度 | 完成率 | 狀態 |", "| :--- | :---: | :---: | :--- |"]
    for sub, target in CONFIG[cat_name]["subs"].items():
        sub_path = os.path.join(path, sub)
        count = len([f for f in os.listdir(sub_path) if f.endswith(('.cpp', '.py'))]) if os.path.exists(sub_path) else 0
        pct = int((count / target) * 100) if target > 0 else 0
        table.append(f"| [{sub}](./{sub}/) | {count}/{target} | {pct}% | {'✅' if count >= target else '🔥'} |")
    
    table_content = "\n".join(table)
    with open(readme_path, "r", encoding="utf-8") as f: content = f.read()
    if L1_START in content:
        parts = content.split(L1_START)
        new_content = f"{parts[0]}{L1_START}\n{table_content}\n{L1_END}{parts[1].split(L1_END)[1]}"
        with open(readme_path, "w", encoding="utf-8") as f: f.write(new_content)

def update_l0_root():
    readme_path = "README.md"
    table = ["| 階段大分類 | 完成度 | 完成率 |", "| :--- | :---: | :---: |"]
    for cat, info in CONFIG.items():
        count = sum(len([f for f in os.listdir(os.path.join(cat, sub)) if f.endswith(('.cpp', '.py'))]) 
                    for sub in info["subs"] if os.path.exists(os.path.join(cat, sub)))
        pct = int((count / info['total']) * 100) if info['total'] > 0 else 0
        table.append(f"| [{cat}](./{cat}/) | {count}/{info['total']} | {pct}% |")
    
    table_content = "\n".join(table)
    with open(readme_path, "r", encoding="utf-8") as f: content = f.read()
    if ROOT_START in content:
        parts = content.split(ROOT_START)
        new_content = f"{parts[0]}{ROOT_START}\n{table_content}\n{ROOT_END}{parts[1].split(ROOT_END)[1]}"
        with open(readme_path, "w", encoding="utf-8") as f: f.write(new_content)

if __name__ == "__main__":
    for cat, info in CONFIG.items():
        for sub in info["subs"]:
            update_l2_topic(os.path.join(cat, sub), sub)
        update_l1_chapter(cat, cat)
    update_l0_root()
    print("全站 README 同步完成！")