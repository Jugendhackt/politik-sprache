from ..read_data import parse_data, write_json
from . import analyze_words
import click, json

@click.command()
@click.argument('input_json')
@click.argument('output_json')
def main(input_json, output_json):
    with open(input_json, 'r') as f:
        input_obj = json.load(f)
    output_obj = analyze_words(input_obj)
    with open(output_json, 'w') as f:
        json.dump(output_obj, f)

if __name__ == "__main__":
    main()
