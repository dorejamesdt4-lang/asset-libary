from pathlib import Path
import hashlib, json, tempfile
root = Path(__file__).resolve().parent
manifest = json.loads((root / "source_manifest.json").read_text())
for item in manifest["files"]:
    if "parts" not in item:
        continue
    target = root / item["path"]
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as tmp:
        for part in item["parts"]:
            tmp.write((root / part["path"]).read_bytes())
        temp = Path(tmp.name)
    data_hash = hashlib.sha256(temp.read_bytes()).hexdigest()
    if temp.stat().st_size != item["size_bytes"] or data_hash != item["sha256"]:
        temp.unlink()
        raise SystemExit(f"Integrity check failed: {item['path']}")
    temp.replace(target)
    print(f"Restored and verified {item['path']}")
