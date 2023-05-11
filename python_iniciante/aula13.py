a ='a'
b = 'b'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a, b, c)
print(formato)

#professor

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)