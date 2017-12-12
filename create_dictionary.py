import sys
import csv
import re
import string
import json


def map_sentiment_word(sentiment):
    if sentiment == "0":
        return "Dreadful."
    elif sentiment == "1":
        return "Perversity."
    elif sentiment == "2":
        return "And."
    elif sentiment == "3":
        return "Lively."
    return "Masterpiece."


def make_dictionary(text, args):
    result = {}
    reader = csv.reader(text)
    positive = 0
    negative = 0
    neutual = 0
    for line in reader:
        sentiment = line[2]
        if len(args) > 2:
            number = args[-1]
            if sentiment == '1' or sentiment == '0':
                if negative > number:
                    continue
                negative += 1
                sentiment = -1
            elif sentiment == '3' or sentiment == '4':
                if positive > number:
                    continue
                positive += 1
                sentiment = 1
            else:
                if neutual > number:
                    continue
                neutual += 1
                sentiment = 0
        emojis = tuple(i[0] for i in re.findall(
            r'([^\w\s’])', line[1]) if i.strip(string.punctuation) != '')
        if emojis == tuple():
            continue
        emoji_sentiment = (emojis[0], sentiment)
        result[emoji_sentiment] = result.get(emoji_sentiment, 0) + 1
    return result


def make_lexicon(result):
    lexicon = {}
    for key in result.keys():
        emojis = key[0]
        sentiment = key[1]
        if emojis not in lexicon:
            lexicon[emojis] = {sentiment: result[key]}
        else:
            lexicon[emojis][sentiment] = result[key]
    for key in lexicon.keys():
        total = sum(lexicon[key].values())
        for sentiment in lexicon[key].keys():
            lexicon[key][sentiment] /= total
    return lexicon


def write_lexicon(output, lexicon):
    new_lexicon = {}
    for emojis in lexicon.keys():
        new_emojis = ", ".join(emojis)
        new_lexicon[new_emojis] = lexicon[emojis]
    json.dump(new_lexicon, output)


def main(args):
    with open(args[1], newline='', encoding='utf-8') as text:
        result = make_dictionary(text, args)
        lexicon = make_lexicon(result)
    with open('lexicon.json', 'w', encoding='utf-8') as output:
        write_lexicon(output, lexicon)


if __name__ == '__main__':
    main(sys.argv)
