import spacy
import json

if __name__=="__main__":
    data = {}
    with open("data/statements.json") as file:
        statements = json.load(file)

        nlp = spacy.load("de_core_news_sm")
        for statement in statements:
            if statement["party"] not in data:
                data[statement["party"]] = {}
            if statement["year"] not in data[statement["party"]]:
                data[statement["party"]][statement["year"]] = {}

            doc = nlp(statement["text"])
            for token in doc:
                if token.pos_ not in data[statement["party"]][statement["year"]]:
                    data[statement["party"]][statement["year"]][token.pos_] = 1
                else:
                    data[statement["party"]][statement["year"]][token.pos_]+=1


    with open("data/wordtype_analysis.json", "w+") as f:
        f.write(json.dumps(data))
        f.close()
