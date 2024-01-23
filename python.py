def process_list(lst):
    try:
        if (len(lst)%10!=0):
            raise Exception('length of a lst is not a multiple of 10')
        new_lst=[lst[i] for i in range(0,len(lst)) if i%2!=0 and i%3!=0]
        return new_lst
    except Exception as e:
        return e        

# for manually checking the list
# lst=list(map(int,input().split())) 
# print(process_list(lst))
