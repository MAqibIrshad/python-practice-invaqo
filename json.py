import json
json_data = {
    "name": "MAqibIrshad",
    "designation": "AI Engineer"
}

with open("data.json", 'w') as f:
    json.dump(json_data, f, indent=4)

with open("data.json") as f:
    json_file = json.load(f)
    print(json_file)