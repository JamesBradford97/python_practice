#2**3 is 2 to the power 3

def raise_to_power(base_num,power):
    #return base_num**number
    result = 1
    for index in range(power):
        result *= base_num
    return result

print(raise_to_power(3,2))
