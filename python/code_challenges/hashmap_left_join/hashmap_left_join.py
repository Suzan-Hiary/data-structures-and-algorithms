from hashtable import HashTable
def left_join(ht_one, ht_two):

    
    listt = []
    for elem in ht_one:
        if elem:

            i = 0
            curr_elem = elem[i]


            while curr_elem:

                key = curr_elem[0]

                if ht_two.contains(key):
                    listt.append([key, curr_elem[1], ht_two.get(key)])


                else:
                    listt.append([key, curr_elem[1], None])
                try:    
                    if elem[i+1]:
                        i+=1
                        curr_elem = elem[i]
                    else:
                        curr_elem = None
                except:
                    break

    return listt