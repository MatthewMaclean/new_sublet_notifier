def write_list_to_file(f, l):
    file = open(f, "w")
    file.write("\n".join(l))
    file.close()


def get_list_from_file(f):
    file = open(f, "r")
    ids = file.read().split()
    file.close()
    return ids
