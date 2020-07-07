#Write program that gets two names and displays them in alphabetical order
import string
letters = string.ascii_lowercase

name1 = input("Enter first name:")
name2 = input("Enter second name:")

if letters.index(name1[0]) > letters.index(name2[0]):
    print(name2)
    print(name1)
elif letters.index(name1[0]) < letters.index(name2[0]):
    print(name1)
    print(name2)
else:
    print("You have entered the same name twice")

