## DIVA RAHMANINGTYAS CITRA AYU PRADANI
## L200200237
## Praktikum Algoritma dan Struktur Data I

## Nomor 1
## Program pengecekan username
import re
u = '@divarhm07_'
pola = r'@[a-zA-Z_]+[0-9.\_]+'
un = re.findall(pola, u)
if un:
    if u == un[0]:
        print('PASS')
    elif u != un[0]:
        print('FAILED')
else:
    print('FAILED')

## Nomor 2
## Program untuk mencetak email yang ada pada teks
import re
w = open('email.txt', 'r', encoding='latin1')
s = w.read()
w.close()
pola = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
email = re.findall(pola, s)
print(email)

## Nomor 3
## Menentukan angka terluar dari sebuah pohon biner
class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
# Membuat simpul-simpul dan mengisi data
A =  _SimpulPohonBiner('Diva')
B =  _SimpulPohonBiner('Dayana')
C =  _SimpulPohonBiner('Dhilla')
D =  _SimpulPohonBiner('Dimas')
E =  _SimpulPohonBiner('Dana')
F =  _SimpulPohonBiner('Mahes')
G =  _SimpulPohonBiner('Zaki')
H =  _SimpulPohonBiner('Yoga')
I =  _SimpulPohonBiner('Dio')
J =  _SimpulPohonBiner('Pradani')
# Menghubungkan simpul ortu-anak
A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I
# Menemukan angka terluar pohon biner
    # aaaaaa maaf mas belum nemu
