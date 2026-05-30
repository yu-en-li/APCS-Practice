import os

# --- 設定區：直觀定義結構與目標 ---
CONFIG = {
    "01_Basic_Syntax": {
        "total": 15,
        "subs": {
            "01_IO_Optimization": 5,
            "02_Conditionals": 5,
            "03_Loops": 5,
            "04_Functions": 5,
        },
    },
    "02_Data_Structures": {
        "total": 25,
        "subs": {"01_Array": 5, "02_Vector": 5, "03_String": 5, "04_Struct": 5},
    },
    "03_Basic_Algorithms": {
        "total": 35,
        "subs": {
            "01_Sorting": 5,
            "02_Binary_Search": 5,
            "03_Greedy": 5,
            "04_Brute_Force": 5,
            "05_Two_Pointers": 5,
            "06_Math_Theory": 5,
        },
    },
    "04_Advanced_Topics": {
        "total": 25,
        "subs": {
            "01_Recursion": 4,
            "02_Stack_Queue": 4,
            "03_DFS": 4,
            "04_BFS": 4,
            "05_DP": 4,
            "06_Graph_Tree": 5,
        },
    },
}

# --- 標籤設定 ---
ROOT_START, ROOT_END = "<!-- ROOT_START -->", "<!-- ROOT_END -->"
L1_START, L1_END = "<!-- L1_START -->", "<!-- L1_END -->"
L2_START, L2_END = "<!-- L2_START -->", "<!-- L2_END -->"


def update_l2_topic(path, sub_name):
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        return

    files = [f for f in os.listdir(path) if f.endswith((".cpp", ".py"))]

    # 整理資料：{ 題目名稱: { "links": [], "title": "...", "complexity": "...", "tag": "...", "diff": "..." } }
    data = {}
    for f in sorted(files):
        name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1].lower()
        file_path = os.path.join(path, f)

        # --- 🚀 核心升級：自動解析多個 APCS 欄位 ---
        prob_title = name  # 預設用檔名
        complexity = "未標記"
        tag = "未標記"
        difficulty = "0"  # 預設 0 顆星

        try:
            with open(file_path, "r", encoding="utf-8") as file_obj:
                head = [file_obj.readline() for _ in range(15)]
                for line in head:
                    import re

                    # 1. 抓取題目名稱
                    title_match = re.search(r"(?://|#)\s*APCS Title:\s*(.*)", line)
                    if title_match:
                        prob_title = title_match.group(1).strip()

                    # 2. 抓取時間複雜度
                    comp_match = re.search(r"(?://|#)\s*APCS Complexity:\s*(.*)", line)
                    if comp_match:
                        val = comp_match.group(1).strip()
                        complexity = f"${val}$" if not val.startswith("$") else val

                    # 3. 抓取核心觀念
                    tag_match = re.search(r"(?://|#)\s*APCS Tag:\s*(.*)", line)
                    if tag_match:
                        tag = tag_match.group(1).strip()

                    # 4. 抓取難度並轉換
                    # 4. 抓取難度並轉換成完美對齊的黑白星
                    diff_match = re.search(r"(?://|#)\s*APCS Difficulty:\s*(\d+)", line)
                    if diff_match:
                        star_count = int(diff_match.group(1).strip())
                        # 限制在 1~5 顆星之間，多或少都會被修正
                        star_count = max(1, min(5, star_count))
                        difficulty = " ".join("★" * star_count + "☆" * (5 - star_count))
        except Exception as e:
            print(f"無法讀取 {f} 的標籤資料: {e}")
        # -------------------------------------------

        display_name = "C++" if ext == ".cpp" else "Py"
        link = f"[{display_name}](./{f})"

        if name not in data:
            data[name] = {
                "links": [],
                "title": prob_title,
                "complexity": complexity,
                "tag": tag,
                "difficulty": difficulty,
            }

        data[name]["links"].append(link)

        # 如果複數檔案中（同時有 .cpp 和 .py）有某一版寫了註解，就蓋掉預設值
        if prob_title != name:
            data[name]["title"] = prob_title
        if complexity != "未標記":
            data[name]["complexity"] = complexity
        if tag != "未標記":
            data[name]["tag"] = tag
        if difficulty != "0" and difficulty != "未標記":
            data[name]["difficulty"] = difficulty

    # 完美對齊你要求的欄位：題目名稱 | 程式連結 | 時間複雜度 | 詳細筆記 | 難度 | 核心觀念 | 狀態
    table = [
        "| 題目名稱 | 程式連結 | 時間複雜度 | 詳細筆記 | 難度 | 核心觀念 | 狀態 |",
        "| :--- | :--- | :---: | :---: | :---: | :--- | :---: |",
    ]

    for name, info in data.items():
        link_str = " ".join(info["links"])

        # 狀態欄（自動判定）：如果同時寫了 C++ 和 Python，或者只要有寫就亮綠燈
        status_icon = "✅ 已過關" if len(info["links"]) > 0 else "⏳ 挑戰中"

        table.append(
            f"| **{info['title']}** | {link_str} | {info['complexity']} | "
            f"[📝 Notion](請在此處貼上連結) | {info['difficulty']} | {info['tag']} | {status_icon} |"
        )

    table_content = "\n".join(table)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if L2_START in content:
        parts = content.split(L2_START)
        after_tag = parts[1].split(L2_END)[1]
        new_content = f"{parts[0]}{L2_START}\n{table_content}\n{L2_END}{after_tag}"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        return

    files = [f for f in os.listdir(path) if f.endswith((".cpp", ".py"))]

    # 整理資料：{ 題目名稱: { "links": [連結1], "complexity": "未標記" } }
    data = {}
    for f in sorted(files):
        name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1].lower()
        file_path = os.path.join(path, f)

        # --- 🚀 新增：自動解析程式碼內的複雜度註解 ---
        complexity = "未標記"
        try:
            with open(file_path, "r", encoding="utf-8") as file_obj:
                # 唯讀取前 15 行，避免大型檔案浪費時間
                head = [file_obj.readline() for _ in range(15)]
                for line in head:
                    # 支援 C++ 的 // 和 Python 的 # 註解格式
                    import re

                    comp_match = re.search(r"(?://|#)\s*APCS Complexity:\s*(.*)", line)
                    if comp_match:
                        complexity = comp_match.group(1).strip()
                        # 自動幫你加上 Markdown 的數學符號包圍，讓 GitHub 渲染更漂亮
                        if not complexity.startswith("$"):
                            complexity = f"${complexity}$"
        except Exception as e:
            print(f"無法讀取 {f} 的複雜度: {e}")
        # -------------------------------------------

        # 決定顯示名稱：.cpp -> C++, .py -> Py
        display_name = "C++" if ext == ".cpp" else "Py"
        link = f"[{display_name}](./{f})"

        if name not in data:
            data[name] = {"links": [], "complexity": complexity}

        data[name]["links"].append(link)
        # 如果其中一個檔案（例如 C++ 版）有寫複雜度，就蓋掉預設值
        if complexity != "未標記":
            data[name]["complexity"] = complexity

    # 修改表格標頭，加入「時間複雜度」欄位
    table = [
        "| 題目名稱 | 程式連結 | 時間複雜度 | 詳細筆記 | 難度 | 核心觀念 | 狀態 |",
        "| :--- | :--- | :---: | :---: | :---: | :--- | :---: |",
    ]

    for name, info in data.items():
        link_str = " ".join(info["links"])
        comp_str = info["complexity"]
        # 將複雜度填入第三個欄位，後續維持你原本的 Notion 欄位
        table.append(
            f"| **{name}** | {link_str} | {comp_str} | [📝 Notion](請在此處貼上連結) | | | |"
        )

    table_content = "\n".join(table)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if L2_START in content:
        parts = content.split(L2_START)
        after_tag = parts[1].split(L2_END)[1]
        new_content = f"{parts[0]}{L2_START}\n{table_content}\n{L2_END}{after_tag}"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        return

    files = [f for f in os.listdir(path) if f.endswith((".cpp", ".py"))]

    # 整理資料：{ 題目名稱: [連結1, 連結2] }
    data = {}
    for f in sorted(files):
        name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1].lower()

        # 決定顯示名稱：.cpp -> C++, .py -> Py
        display_name = "C++" if ext == ".cpp" else "Py"
        link = f"[{display_name}](./{f})"

        if name not in data:
            data[name] = []
        data[name].append(link)

    # 修改表格標頭，加入「詳細筆記」欄位
    table = [
        "| 題目名稱 | 程式連結 | 詳細筆記 | 難度 | 核心觀念 | 狀態 |",
        "| :--- | :--- | :---: | :---: | :--- | :---: |",
    ]

    for name, links in data.items():
        link_str = " ".join(links)
        # 這裡預留了 Notion 連結的欄位 (第三個欄位)
        # 你之後可以在這欄手動貼上你的 Notion 連結
        table.append(f"| **{name}** | {link_str} | [📝 Notion](請在此處貼上連結) | | | |")

    table_content = "\n".join(table)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if L2_START in content:
        parts = content.split(L2_START)
        # 確保保留標籤後的內容（例如您手動填寫過的表格資料）
        after_tag = parts[1].split(L2_END)[1]
        new_content = f"{parts[0]}{L2_START}\n{table_content}\n{L2_END}{after_tag}"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)


