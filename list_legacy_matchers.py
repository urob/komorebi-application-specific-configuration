from pathlib import Path

import yaml

ROOT = Path(__file__).parents[0]
FILE = ROOT / "applications.yaml"

with open(FILE, "r") as f:
    rules = yaml.safe_load(f)

for r in rules:
    if (id := "identifier") in r:
        if r[id]["matching_strategy"] != "Legacy":
            del r[id]

    if (id := "float_identifiers") in r:
        for i in reversed(range(len(r[id]))):
            if r[id][i]["matching_strategy"] != "Legacy":
                del r[id][i]

for i in reversed(range(len(rules))):
    r = rules[i]
    if (id := "float_identifiers") in r:
        if r[id] == []:
            del r[id]

    if "options" in r:
        del r["options"]

    if "identifier" not in r and "float_identifiers" not in r:
        del rules[i]


with open(ROOT/ "legacy_uses.yaml", "w") as f:
    yaml.dump(rules, f, sort_keys=False, allow_unicode=True)
