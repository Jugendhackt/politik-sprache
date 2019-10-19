import json
import csv
from collections import defaultdict

tree = lambda: defaultdict(tree)


def analyze_vad():
    vad_data = {}
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    with open("data/translated_data.csv") as vad_files:
        vad_reader = csv.DictReader(vad_files)
        for row in vad_reader:
            vad_data[row["word_german"]] = {
                "valence": float(row["valence"]),
                "arousal": float(row["arousal"]),
                "dominance": float(row["dominance"]),
            }

    with open("data/words.json") as file:
        parties = json.load(file)

        for party in parties:
            for year in parties[party]:
                count = 0
                for word in parties[party][year]:
                    if word["word"] in vad_data:
                        data[party][year]["valence"] += (
                            (vad_data[word["word"]]["valence"]-4.5)/4.5 * word["count"]
                        )
                        data[party][year]["arousal"] += (
                            (vad_data[word["word"]]["arousal"]-4.5)/4.5 * word["count"]
                        )
                        data[party][year]["dominance"] += (
                            (vad_data[word["word"]]["dominance"]-4.5)/4.5 * word["count"]
                        )
                        count += word["count"]
                if count != 0:
                    data[party][year]["valence"]  /= count
                    data[party][year]["arousal"]  /= count
                    data[party][year]["dominance"]  /= count
    
    with open("data/vad.json", "w") as file:
        json.dump(data, file)

