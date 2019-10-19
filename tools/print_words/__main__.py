import click, json


@click.command()
@click.argument('words_json_file')
@click.option('-n', default=20, help='First n top words used')
def main(words_json_file, n):
    with open(words_json_file, 'r') as f:
        obj = json.load(f)
    for partei, data in obj.items():
        print('')
        print(partei)
        print('')
        for year, words in data.items():
            print(year+':')
            for i in words[:n]:
                print('"'+i['word']+'" : '+str(i['count'])+' Mal')
            print('')

if __name__ == "__main__":
    main()
