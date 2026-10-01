def abbrev_name(name):
    name_splited = name.split()
    name_initials = name_splited[0][0].upper()+'.'+name_splited[1][0].upper()
    print(name_initials)
    return name_initials