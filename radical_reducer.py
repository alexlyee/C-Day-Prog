#credit to matt!

primes = [2]
raised_list = []
factors = []

def prime_time ():
    for x in range(primes[0], 10000):
        esc = 0
        y = 0
        while y < len(primes) and esc == 0:
            if x % primes[y] == 0:
                esc = 1
            y = y + 1
        if esc == 0:
            primes.append(x)

def factor_test(num):
    for x in range(len(raised_list)):
        if num % raised_list[x] == 0:
            factors.append(primes[x])
            num = num / raised_list[x]
            num = factor_test(num)
    return num

def const():
    v = 1
    for i in range(len(factors)):
        v = v * factors[i]
    return v

exp = int(input("Degree of Root: "))
prime_time()
for x in range(len(primes)):
    raised_list.append(primes[x] ** exp)
num = factor_test(int(input("Number Under the Radical (radicand) : ")))
if num == 1:
    print(str(const()))
else:
    print(str(const()) + " * " + str(exp) + "rt( " + str(int(num)) + " )")
input("Press Enter to Continue.")