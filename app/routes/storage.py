from pathlib import Path
import json
import os

# Vercel's filesystem is read-only except for /tmp, so fall back to it
# there. Note: /tmp is ephemeral and not shared across instances, so this
# is not persistent storage in production - only a stopgap.
DATA_DIR = Path("/tmp") if os.environ.get("VERCEL") else Path("Data")
DATA_FILE = DATA_DIR / "issues.json"

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE,"r") as f:
            content = f.read()
            if(content.strip):
                return json.loads(content)
    return []

def save_data(data):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data,f,indent=2)

