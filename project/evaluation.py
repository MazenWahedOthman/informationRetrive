def read_mappings():
    f = open("/Users/Mazen/Desktop/cacm/qrels.text")

    mappings = {}

    for a_line in f.readlines():
        voc = a_line.strip().split()
        key = voc[0].strip()
        current_value = voc[1].strip()
        value = []
        if key in mappings.keys():
            value = mappings.get(key)
        value.append(current_value)
        mappings[key] = value

    f.close()
    return mappings


def calculate_recall(res, gold_standard):
    true_pos = 0
    for item, x in res.items():
        for i, j in mappings.items():
            if i == '01':
                x = len(j)
                for k in j:

                    if k == str(item):
                        print(k)
                        true_pos += 1
    print(true_pos)
    return float(true_pos) / float(x)


def calculate_precision_10(res, gold_standard):
    true_pos = 0
    for item, x in res.items():
        for i, j in mappings.items():
            if i == '01':
                for k in j:

                    if k == str(item):
                        print(k)
                        true_pos += 1
    print(true_pos)
    return float(true_pos) / 10


def calculate_precision(res, gold_standard):
    true_pos = 0
    for item, x in res.items():
        for i, j in mappings.items():
            if i == '01':
                for k in j:

                    if k == str(item):
                        print(k)
                        true_pos += 1
    print(true_pos)
    return float(true_pos) / float(len(res.items()))
