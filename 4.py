largest = 0

for j in range(100, 1000):
    for i in range(j, 1000):
        product = i*j
        if str(product)[::-1] == str(product):
            if product > largest:
                largest = product
        
print(largest)