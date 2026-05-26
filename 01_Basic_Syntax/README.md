<br>

# 01_Basic_Syntax: 基礎語法與 I/O 優化

本資料夾紀錄學習基礎語法與輸入輸出優化的過程，這是所有演算法邏輯的根基。

<br>

---

<br>

## 📚 學習重點 (Key Concepts)

<br>

- **[01_IO_Optimization](./01_IO_Optimization/)**：熟悉 `cin`/`cout` 與 `scanf`/`printf` 的效能差異，掌握 I/O 加速技巧。
  
<br>

- **[02_Conditionals](./02_Conditionals/)**：`if-else` 與 `switch` 的邏輯判斷精確度。
  
<br>

- **[03_Loops](./03_Loops/)**：`for`、`while` 迴圈的邊界條件 (Boundary Conditions) 處理。

<br>

- **[04_Functions](./04_Functions/)**：函式的參數傳遞與變數生命週期 (Scope)。

<br>

---

<br>

## 💡 關鍵筆記 (Key Takeaways)

<br>

> *「基礎不紮實，複雜演算法往往會在邊界條件上出錯。」*

<br>

1. **I/O 加速**：在 C++ 中，務必使用 `ios_base::sync_with_stdio(0); cin.tie(0);` 來避免超時。
2. **邊界處理**：迴圈的判斷式應特別注意是否會造成「無限迴圈」或「少跑一次」的問題。

<br>

---

<br>

## 📝 實作挑戰彙整 (Coding Challenges)

<br>

*本分類共計 4 個核心練習模組，涵蓋基礎語法關鍵技術。*

<br>

| 分類 | 題目名稱 | 核心觀念 | 難度 | 複雜度 | 狀態 | 連結 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IO** | 基礎輸入輸出優化 | `#Stream` | ⭐ | $O(1)$ | ✅ | [詳情](./01_IO_Optimization/) |
| **Cond** | 條件判斷邏輯 | `#Logic` | ⭐⭐ | $O(1)$ | ✅ | [詳情](./02_Conditionals/) |
| **Loop** | 迴圈邊界處理 | `#Iter` | ⭐⭐ | $O(n)$ | 📝 | [詳情](./03_Loops/) |
| **Func** | 函式參數傳遞 | `#Scope` | ⭐⭐⭐ | $O(1)$ | 📝 | [詳情](./04_Functions/) |



<br>

---

<br>

*Back to [Main Repository](../README.md)*

<br>
