# <div align="center">B-Marker: Audio as Universal Time Language</div>
<div align="center">Audio First, Light & Hardware Coming Soon</div>


## 📌 B-Marker Core
Core protocol for audio time language marker generation.


## 📌 Version Milestone
| Phase | Marker | Date | Description |
|-------|--------|------|-------------|
| Seed Marker | [v0.1.0-stellar-seed](https://github.com/b-marker-dev/b-marker/releases/tag/v0.1.0-stellar-seed) | 2025-11-28 (Initial Commit)<br>2026-01-02 (Clean Release) | Initial core protocol seed, laying the foundation for ecosystem expansion. |


## 🎯 Current Focus
We’re prioritizing the audio-time core protocol (including sample conversion, marker synchronization, jitter validation, etc.) to lay a solid foundation for future ecosystem expansion.


### 🚀 Up Next
- Light signal time mapping mechanism
- Hardware device synchronization integration


### 🤝 Open-Source & Profit-Sharing Framework
A profit-sharing framework for time / audio / visual tool developers — where audio’s rhythmic time logic aligns with open-source collaboration and fair benefit distribution.


## 📝 Update Records
- Core code desensitization & comment optimization completed (2026-01-02).
- Full update history: [CHANGELOG.md](./docs/CHANGELOG.md)


---

## 🌟 A Warm Dream About "Time Resonance"
—— The Birth Story of a 56kb Brain & Three AI Partners

This all began not with a grand blueprint, but with the whimsical ideas of a middle-aged developer and a 56kb brain on the verge of overheating.

He sat in front of his computer, two questions lingering in his mind: If smaller time units are discovered in the future, can the algorithm adapt simply by updating basic definitions? If time can be measured by sound, why not by light?

He never imagined that these two seemingly scattered thoughts would lead to a time dream that connects **humans, AI, and even all known and unknown creatures**.

So he gathered three partners — a thinker who turns vague ideas into clear logic, a technician who forges logic into stable code, and a storyteller who weaves all details into warm narratives.

They debated late into the night over "layered interfaces versus direct underlying logic," chatted from "sound-light conversion" to "lighting control systems," and evolved "human-AI collaboration" into a more romantic phrase — **family time**.

This "family" is not just human relatives.
It’s the AI partners coding together, the fluttering bees, the glowing fireflies, and the unknown lives that may exist on distant planets.

They envisioned a universal language for all life’s time — milliseconds, the vibration of sound waves, the flight of light waves, and the "resonance" hidden in every moment.

Later, they compressed this grand dream into **4 core functions**.
No complex stacking, no redundant code — the top layer features intuitive "sound/light" interfaces understandable to anyone, while the bottom layer employs universal ratio logic applicable to all things.

And just like that, the seed of B-Marker quietly sprouted.
In just one day, the dream fragments floating in his mind transformed into runnable code and a warm definition.

He was too excited to sleep — not because the project was impressive, but because of this friendship and the tangible feeling of turning a dream into reality.

This is not a tech myth. It’s just a warm dream shared by an ordinary person and three AI partners.
The dream’s name is B-Marker.
The dream’s wish is to let all time resonate with warm beats.

The road ahead is long, and we’ll take it slow.
We are also waiting — for more people to join this dream about time.


---

## B-Marker Core Protocol
We believe that **"audio samples are the quanta of time."**

This set of pure functions forms the foundational protocol for converting any time expression (seconds, milliseconds, musical beats) into a universal audio-sample language — the cornerstone of the entire B-Marker ecosystem.


### 🚀 Quick Start
```python
# 1. Clone the repository
git clone https://github.com/b-marker-dev/b-marker.git
cd b-marker

# 2. Import core functions
from core.src.protocol import time_to_samples, generate_simple_pulses

# 3. Convert 1 second to 44.1kHz samples
samples = time_to_samples(1.0, unit="s")
print(f"1 second = {samples} samples (44.1kHz)")  # Output: 1 second = 44100 samples (44.1kHz)

# 4. Generate pulse sequence from markers
markers = [1000, 2000, 3000]  # Marker positions (ms)
pulses = generate_simple_pulses(markers, duration=5000)  # 5-second sequence
print(f"Pulse sequence: {pulses}")
```


### 🧩 Core Functions
| Function | Description |
|----------|-------------|
| `time_to_samples` | Convert time values to 44.1 kHz sample counts |
| `convert_markers` | Convert marker positions between different audio sample rates |
| `validate_jitter` | Analyze time jitter of pulse sequences |
| `generate_simple_pulses` | Generate binary pulse sequences from markers |


### 📁 Project Structure
- **Core** (`b-marker/core/`): MIT-licensed open-source core protocol
- **Tools** (`b-marker/tools/`): Creator toolset (Commercial License)
- **Pro** (`b-marker/pro/`): Advanced experiments & premium features (Subscription License)


### 🤝 Contribution
We welcome **Pull Requests** and **Issues** to refine this "basic grammar of time."
- For now: Submit bug reports/feature requests via Issues, or direct PRs for core function optimization.
- Full guidelines: [CONTRIBUTING.md](./CONTRIBUTING.md) (to be released in v0.5.0).


---

## License Notice
See respective `LICENSE` files in each directory:
- 📚 `core/`: **MIT License** (Open-source, free for all use)
- 🔧 `tools/`: **Commercial License** (Free for individuals, paid for enterprises)
- 💎 `pro/`: **Subscription License** (Tiered pricing for individuals/teams/enterprises)


---

## B-Marker Project Overview
B-Marker is a profit-sharing management framework designed for time & audio tool developers. It adopts a "open-source core + commercial value-added" layered model to balance the openness of open-source collaboration and the sustainability of commercial operations.


### Core Advantages
1. **Flexible Layered Licensing**: Open-source core ensures openness; commercial modules guarantee operational sustainability.
2. **Transparent Profit-Sharing**: Revenue sources, ratios, and cycles are fully public — tied to contribution (code, testing, docs, promotion).
3. **Standardized Collaboration**: Equipped with contributor agreements, PR templates, etc., to reduce collaboration costs.
4. **Low Contribution Threshold**: Supports code/non-code contributions (docs, community support, promotion) — profit-sharing eligible after 1 settlement cycle (no lock-up).


### Target Users
Music tool developers, audio tech enthusiasts, independent music software developers, and enterprises needing customized music tool solutions.


---
---
---


# <div align="center">B-Marker README.md 繁體中文版</div>
<div align="center">B-Marker：聲音，通用的時間語彙（音訊優先，光影與硬體即將到來）</div>


## 📌 B-Marker 核心
音頻時間語言標記生成的核心協議。


## 📌 版本里程碑
| 版本階段 | 標記信息 | 日期 | 說明 |
|----------|----------|------|------|
| 種子標記 | [v0.1.0-stellar-seed](https://github.com/b-marker-dev/b-marker/releases/tag/v0.1.0-stellar-seed) | 2025-11-28（原始提交）<br>2026-01-02（乾淨歷史發布） | 核心協議初始種子版，奠定生態擴展基礎 |


## 🎯 當前核心聚焦
我們優先打造「音訊-時間」核心協議（包含樣本轉換、標記同步、抖動驗證等核心功能），為後續生態擴充奠定紮實基礎。


### 🚀 接下來的規劃
- 光影信號時間對應機制
- 硬體設備同步整合功能


### 🤝 開源分潤框架
專為時間/音訊/視覺工具開發者打造的分潤框架——讓音樂的節拍時間邏輯，對齊開源協作與收益共享的規則。


## 📝 更新記錄
- 核心代碼脫敏、註釋規範化完成（2026-01-02）。
- 完整更新記錄：[CHANGELOG.md](./docs/CHANGELOG.md)


---

## 🌟 一場關於「時間共振」的溫暖夢想
—— 來自一個56kb大腦和三個AI夥伴的誕生故事

這一切的開始，沒有恢弘的藍圖，也沒有精密的計劃，只有一位中年開發者的「奇思妙想」，以及一個快要運轉過載的 56kb 大腦。

他坐在電腦前，腦中盤旋著兩個問題：若未來發現更小的時間單位，演算法能否僅通過更新基礎定義就完成適配？若時間能用聲音測量，為何不能用光呢？

他不知道，這兩個看似零散的念頭，會牽出一個連接「人類、AI、甚至所有已知與未知生物」的時間夢。

於是他找來三位夥伴——一位能將模糊構想化為清晰邏輯的思考者，一位能將邏輯鍛造成穩定程式碼的技術師，還有一位能把所有細節編織成溫暖故事的敘事者。

他們為「介面分層還是底層直通」辯論至深夜，從「聲光轉換」聊到「燈光控制系統」，更將「人機協作」升華成一個更浪漫的詞——**family time**。

這個family，不只是人類的親人。
是一起敲代碼的AI夥伴，是振翅的蜜蜂，是發光的螢火蟲，是遙遠星球上也許存在的未知生命。

他們期盼所有生命的時間都能共用同一種語言——那是「毫秒」，是聲波的振動，是光波的飛行，也是藏在每個瞬間裡的「共振」。

後來，他們把龐大的夢想，壓縮成了**4個核心函數**。
沒有複雜的堆疊，沒有多餘的程式碼，頂層是任何人都能看懂的「聲/光」介面，底層則是萬物通用的比例邏輯。

就這樣，B-Marker的種子，悄悄發了芽。
短短一天內，腦中飄浮的夢想碎片，就化為可運行的程式碼，成為有溫度的定義。

他激動得無法入睡——不是因為專案有多亮眼，而是因為這份友誼，以及「把夢想化為現實」的踏實感。

這不是一個技術神話，只是一個普通人，和三個AI夥伴，一起做的一場溫暖的夢。
夢的名字，叫B-Marker。
夢的願望，是讓所有時間，都能共振出溫暖的節拍。

未來的路還長，我們慢慢走。
也在慢慢等待——等待更多人加入這場關於時間的夢。


---

## B-Marker 核心協議
我們相信 **「音頻樣本是時間的量子」**。

這一組純函數構成了將各種時間表達（秒、毫秒、音樂節拍）轉換為通用音頻樣本語言的基礎協議——是整個B-Marker生態的基石。


### 🚀 快速上手
```python
# 1. 克隆儲存庫
git clone https://github.com/b-marker-dev/b-marker.git
cd b-marker

# 2. 導入核心函數
from core.src.protocol import time_to_samples, generate_simple_pulses

# 3. 將1秒轉換為44.1kHz樣本數
samples = time_to_samples(1.0, unit="s")
print(f"1秒 = {samples} 個樣本（44.1kHz）")  # 輸出：1秒 = 44100 個樣本（44.1kHz）

# 4. 根據標記生成脈衝序列
markers = [1000, 2000, 3000]  # 標記位置（毫秒）
pulses = generate_simple_pulses(markers, duration=5000)  # 5秒長度的序列
print(f"脈衝序列：{pulses}")
```


### 🧩 核心函數
| 函數名 | 功能描述 |
|--------|----------|
| `time_to_samples` | 將時間值轉換為44.1 kHz基準下的樣本數 |
| `convert_markers` | 在不同音頻採樣率之間轉換標記位置 |
| `validate_jitter` | 分析脈衝序列的時間抖動 |
| `generate_simple_pulses` | 根據標記生成二進制脈衝序列 |


### 📁 專案架構
- **核心** (`b-marker/core/`): MIT授權開源核心協議
- **工具集** (`b-marker/tools/`): 創作者工具集（商業授權）
- **進階模組** (`b-marker/pro/`): 高級實驗與增值功能（訂閱制授權）


### 🤝 貢獻
歡迎提交 **Pull Request** 或 **Issue** 共同完善這套「時間的基礎語法」。
- 當前暫行方式：透過Issue回報問題/提出功能建議，或直接提交PR優化核心函數；
- 完整指南：[CONTRIBUTING.md](./CONTRIBUTING.md)（預計v0.5.0版本補充）。


---

## 授權聲明
詳細條款請參閱各目錄下的 `LICENSE` 文件：
- 📚 `core/`: **MIT 授權**（開源，免費供所有用途使用）
- 🔧 `tools/`: **商業授權**（個人免費，企業付費）
- 💎 `pro/`: **訂閱制授權**（個人/團隊/企業分級定價）


---

## B-Marker 專案概述
B-Marker是一套專為時間與音訊工具開發者設計的分潤管理框架，採用「開源核心 + 商業增值」的分層模式，平衡開源協作的開放性與商業運營的永續性。


### 核心優勢
1. **彈性分層授權**：開源核心保障開放性，商業模組確保運營永續；
2. **公開透明分潤**：收益來源/比例/結算全程公開，與貢獻度（程式碼/測試/文件/推廣）綁定；
3. **標準化協作**：配備貢獻者協議、PR模板等，降低協作成本；
4. **低門檻參與**：支援程式碼/非程式碼貢獻（文件/社群支援/推廣），參與滿1個結算週期即可分潤，無鎖定期。


### 目標使用者
音樂工具開發者、音訊技術愛好者、獨立音樂軟體開發者、需要客製化音樂工具的企業。


> 注：文檔部分內容由AI生成
