import read_data
import operator

def analyze_words(statements):
  parties = {}

  for statement in statements: 
    party = statement["party"]
    year = statement["year"]

    if party not in parties:
      parties[party] = {}

    if year not in parties[party]:
      parties[party][year] = []

    for word in statement["text"].split():
      word = word.lower()
      word = word.replace(".", "")
      word = word.replace("!", "")
      word = word.replace("?", "")

      i = read_data.find_index(parties[party][year], "word", word)
      if i == None:
        i = len(parties[party][year])
        parties[party][year].append({ "count": 0, "word": word })
        
      parties[party][year][i]["count"] += 1
  
  
  for party in parties:
    for year in parties[party]:
      parties[party][year].sort(key=operator.itemgetter("count"), reverse=True)
  

  return parties

if __name__ == "__main__":
  statements = read_data.parse_data("../data/qual-o-mat/")
  parties = analyze_words(statements)
  read_data.write_json("words.json", parties)

