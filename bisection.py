from math import exp

def functionVal(x):
    return exp(-0.7 * x) - 0.3 * (x ** 0.5) + 1

print("first\t\tmiddle\t\t\tfunction")
f = open('217_bisection.txt', 'w')
a = 10.5
b = 11.5
epsilon = 0.00001
m = (a + b) / 2
count = 0
while abs(functionVal(m)) > epsilon:
    if functionVal(a) * functionVal(m) < 0:
        b = m
    else:
        a = m
    m = (a + b) / 2
    print("%d\t\t%.8f\t\t%.8f" % (a, m, functionVal(m)))
    count += 1


f.write('equation: e^(-0.7 * x) - 0.3 * (x^5) + 1\n')
f.write('\ninitial: 10.5 and 11.5')
f.write('\nnumber of steps: '+ str(count))
f.write('\nresult: '+ str(m))