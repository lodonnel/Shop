import ast


def rw_file(filename, content=None):
    if content is None:     # reading

        with open(filename) as f:
            list_of_dict = []
            for line in f:

                line = line.rstrip()
                new_dict = {}
                pairs = line.split(',')
                for kv in pairs:
                    k, v = kv.split(":")
                    new_dict[k] = v
                list_of_dict.append(new_dict)

            return list_of_dict
    else:                   # writing
        with open(filename, "a+") as f:
            f.writelines(content)


def stringify(list_items):
    content = ""
    for item in list_items:
        content = ','.join(item)
        content += "\n"
    return content

# if __name__ == '__main__': main()
