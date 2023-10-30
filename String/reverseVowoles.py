def return_reverse(s):
    vowles = {'a', 'e', 'i', 'o', 'u'}
    s_split=list(s)

    print(s_split)
    i =0 
    j = len(s_split)-1

    while i<=j:
        if s_split[i] in vowles:
            if s_split[j]  in vowles:
                s_split[i], s_split[j] = s_split[j], s_split[i]
                i+=1
                j-=1

            else:
                j-=1
            
            
        else:
            i+=1
    return "".join(s_split)


print(return_reverse("hlifapou"))
