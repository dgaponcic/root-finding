from math import exp

def functionVal(x):
    return exp(-0.7 * x) - 0.3 * (x ** 0.5) + 1

f = open('217_brent.txt', 'w')
a = 10.5
b = 11.5
old = a
epsilon = 0.00001
new = 0
count = 0
print("b\t\tnew\t\t\tfunction")
while abs(functionVal(b)) > epsilon:
    if(abs(functionVal(b)) > abs(functionVal(a))): a, b = b, a
    if functionVal(b) != functionVal(old):
        s = b - (b - old) / (functionVal(b) - functionVal(old)) * functionVal(b)
    else:
        s = (a + b) / 2
    old = b
    m = (a + b) / 2
    if(s < b and s > m): new = s
    else: new = m
    if(functionVal(a) * functionVal(new) < 0): b = new
    else:
        a = b
        b = new
    print("%d\t\t%.8f\t\t%.8f" % (b, new, functionVal(new)))

    count += 1


f.write('equation: e^(-0.7 * x) - 0.3 * (x^5) + 1\n')
f.write('\ninitial: 10.5 and 11.5')
f.write('\nnumber of steps: '+ str(count))
f.write('\nresult: '+ str(new))