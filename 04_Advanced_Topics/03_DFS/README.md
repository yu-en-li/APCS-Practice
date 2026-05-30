<br>

# 03_Shortest_Path: 最短路徑

本節學習如何在帶權圖中計算點對點的最短距離。

<br>

---

<br>

## 📌 學習目標 (Objectives)
- **基礎鞏固**：掌握 Dijkstra, Bellman-Ford, Floyd-Warshall 演算法。
- **效率優化**：根據權重性質（負權邊、稠密/稀疏圖）選定最快演算法。
- **邊界案例**：處理負環路徑的偵測與處理。

<br>

---

## 📝 題目索引 (Problem Index)

<!-- L2_START -->
| 題目名稱 | 程式連結 | 詳細筆記 | 難度 | 核心觀念 | 狀態 |
| :--- | :--- | :---: | :---: | :--- | :---: |
<!-- L2_END -->

<br>

---

<br>

## 💡 解題筆記 (Key Notes)
- **核心重點**：Dijkstra 適用於非負權圖 ($O(E \log V)$)；Bellman-Ford 適用於含負權圖。
- **常見陷阱**：未正確處理優先權佇列 (Priority Queue) 中的重複節點。
- **進階思考**：透過 Floyd-Warshall 處理全點對最短路問題 ($O(V^3)$)。
