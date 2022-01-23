import json

START_NUMBER = 1
END_NUMBER = 10000

for number in range(START_NUMBER, END_NUMBER+1):
    print(number)
    json_data = {
        "description": "Baby Sharks Guild, ",
        "image": "https://metadata.babysharksguild.com/images/0.gif",
        "name": f"Baby Shark #{number}",
        "attributes": [{
            "trait_type": "STATUS",
            "value": "Unrevealed"
        }]
    }

    with open(f"./data/{number}", "w") as f:
        json.dump(json_data, f)