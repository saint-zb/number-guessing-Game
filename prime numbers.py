def is_prime(num):

    if num <= 1:
        print(False)
    for i in range(2,int(num**0.5)+1):
        print (i)
is_prime(10)

"""the range function starts at 0 by default
 and stops at the "lastnumber-1""ie it is not inclusie 
 of the stop arg"""
# 
