#!/usr/bin/env python
"""Generate README links for vehicles."""
import json

with open("output/models.json", "r") as fileh:
    result = json.load(fileh)

for model in result:
    print(
        f"- [{model['series'].replace('_', ' ')}](https://flatgithub.com/major/lexgrabber?filename=output/{model['modelCode'].upper()}.csv)"
    )
