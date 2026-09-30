def positive_sum(arr):
    # Your code here
    arr_pos = []
    for i in range(len(arr)):
        if(arr[i]>0):
            arr_pos.append(arr[i])   
    
    return sum(arr_pos)