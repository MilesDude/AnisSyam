from pathlib import Path
p = Path(r'D:\download\Wedding HTML\index.html')
text = p.read_text(encoding='utf-8', errors='replace')
text = text.replace('<span class="detail-icon">�</span>\n        <span class="detail-label">Date · Tarikh</span>', '<span class="detail-icon">&#x1F48D;</span>\n        <span class="detail-label">Date · Tarikh</span>')
text = text.replace('            � &nbsp; Add to Calendar', '            &#x1F48C; &nbsp; Add to Calendar')
text = text.replace('<span class="detail-icon">�</span>\n        <span class="detail-label">Venue · Tempat</span>', '<span class="detail-icon">&#x1F492;</span>\n        <span class="detail-label">Venue · Tempat</span>')
p.write_text(text, encoding='utf-8')
