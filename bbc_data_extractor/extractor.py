import csv
from random import shuffle
from os import listdir, walk
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk


# Part 1: generate "classes.txt"
def load_classes():
    classes_list = []
    for entry in listdir("bbc"):
        classes_list.append(entry) if (entry[-3:] != "TXT") else 0
    return classes_list


def create_classes():
    classes_list = load_classes()
    with open("bbc_data/classes.txt", "w") as outfile:
        for i, entry in enumerate(classes_list):
            outfile.write(str(i) + ":" + entry + "\n")


# Part 2: generate "keywords.txt"

# Part 3: generate "dataset.csv"
def load_dataset():
    csv_list = []
    classes_list = load_classes()
    for i, entry in enumerate(classes_list):
        path = "bbc/" + entry
        for (dirpath, firnames, filenames) in walk(path):  # five classes
            for filename in filenames:
                with open(path + "/" + filename, encoding='unicode_escape') as infile:
                    doc = list(csv.reader(infile))
                    data = [i+1, doc[0][0] + ". " + doc[2][0]]
                    csv_list.append(data)
    shuffle(csv_list)
    return csv_list


def create_dataset():
    csv_list = load_dataset()
    with open("bbc_data/dataset.csv", "w") as outfile:
        w = csv.writer(outfile)
        w.writerows(csv_list)


if __name__ == "__main__":
    # create_classes()
    # create_dataset()
    counter = 1
    with open("bbc_data/dataset.csv") as dataset:
        r = csv.reader(dataset)
        for r_ele in r:
            print(f"{len(r_ele)}: {counter}: {r_ele}")
            counter += 1
