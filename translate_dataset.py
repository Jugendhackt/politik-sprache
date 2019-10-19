import csv
from googletrans import Translator
import json

translator = Translator()
translated_dataset = {}

with open("BRM-emot-submit.csv") as input_file:
    with open("translated_data.json", "w+") as output_file:
        reader = csv.DictReader(input_file, delimiter=",")

        file_text = output_file.read()
        if file_text != "":
            translated_dataset = json.loads()

        for row in reader:
            if row["Word"] not in translated_dataset:
                # try:
                print(row["Word"])
                translater_helper = translator.translate(row["Word"], dest="de")
                print(translater_helper)
                translated_word = translater_helper.text
                translated_dataset[row["Word"]] = {
                    "word_german": translated_word,
                    "valence": row["V.Mean.Sum"],
                    "arousal": row["A.Mean.Sum"],
                    "dominance": row["D.Mean.Sum"],
                }
                print(
                    {
                        "word_english": row["Word"],
                        "word_german": translated_word,
                        "valence": row["V.Mean.Sum"],
                        "arousal": row["A.Mean.Sum"],
                        "dominance": row["D.Mean.Sum"],
                    }
                )
            # except json.decoder.JSONDecodeError as error:
            #     print(error)

        output_file.write(json.dumps(translated_dataset))
