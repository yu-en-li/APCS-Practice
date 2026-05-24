# 🚀 High School C++ & APCS Coding Journey

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

## 📈 刷題進度與解題清單

### 📋 基礎語法練習 (ZeroJudge / 自訂題目)
| 題號 / 題目名稱 | 核心觀念 | 程式碼連結 | 解題反思 / 關鍵點 |
| :--- | :--- | :--- | :--- |
| **a001. 哈囉** | 輸出入基礎、I/O 優化 | [a001.cpp](./01_Basic_Syntax/a001.cpp) | 成功打通 VS Code 環境，並導入 `sync_with_stdio(false)` 提升 I/O 效率。 |


> 💡 *隨著練習量增加，我會持續將寫好的 `.cpp` 檔案分類放入對應資料夾，並更新此對照表。*
---

## 📝 刷題常用：高效 C++ 模板
在解題時，為了避免大量資料輸入輸出導致 TLE (Time Limit Exceeded)，我設定了標準的 Snippet 加速範本：

```cpp
#include <iostream>
using namespace std;

int main() {
    // 關閉輸入輸出流同步，加速 cin/cout 效率
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // 實作邏輯寫在此處
    
    return 0;
}