# WAP to find if a number is an even number or not using walrus operator?
num = int(input('Enter a number:'))
if (rem := num % 2) == 0:
    print(num, 'is an even number with remainder',rem)
else:
    print(num, 'is an odd number with remainder',rem)
