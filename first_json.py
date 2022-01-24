import json

START_NUMBER = 1
END_NUMBER = 100

for number in range(START_NUMBER, END_NUMBER+1):
    print(number)
    json_data = {
        "description": '”Baby Sharks Guild” is a collection that includes 10,000 kinds of unique sharks. In the collection, you can definitely find your best kawaii sharks here. Please see [BabySharksGuild.com](https://babysharksguild.com/) for the details. \n\n This studio is made up of unrecognized young creators in Japan. It was established thanks to the cooperation of entrepreneurs, engineers, interpreters, designers, illustrators, Gif animators, video creators and planner.\n\n This amazing Gif animation was created by **Y.Nagatsuka** in flipbook animation style.',
        "image": "https://metadata.babysharksguild.com/images/0.gif",
        "name": f"Baby Shark #{number}",
        "attributes": [{
            "trait_type": "STATUS",
            "value": "Unrevealed"
        }]
    }

    with open(f"./data/{number}", "w") as f:
        json.dump(json_data, f, indent=2)