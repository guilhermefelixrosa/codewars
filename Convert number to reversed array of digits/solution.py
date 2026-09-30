def digitize(n):
    list = []
    n_str = str(n)
    for i in range(len(n_str)):
        list.append(int(n_str[i]))
    
    list_reverse = []
    for j in range(len(list)):
        num = len(list)-j-1
        list_reverse.append(list[num])
        
    return list_reverse