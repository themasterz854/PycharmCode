from Crypto.Util.number import *

c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
n = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
e = 65537
p = 1899107986527483535344517113948531328331
q = 674357869540600933870145899564746495319033
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)

print(long_to_bytes(pow(c, d, n)))
enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"
# ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

for i in range(0, len(enc), 2):
    print((((enc[i]) - ((enc[i + 1]))) >> 8))
