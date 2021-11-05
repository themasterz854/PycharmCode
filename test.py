from Cryptodome.Util.number import getPrime, bytes_to_long

x = [getPrime(32) for _ in range(128)]
print(len(x))