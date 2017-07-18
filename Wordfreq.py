import sys
import re
import collections
import glob
from tqdm import tqdm


def getArgv():
    return sys.argv[1]


def count_words(string_a):
    text = string_a.split()
    counter = collections.Counter(w.lower() for w in text)
    return counter


def filter_words(wordfreq):
    with open('/home/hdk216/Documents/FYP/pythonCrawler/wordList', 'r') as f:
        ignore = f.readlines()
        ignore = [x.strip() for x in ignore]
    for word in list(wordfreq):
        if word in ignore:
            del wordfreq[word]


def acquire_list():
    fnames = []
    fpath = "/home/hdk216/Documents/kernel/*.c"
    fpath2 = "/home/hdk216/Documents/kernel/**/*.c"
    wordfreq = collections.Counter()

    for f in glob.glob(fpath):
        fnames.append(f)

    for f in glob.glob(fpath2):
        fnames.append(f)

    for fname in tqdm(fnames):
        with open(fname) as f:
            content = f.readlines()

        content = [x.strip() for x in content]
        x = re.findall('\* .*', content[1])
        # print x

        a = [x for x in content if re.match('\* .+', x)]
        # print '\n'.join(a)

        for strings in a:
            wordfreq_part = count_words(strings)
            wordfreq = wordfreq + wordfreq_part

    filter_words(wordfreq)
    print wordfreq

    with open('./counter', 'w+') as f:
        for k in wordfreq:
            f.write("{} {}\n".format(k, wordfreq[k]))


def get_wordfreq_from_file():
    with open('./counter') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    wordfreq = {}
    for line in content:
        line = line.split()
        wordfreq[line[0]] = line[1]

    print collections.Counter(wordfreq).most_common()
