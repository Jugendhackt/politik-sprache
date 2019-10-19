import csv
from google.cloud import translate
import json

translate_client = translate.Client()

translated_dataset = {}

with open("data/BRM-emot-submit.csv") as input_file:
    with open("translated_data.json", "w+") as output_file:
        reader = csv.DictReader(input_file, delimiter=",")

        file_text = output_file.read()
        if file_text != "":
            translated_dataset = json.loads()

        for row in reader:
            if row["Word"] not in translated_dataset:
                # try:
                print(row["Word"])

                translated_word = translate_client.translate(row["Word"],target_language='de')["translatedText"]
                
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
