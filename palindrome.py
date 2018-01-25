p = input("Input a word and the program will determine if it's a palindrome or not: ")

p_reverse = ""
for i in range(len(p)-1, -1, -1):
    p_reverse += p[i]

if(p == p_reverse):
    print("It's a palindrome!")

else:
    print("It's not a palindrome")
