import json
import re


def preprocess(text):
    text = text.lower()
    text = text.lstrip()
    text = re.sub(r'[.]', ' ', text)
    return text


def splitkeep(text, delimiter):
    sentence = [sentence + delimiter for sentence in text.split(delimiter) if sentence]
    return sentence


def gen_ngrams(text, n_count):
    sentences = splitkeep(text, '.')

    ngrams = dict()
    for sentence in sentences:
        sentence = preprocess(sentence)
        words = sentence.split()

        ngrams = []
        for i in range(len(words) - n_count + 1):
            ngrams.append(words[i:i + n_count])
    return ngrams


def ngrams_to_nested_dict(ngrams):
    ngram_dict = dict()

    for ngram in ngrams:
        for word in ngram:
            if ngram_dict[word]:
                ngram_dict[word] += 1
            else:
                ngram_dict[word] = 1


def main():
    n_count = 3
    text = 'The big truck is louder than the small car. The small kid in the car likes the big truck.'

    ngrams = gen_ngrams(text, n_count)

    # print(ngrams)

    ngrams_to_nested_dict(ngrams)

    # print(sum(ngrams.values()))
    # pop_ngram = max(ngrams.values())
    #
    # pop_ngrams = list()
    # for key, value in ngrams.items():
    #     if value == pop_ngram:
    #         pop_ngrams.append(key)
    #
    # print(pop_ngrams)


if __name__ == '__main__':
    main()
