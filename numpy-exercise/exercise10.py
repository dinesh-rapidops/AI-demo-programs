n = int(input('Enter an integer:'))
print('the divisors of the number are:')
for i in range(1, n+1):
    if(n%i==0):
        print(i)