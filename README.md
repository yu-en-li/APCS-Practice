# 🚀 Dual-Engine Coding Journey: C++ & Python Lab

工作面板：[![Notion]([https://img.shields.io/badge/Notion-WorkSpace-000000?style=flat-square&logo=notion&logoColor=white](https://www.notion.so/36a43be958cd80528db4df429506892f?v=36a43be958cd8075b3ac000c2c628f5d&source=copy_link))](#) 
APCS 目標：`觀念 3+ 級分` / `實作 3+ 級分` 🎯

---

## 🧑‍💻 關於我 (About Me)

- **學歷背景**：高中一年級
- **核心目標**：於高中期間累積完整的資訊自主學習歷程，挑戰 **APCS 雙 3 級分以上**，並為大學資訊工程及相關學系申請奠定紮實的演算法與實作基礎。
- **目前進度**：基礎語法鞏固、初階資料結構與基礎演算法練習（持續高頻更新中 🔥）。

### 🛠️ 技能樹與開發工具 (Skills & Tools)

![C++](https://img.shields.io/badge/C++-17/20-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-1.x-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)
![Git](https://img.shields.io/badge/Git-Pro-F05032?style=flat-square&logo=git&logoColor=white)

為了完美模擬 APCS 考場環境並建立高效率的刷題習慣，我配置了以下本地開發環境：
- **編輯器 (Editor)**：Visual Studio Code (VS Code)
- **編譯器 (Compiler)**：MinGW-w64 (`g++ 15.2.0`, UCRT64 環境)
- **自動化工具**：Code Runner (設定於內建 Terminal 執行互動測資)
- **版本控制**：Git / GitHub (嚴格執行每日 Contribution 綠色牆紀錄)

---

## 📊 程式解題進度與核心里程碑 (Milestones)

本 Repo 採用**層級式管理**。本主頁僅收錄挑戰性較高之 **APCS 歷屆實作題** 與 **進階演算法精選（核心重點題）**；其餘基礎與一般主題之完整練習題庫，請點擊下方導覽連結至各分類資料夾查看。

### 📌 核心戰力：精選重點題與 APCS 歷屆試題 (Featured Highlights)

> 💡 *當你挑戰成功 APCS 歷屆試題或高階演算法題時，光榮地將它們登錄在下方表格中吧！*

| 挑戰年份/來源 | 題目名稱 (連結) | 實作語言 | 關鍵反思與演算法優化 (教授必看點) | 知識點 Tags |
| :---: | :--- | :---: | :--- | :--- |
| *範例* | *[ZJ c575 基地台](#)* | *`C++`* | *運用二分搜尋逼近最小半徑，並以 $O(N)$ 貪婪法驗證，總複雜度 $O(N \log R)$* | *二分搜尋、貪婪* |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

### 🗂️ 完整知識地圖與分類題庫導覽 (Repository Navigation)

想查看更多一般練習題目實作與詳細 Notion 筆記，請點擊以下分類目錄進入查看：

* 📂 [01. 基礎語法練習 (Basic Syntax)](./01_Basic_Syntax/) — `0 題已完成` ｜ I/O 優化、條件判斷、進階迴圈、自訂函式
* 📂 [02. 資料結構基礎 (Data Structures)](./02_Data_Structures/) — `0 題已完成` ｜ 多維陣列、`std::vector`、字串處理、結構體應用
* 📂 [03. 基礎演算法 (Basic Algorithms)](./03_Algorithms/) — `0 題已完成` ｜ 二分搜尋、雙指標、基礎數論、內建排序
* 📂 [04. 高階與進階專題 (Advanced Topics)](./04_Advanced_Topics/) — `規劃中` ｜ 遞迴、DFS/BFS、貪心演算法、中階資料結構
* 📂 [05. 位元與數論 (Math & Theory)](./05_Math_Theory/) — `規劃中` ｜ 位元運算 (Bitwise)、狀態壓縮、質數篩法

*(進度文字與題數皆可隨著你的實作進度自由修改)*

---

## 💡 作戰紀律 (Coding Workflow)

每完成一題解題，我會嚴格執行以下工作流，確保知識完全內化：
1. **分批 Commit**：依據功能與重構分批提交程式實作檔案（遵循基本 Conventional Commits 規範）。
2. **同步對照表**：更新此 README 核心里程碑或分類資料夾內的題庫表格。
3. **內化至 Notion**：於 Notion 任務中心撰寫詳細筆記（包含解題思維、TLE/WA 踩雷紀錄與時間複雜度分析）。

---

## 📝 刷題常用：高效 C++ 模板 (C++ Template)

在解題時，為了避免大量資料輸入輸出導致 **TLE (Time Limit Exceeded)**，我設定了標準的 Snippet 加速範本：

```cpp
#include <iostream>

using namespace std;

int main() {
    // 關閉輸入輸出流同步，優化 cin/cout 效率，使其接近 scanf/printf
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    
    
    return 0;
}
