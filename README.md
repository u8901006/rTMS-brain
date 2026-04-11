# rTMS Brain

⚡ 重複經顱磁刺激（rTMS）文獻日報 — 每日自動更新

## 關於

本計畫每日自動從 PubMed 抓取最新的 rTMS 相關文獻，透過 Zhipu AI（GLM-5.1）進行摘要、分類與 PICO 分析，生成精美的 HTML 日報頁面，部署於 GitHub Pages。

## 涵蓋範圍

- **期刊**：Brain Stimulation、Clinical Neurophysiology、Neuromodulation 等 20 本 Q1-Q2 期刊
- **疾病關鍵字**：憂鬱症、耳鳴、失眠、慢性疼痛、纖維肌痛症、神經病理性疼痛、偏頭痛、中風復健、焦慮症、PTSD、強迫症、暈眩等
- **核心技術詞**：rTMS、theta burst stimulation、iTBS、cTBS、neuromodulation、neuronavigation

## 線上閱讀

👉 [https://u8901006.github.io/rTMS-brain/](https://u8901006.github.io/rTMS-brain/)

## 架構

```
scripts/
  fetch_papers.py      # PubMed 文獻抓取
  generate_report.py   # Zhipu AI 分析 + HTML 生成
  generate_index.py    # 首頁索引生成
.github/workflows/
  daily-report.yml     # GitHub Actions 每日排程
docs/
  rtms-YYYY-MM-DD.html # 每日報告
  index.html           # 歷史報告索引
```

## 技術棧

- PubMed E-utilities API（文獻來源）
- Zhipu AI GLM-5.1（AI 分析）
- GitHub Actions（自動化排程，每日台北時間 04:00）
- GitHub Pages（靜態網站部署）

## 授權

學術研究用途，歡迎自由使用。
