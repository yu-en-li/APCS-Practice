# 🚀 Dual-Engine Coding Journey: C++ & Python Lab

### 🧑‍💻 關於我
- **學校 / 年級：** 高中一年級
- **學習目標：** 希望於高中期間累積資訊學習歷程，挑戰 **APCS 觀念 3 級分 / 實作 3 級分以上**，並為大學資工/相關科系申請奠定基礎。
- **目前進度：** 基礎語法與演算法練習（持續更新中）

---

## 🛠️ 開發環境與工具
為了模擬 APCS 考場環境並建立高效率的刷題習慣，我配置了以下開發環境：
- **編輯器 (Editor):** Visual Studio Code (VS Code)
- **編編譯器 (Compiler):** MinGW-w64 (g++ 15.2.0, UCRT64 環境)
- **自動化工具:** Code Runner (設定於內建 Terminal 執行互動測資)
- **程式碼託管:** GitHub (記錄每日 Contribution 綠色牆)

---


## 📊 程式解題進度與知識地圖

這個對照表全面紀錄了我的刷題軌跡。整體開發**以 C++ 作為核心實作語言**以鍛鍊底層運作邏輯；並在課堂要求或特定演算法驗證時，搭配 **Python 進行雙軌練習**。

### 📂 01. 基礎語法練習 (Basic Syntax)
*對應 Notion：【語法】系列（I/O 處理、條件判斷 `if-else`、重複迴圈 `for/while`、自訂函式）*

| 題號 | 題目名稱 | 困難度 | 關鍵知識點 | 狀態 | 實作紀錄 | 題目 | 筆記 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| a010 | 質因數分解 | 🟡 進階 | `迴圈優化` | ✅ | 💻 [C++] | [ZJ]([連結](https://zerojudge.tw/ShowProblem?problemid=a010)) | [Notion](連結) |
| b002 | 簡易運算 | 🟢 基礎 | `條件判斷` | ✅ | 🐍 [Py] | [ZJ](連結) | [Notion](連結) |

<br>

### 📂 02. 資料結構基礎 (Data Structures)
*對應 Notion：【資料】系列（多維陣列、動態陣列 `vector`、字串處理 `string`、結構體 `struct`、物件導向 `OOP`）*

| 題號 / 題目名稱 | 核心觀念 | 程式碼連結 | 解題反思 / 關鍵點 |
| :--- | :--- | :--- | :--- |
| 範例題目 | 資料｜動態陣列 (vector) | [C++](./02_Data_Structures/) | 尚未開始挑戰 |

<br>

### 📂 03. 基礎演算法 (Basic Algorithms)
*對應 Notion：【算法】系列（內建排序 `sort`、二分搜尋、雙指標、暴力列舉、數學與數論）*

| 題號 / 題目名稱 | 核心觀念 | 程式碼連結 | 解題反思 / 關鍵點 |
| :--- | :--- | :--- | :--- |
| 範例題目 | 算法｜二分搜尋 | [C++](./03_Basic_Algorithms/) | 尚未開始挑戰 |

<br>

### 📂 04. 高階與進階專題 (Advanced Topics)
*對應 Notion：【高階】系列（遞迴 `Recursion`、堆疊與佇列 `Stack/Queue`、貪心演算法 `Greedy` 等 APCS 觀念）*

| 題號 / 題目名稱 | 核心觀念 | 程式碼連結 | 解題反思 / 關鍵點 |
| :--- | :--- | :--- | :--- |
| 範例題目 | 高階｜遞迴 (Recursion) | [C++](./04_Advanced_Topics/) | 尚未開始挑戰 |

<br>

### 📂 05. 位元與數論 (Math & Theory)
*對應 Notion：【語法｜位元運算 (Bitwise)】與【算法｜數學與數論】進階主題*

| 題號 / 題目名稱 | 核心觀念 | 程式碼連結 | 解題反思 / 關鍵點 |
| :--- | :--- | :--- | :--- |
| 範例題目 | 語法｜位元運算 (Bitwise) | [C++](./05_Math_and_Theory/) | 尚未開始挑戰 |

---

💡 *作戰紀律：每完成一題，我會分批 Commit 程式實作檔案，並同步更新此對照表與 Notion 任務中心，確保知識完全內化。*

## 📝 刷題常用：高效 C++ 模板
在解題時，為了避免大量資料輸入輸出導致 TLE (Time Limit Exceeded)，我設定了標準的 Snippet 加速範本：

```cpp
#include <iostream>
using namespace std;

int main() {
    // 關閉輸入輸出流同步，加速 cin/cout 效率
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    
    
    return 0;
}
