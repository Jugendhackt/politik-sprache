from . import parse_data
from . import write_json

if __name__ == "__main__":
    statements = parse_data("data/qual-o-mat/")
    write_json("data/statements.json", statements)

