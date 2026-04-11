#!/usr/bin/env python3
"""Generate index.html listing all rTMS daily reports."""

import glob
import os
from datetime import datetime

html_files = sorted(glob.glob("docs/rtms-*.html"), reverse=True)
links = ""
for f in html_files[:30]:
    name = os.path.basename(f)
    date = name.replace("rtms-", "").replace(".html", "")
    try:
        d = datetime.strptime(date, "%Y-%m-%d")
        date_display = d.strftime("%Y年%-m月%-d日")
    except Exception:
        date_display = date
    weekday = (
        ["一", "二", "三", "四", "五", "六", "日"][
            datetime.strptime(date, "%Y-%m-%d").weekday()
        ]
        if len(date) == 10
        else ""
    )
    links += f'<li><a href="{name}">📅 {date_display}（週{weekday}）</a></li>\n'

total = len(html_files)

index = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>rTMS Brain · 重複經顱磁刺激文獻日報</title>
<style>
  :root {{ --bg: #0a0e1a; --surface: #111827; --line: #1e293b; --text: #e2e8f0; --muted: #94a3b8; --accent: #38bdf8; --accent2: #818cf8; --accent-soft: rgba(56,189,248,0.12); }}
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ background: var(--bg); color: var(--text); font-family: "Noto Sans TC", "PingFang TC", "Helvetica Neue", Arial, sans-serif; min-height: 100vh; }}
  body::before {{ content: ''; position: fixed; top: -40%; left: -20%; width: 80%; height: 80%; background: radial-gradient(circle, rgba(56,189,248,0.06) 0%, transparent 70%); pointer-events: none; z-index: 0; }}
  .container {{ position: relative; z-index: 1; max-width: 640px; margin: 0 auto; padding: 80px 24px; }}
  .logo {{ font-size: 48px; text-align: center; margin-bottom: 16px; }}
  h1 {{ text-align: center; font-size: 24px; color: #fff; margin-bottom: 8px; }}
  .subtitle {{ text-align: center; color: var(--accent); font-size: 14px; margin-bottom: 48px; }}
  .count {{ text-align: center; color: var(--muted); font-size: 13px; margin-bottom: 32px; }}
  ul {{ list-style: none; }}
  li {{ margin-bottom: 8px; }}
  a {{ color: var(--text); text-decoration: none; display: block; padding: 14px 20px; background: var(--surface); border: 1px solid var(--line); border-radius: 12px; transition: all 0.2s; font-size: 15px; }}
  a:hover {{ background: var(--accent-soft); border-color: var(--accent); transform: translateX(4px); }}
  .clinic-banner {{ margin-top: 48px; }}
  .clinic-link {{ display: flex; align-items: center; gap: 14px; padding: 18px 24px; background: linear-gradient(135deg, rgba(56,189,248,0.06), rgba(129,140,248,0.06)); border: 1px solid rgba(56,189,248,0.2); border-radius: 16px; text-decoration: none; color: var(--text); transition: all 0.3s; }}
  .clinic-link:hover {{ border-color: var(--accent); transform: translateY(-2px); }}
  .clinic-icon {{ font-size: 28px; flex-shrink: 0; }}
  .clinic-name {{ font-size: 15px; font-weight: 700; color: #fff; flex: 1; }}
  .clinic-arrow {{ font-size: 18px; color: var(--accent); font-weight: 700; }}
  footer {{ margin-top: 56px; text-align: center; font-size: 12px; color: var(--muted); }}
  footer a {{ display: inline; padding: 0; background: none; border: none; color: var(--muted); }}
  footer a:hover {{ color: var(--accent); }}
</style>
</head>
<body>
<div class="container">
  <div class="logo">⚡</div>
  <h1>rTMS Brain</h1>
  <p class="subtitle">重複經顱磁刺激文獻日報 · 每日自動更新</p>
  <p class="count">共 {total} 期日報</p>
  <ul>{links}</ul>
  <div class="clinic-banner">
    <a href="https://www.leepsyclinic.com/" class="clinic-link" target="_blank">
      <span class="clinic-icon">🏥</span>
      <span class="clinic-name">李政洋身心診所</span>
      <span class="clinic-arrow">→</span>
    </a>
  </div>
  <footer>
    <p>Powered by PubMed + Zhipu AI · <a href="https://github.com/u8901006/rTMS-brain">GitHub</a></p>
  </footer>
</div>
</body>
</html>"""

with open("docs/index.html", "w", encoding="utf-8") as f:
    f.write(index)
print("Index page generated")
