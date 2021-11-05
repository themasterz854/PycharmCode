from Cryptodome.Util.number import getPrime, bytes_to_long
#from private import flag

def product(lt):
	rt = 1
	for num in lt:
		rt *= num
	return rt
#x = bytearray("flag","UTF-8")
#m = 2
#primes = [getPrime(32) for _ in range(128)]
#print(len(primes))
#n = 1209189015004777713827486192606831034367269297350769290045032552593515939034780696478888918514383256365592992271688226983110999601106257134680800266911065034210257730438931
#e = 65537
#print(n)
#print(pow(m, e, n))

