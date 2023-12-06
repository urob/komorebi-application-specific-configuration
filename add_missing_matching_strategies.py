from pathlib import Path

import yaml

ROOT = Path(__file__).parents[0]
FILE = ROOT / "applications.yaml"

with open(FILE, "r") as f:
    rules = yaml.safe_load(f)

for r in rules:
    if (id := "identifier") in r:
        if "matching_strategy" not in r[id]:
            r[id]["matching_strategy"] = "Equals" if r[id]["kind"] == "Exe" else "Legacy"

    if (id := "float_identifiers") in r:
        for q in r[id]:
            if "matching_strategy" not in q:
                q["matching_strategy"] = "Equals" if q["kind"] == "Exe" else "Legacy"


with open(ROOT/ "applications_edited.yaml", "w") as f:
    yaml.dump(rules, f, sort_keys=False, allow_unicode=True)
