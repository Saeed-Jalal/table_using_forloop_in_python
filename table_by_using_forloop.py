number = int(input("Inter the number you want table: "))
#Using forloop here
for count in range(1, 100):
    product = number * count
    print(number, " X ", count, " = ", product)