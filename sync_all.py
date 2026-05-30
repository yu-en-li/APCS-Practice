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
ROOT_START, ROOT_END = "", ""
L1_START, L1_END = "", ""
L2_START, L2_END = "", ""


def update_l2_topic(path, sub_name):
    readme_path = os.path.join(path, "README.md")

    # 找出該目錄下所有的 C++ 和 Python 檔案（👉 已加入排除 tempCodeRunnerFile 的邏輯）
    files = (
        [
            f for f in os.listdir(path) 
            if f.endswith((".cpp", ".py")) and "tempCodeRunner" not in f
        ]
        if os.path.exists(path)
        else []
    )

    # 整理資料：{ 題目名稱: { "links": [], "title": "...", "complexity": "...", "tag": "...", "diff": "...", "notion": "..." } }
    data = {}
    for f in sorted(files):
        name = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1].lower()
        file_path = os.path.join(path, f)

        # --- 🚀 核心功能：自動解析多個 APCS 欄位 ---
        prob_title = name  # 預設用檔名
        complexity = "未標記"
        tag = "`未標記`"
        difficulty = "未標記"
        notion_url = "請在此處貼上連結"  # 預設的 Notion 連結

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

                    # 3. 抓取核心觀念（精準包覆程式碼方塊標籤）
                    tag_match = re.search(r"(?://|#)\s*APCS Tag:\s*(.*)", line)
                    if tag_match:
                        raw_tag = tag_match.group(1).strip()
                        tags = [
                            f"`{t.strip()}`" for t in raw_tag.split(",") if t.strip()
                        ]
                        tag = " ".join(tags) if tags else "`未標記`"

                    # 4. 抓取難度並轉換成完美對齊、帶空格的黑白星 (★ ☆ ☆ ☆ ☆)
                    diff_match = re.search(r"(?://|#)\s*APCS Difficulty:\s*(\d+)", line)
                    if diff_match:
                        star_count = int(diff_match.group(1).strip())
                        star_count = max(1, min(5, star_count))  # 限制在 1~5 星
                        stars = ["★"] * star_count + ["☆"] * (5 - star_count)
                        difficulty = " ".join(stars)

                    # 5. ✨ 新增：抓取 Notion 詳細筆記連結 ✨
                    notion_match = re.search(r"(?://|#)\s*APCS Note:\s*(https?://[^\s]+)", line)
                    if notion_match:
                        notion_url = notion_match.group(1).strip()

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
                "notion": notion_url,
            }

        data[name]["links"].append(link)

        # 如果複數檔案中（同時有 .cpp 和 .py）有某一版寫了註解，就蓋掉預設值
        if prob_title != name:
            data[name]["title"] = prob_title
        if complexity != "未標記":
            data[name]["complexity"] = complexity
        if tag != "`未標記`":
            data[name]["tag"] = tag
        if difficulty != "未標記":
            data[name]["difficulty"] = difficulty
        if notion_url != "請在此處貼上連結":
            data[name]["notion"] = notion_url

    # 完美對齊的 7 欄位大表頭
    table = ["| 題目名稱 | 程式連結 | 時間複雜度 | 詳細筆記 | 難度 | 核心觀念 | 狀態 |",
        "| :--- | :--- | :---: | :---: | :---: | :--- | :---: |",
    ]

    for name, info in data.items():
        link_str = " ".join(info["links"])
        status_icon = "✅ 已過關" if len(info["links"]) > 0 else "⏳ 挑戰中"

        # 這裡會自動帶入 info["notion"] 提取出來的網址
        table.append(
            f"| **{info['title']}** | {link_str} | {info['complexity']} | "
            f"[📝 Notion]({info['notion']}) | {info['difficulty']} | {info['tag']} | {status_icon} |"
        )

    table_content = "\n".join(table)

    # 精準地讀取、置換，絕對不破壞表格外的任何手寫筆記
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 檢查兩個標籤是否都存在
    if L2_START in content and L2_END in content:
        import re
        # 使用正則表達式，精準替換兩個標籤中間的內容
        pattern = f"{re.escape(L2_START)}.*?{re.escape(L2_END)}"
        replacement = f"{L2_START}\n{table_content}\n{L2_END}"
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # 只有當內容真的有變動時才寫入檔案，減少硬碟讀寫
        if new_content != content:
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    else:
        print(f"⚠️ 警告：{readme_path} 找不到完整的 L2 標籤，已自動跳過，保護你的筆記！")


def update_l1_chapter(path, cat_name):
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        return
    table = ["| 子主題 | 進度 | 完成率 | 狀態 |", "| :--- | :---: | :---: | :--- |"]
    for sub, target in CONFIG[cat_name]["subs"].items():
        sub_path = os.path.join(path, sub)
        # 👉 已加入排除 tempCodeRunnerFile 的邏輯，避免計數灌水
        count = (
            len([
                f for f in os.listdir(sub_path) 
                if f.endswith((".cpp", ".py")) and "tempCodeRunner" not in f
            ])
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
        # 👉 已加入排除 tempCodeRunnerFile 的邏輯，避免總進度灌水
        count = sum(
            len(
                [
                    f for f in os.listdir(os.path.join(cat, sub))
                    if f.endswith((".cpp", ".py")) and "tempCodeRunner" not in f
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