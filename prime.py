odd=1
prime = 1
while(prime < 1000):
    prime_test = 2
    odd = odd + 2
    while(odd % prime_test != 0 ):
        prime_test += 1
        if(prime_test == odd):
            prime = prime + 1
print("The 1000th prime number is:", odd)








#instantiate vars
    #prime vars
    #test var
    #odd vars

#test for prime
    #take odd value, and divide by test value while remainder is above 0
    # add 1 to each iteration to test
    #if test value equals odd value, then add 1 to prime var
    #iterate until prime var is 1000 and print out 1000th value
