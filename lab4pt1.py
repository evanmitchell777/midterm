#1000 newtons too heavy
#10 newtons too light

Mass = float(input("Enter objects mass:"))
weight = Mass * 9.8

if weight > 1000:
    print("Object too heavy!")

elif weight < 10:
    print ("object too light!")

else:
    print (weight)
