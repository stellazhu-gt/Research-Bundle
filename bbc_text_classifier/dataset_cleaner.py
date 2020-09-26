import csv

classes_dict = {}


def classes_list_generator():
    classes_list = []
    with open("bbc-text.csv") as raw_file:
        r = csv.reader(raw_file)
        for entry in list(r)[1:]:
            if entry[0] not in classes_list:
                classes_list.append(entry[0])
    return classes_list


def classes_generator():
    classes_list = classes_list_generator()
    print(classes_list)
    with open("bbc_data2/classes.txt", "w") as output:
        w = csv.writer(output)
        for i, c in enumerate(classes_list):
            w.writerow([str(i) + ":" + c])
            classes_dict[c] = i + 1


def dataset_generator():
    print(classes_dict)
    with open("bbc-text.csv") as raw_file:
        r = csv.reader(raw_file)
        with open ("bbc_data2/dataset.csv", "w") as output:
            w = csv.writer(output)
            for row in list(r)[1:]:
                w.writerow([classes_dict[row[0]], row[1]])


if __name__ == "__main__":
    classes_generator()
    dataset_generator()