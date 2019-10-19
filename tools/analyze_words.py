import read_data
import operator

statements = read_data.parse_data("../data/qual-o-mat/")
parties = {}

mostUsed = 0
mostUsedWord = ""

for statement in statements: 
  party = statement["party"]

  if party not in parties:
    parties[party] = []


  for word in statement["text"].split():
    word = word.lower()
    word = word.replace(".", "")
    word = word.replace("!", "")
    word = word.replace("?", "")

    i = read_data.find_index(parties[party], "word", word)
    if i == None:
      i = len(parties[party])
      parties[party].append({ "count": 0, "word": word })
      
    parties[party][i]["count"] += 1

    if parties[party][i]["count"] > mostUsed:
      mostUsed = parties[party][i]["count"]
      mostUsedWord = word

  parties[party].sort(key=operator.itemgetter("count"), reverse=True)

for party in parties:
  for i, word in enumerate(parties[party]):
    print("Top " + str(i + 1) + " word of " + party + ": " + word["word"] + ", used " + str(word["count"]) + " times!")

    if i > 10:
      break

read_data.write_json("words.json", parties)

