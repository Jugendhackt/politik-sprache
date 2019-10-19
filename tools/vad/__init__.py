import json

def analyze_vad():
  with open("data/translated_data.json"):
    with open("data/words.json") as file:
      parties = json.load(file)

      for party in parties:
        for year in parties[party]:
          for word in parties[party][year]:
            print(word)

