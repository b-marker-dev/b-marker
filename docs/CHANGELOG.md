# CHANGELOG
All notable changes to this project will be documented in this file.
本項目的所有重要變更都將記錄在此文件中。

## [0.1.0] - 2026-01-02
### Changed
- Code desensitization: Remove sensitive path/tool-related code
  代碼脫敏：移除敏感路徑/工具相關代碼
- Comment optimization: English first, Traditional Chinese second
  註釋優化：英文在前，繁體中文在後
- Clean Git history: Create new branch with pure core code
  Git歷史清理：創建新分支，只保留純核心代碼
- Remove redundant test code, keep only core logic
  移除多餘測試代碼，僅保留核心邏輯

### Added
- Seed date annotation in core code (for ritual sense)
  核心代碼中添加種子日期註釋（保留儀式感）
- CHANGELOG.md file to track all updates
  新增CHANGELOG.md文件跟蹤所有更新

## [0.0.1] - 2025-11-28 (Seed Version)
### Added
- Initial core protocol implementation
  初始核心協議實現
- Basic functions: time_to_samples, convert_markers, generate_simple_pulses, validate_jitter
  基礎函數：時間轉樣本、標記轉換、脈衝生成、抖動驗證
- Chinese comments for core functions
  核心函數的中文註釋

# Version Rule
- MAJOR.MINOR.PATCH
  - MAJOR: Incompatible API changes (large refactoring)
    不兼容的API變更（大規模重構）
  - MINOR: New features (backward compatible)
    新增功能（向後兼容）
  - PATCH: Bug fixes / small optimizations (backward compatible)
    修復bug/小優化（向後兼容）

# 版本規則
- MAJOR.MINOR.PATCH
  - MAJOR：不兼容的API變更（大規模重構）
  - MINOR：新增功能（向後兼容）
  - PATCH：修復bug/小優化（向後兼容）