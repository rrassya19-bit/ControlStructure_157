n = int(input("MAsukkan Nilai N Untuk Deret Fibbonaci: "))

a = 0
b = 1

print("Deret Fibonacci", n, ":")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b