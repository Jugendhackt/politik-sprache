import json

if __name__== "__main__":
    data = {}

    with open("data/wordtype_analysis.json") as f:
        parties = json.load(f)

    for party in parties:
        print(party, parties[party])
        if party not in data:
            data[party] = {}
        for year in parties[party]:
            if year not in data[party]:
                data[party][year] = {}
            word_count = 0
            for word_type in parties[party][year]:
                if parties[party][year][word_type] not in data[party][year]:
                    data[party][year][word_type] = {}
                word_count += parties[party][year][word_type]
            print(word_count)
            for word_type in parties[party][year]:
                data[party][year][word_type] = parties[party][year][word_type]/word_count

    with open("data/wordtype_perc.json", "w+") as f:
        f.write(json.dumps(data))
        f.close()
