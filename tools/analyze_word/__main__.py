from ..read_data import parse_data, write_json
from . import analyze_words


if __name__ == "__main__":
    statements = parse_data("data/qual-o-mat/")
    parties = analyze_words(statements)
    write_json("data/words.json", parties)

