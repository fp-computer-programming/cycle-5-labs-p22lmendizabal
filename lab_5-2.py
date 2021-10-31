# author: LM (AMDG) 10/27/21

fruit1 = input(" Enter a word. ")
fruit2 = input("Enter another word. ")
if fruit1 > fruit2:
    print(fruit1 + " comes after " + fruit2)
elif fruit1 < fruit2:
    print(fruit1 + " comes before " + fruit2)
else:
    print(fruit1 + " and " + fruit2 + " are the same.")
