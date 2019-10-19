import json

def read_json(path):
  f = open(path, "r")
  parsed = json.load(f)
  f.close()
  return parsed

def find(list, key, value):
  for item in list:
    if item[key] == value:
      return item
  
  return None

def find_index(list, key, value):
  for i, item in enumerate(list):
    if item[key] == value:
      return i

  return None

def parse_data(base):
  allStatements = []
  files = read_json(base + "list.json")

  for file in files:
    opinions = read_json(base + file + "/opinion.json")
    parties = read_json(base + file + "/party.json")
    statements = read_json(base + file + "/statement.json")
    overview = read_json(base + file + "/overview.json")

    for opinion in opinions:
      party = find(parties, "id", opinion["party"])
      statement = find(statements, "id", opinion["statement"])

      statementInstance = {
        "text": statement["text"], 
        "party": party["name"], 
        "party_long_name": party["longname"],
        "from_election": overview["title"],
        "election_date": overview["date"]
      }

      allStatements.append(statementInstance)

  return allStatements

def write_json(path, data):
  f = open(path, "w")
  f.write(json.dumps(data))
  f.close()

if __name__ == "__main__":
  statements = parse_data("../data/qual-o-mat/")
  write_json("output.json", statements)

