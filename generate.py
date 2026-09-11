from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
READINGS = ROOT / "readings"
OUTPUT = ROOT / "readings.json"

def title_from_html(html, fallback):
    m = re.search(r"<h2[^>]*>(.*?)</h2>", html, flags=re.I | re.S)
    if not m:
        return fallback
    title = re.sub(r"<[^>]+>", "", m.group(1))
    return re.sub(r"\s+", " ", title).strip() or fallback

items = []
for p in sorted(READINGS.glob("*.html")):
    html = p.read_text(encoding="utf-8")
    items.append({
        "file": p.name,
        "title": title_from_html(html, p.stem),
        "path": f"./readings/{p.name}",
    })

OUTPUT.write_text(json.dumps(items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"Generated {OUTPUT.name} with {len(items)} readings.")
