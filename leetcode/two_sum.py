def find_indices(lst,target):
    dic = {}

    for i in range(len(lst)):
        complement = target-lst[i]
        if(dic.get(complement)):
            return [i,dic.get(complement)]
        else:
            dic[lst[i]] = i;
    return [-1,-1]

indices = find_indices([12,45,5,7,2,9],11)
print('{first} - {second}'.format(first = indices[0], second = indices[1]))