def update_l1_chapter(path, cat_name):
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        return
    table = ["| 子主題 | 進度 | 完成率 | 狀態 |", "| :--- | :---: | :---: | :--- |"]
    for sub, target in CONFIG[cat_name]["subs"].items():
        sub_path = os.path.join(path, sub)
        count = (
            len([f for f in os.listdir(sub_path) if f.endswith((".cpp", ".py"))])
            if os.path.exists(sub_path)
            else 0
        )
        pct = int((count / target) * 100) if target > 0 else 0
        table.append(
            f"| [{sub}](./{sub}/) | {count}/{target} | {pct}% | {'✅' if count >= target else '🔥'} |"
        )

    table_content = "\n".join(table)
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if L1_START in content:
        parts = content.split(L1_START)
        new_content = f"{parts[0]}{L1_START}\n{table_content}\n{L1_END}{parts[1].split(L1_END)[1]}"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)


def update_l0_root():
    readme_path = "README.md"
    table = ["| 階段大分類 | 完成度 | 完成率 |", "| :--- | :---: | :---: |"]
    for cat, info in CONFIG.items():
        count = sum(
            len(
                [
                    f
                    for f in os.listdir(os.path.join(cat, sub))
                    if f.endswith((".cpp", ".py"))
                ]
            )
            for sub in info["subs"]
            if os.path.exists(os.path.join(cat, sub))
        )
        pct = int((count / info["total"]) * 100) if info["total"] > 0 else 0
        table.append(f"| [{cat}](./{cat}/) | {count}/{info['total']} | {pct}% |")

    table_content = "\n".join(table)
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    if ROOT_START in content:
        parts = content.split(ROOT_START)
        new_content = f"{parts[0]}{ROOT_START}\n{table_content}\n{ROOT_END}{parts[1].split(ROOT_END)[1]}"
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)


if __name__ == "__main__":
    for cat, info in CONFIG.items():
        for sub in info["subs"]:
            update_l2_topic(os.path.join(cat, sub), sub)
        update_l1_chapter(cat, cat)
    update_l0_root()
    print("全站 README 同步完成！")
