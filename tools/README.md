# B-Marker Tools

這是 B-Marker 項目的 **創作者工具集**，提供開箱即用的時間轉換函數，直接解決音視頻創作中的工作流痛點。

## 🎯 核心工具
- `frames_to_ms`：影片幀數轉換為毫秒。
- `beats_to_ms`：音樂節拍轉換為毫秒。
- `samples_to_ms`：音頻樣本數轉換為毫秒。
- `ms_to_frames`：毫秒轉換為影片幀數。

## 📜 重要授權說明

**本目錄 (`b-marker/tools/`) 下的所有代碼與資源，均受 [LICENSE-COMMERCIAL.md](./tools/LICENSE-COMMERCIAL.md) 許可協議約束。**

### 您可以免費：
*   用於 **個人、教育及非商業項目**。
*   用於 **開發者少於10人且不直接產生收入** 的小型團隊內部。
*   將其集成到 **非商業性的開源項目** 中（需遵循OSI開源許可證）。

### 您需要商業許可：
*   將其集成到 **商業軟件、SaaS服務或訂閱制產品** 中。
*   用於 **10人以上團隊** 的內部業務運營。
*   對其進行 **再分發、銷售或作為商業產品的主要組件**。

**商業許可申請**：請聯繫 dev@b-marker.com 或 sales@b-marker.com。

## 🔗 項目架構
- **[`b-marker/core/`](../core/)**：項目的開源核心（MIT協議），定義了「音頻作為時間語言」的基礎協議。
- **`b-marker/tools/`**：您當前所在目錄，基於核心協議構建的創作者工具集（本商業許可）。
- 了解完整的雙軌架構，請參見項目根目錄的 [README.md](../../README.md)。

## 🚀 快速開始
```python
# 安裝後（例如：pip install b-marker-tools），或直接從源碼導入
from b-marker.tools.converters import frames_to_ms, beats_to_ms

print(frames_to_ms(24, fps=24.0))  # 輸出: 1000.0
print(beats_to_ms(4, bpm=120.0))   # 輸出: 2000.0

🤝 貢獻
我們歡迎針對工具集的改進和討論。請注意，所有貢獻的代碼均視為接受本目錄的商業許可協議。
