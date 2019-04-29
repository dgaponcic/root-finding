from math import exp

def functionVal(x):
    return exp(-0.7 * x) - 0.3 * (x ** 0.5) + 1

f = open('217_secant.txt', 'w')
epsilon = 0.00001
count = 0
old1 = 10.5
old2 = 11.5
new = old2
print("old\t\tnew\t\t\tfunction")

while abs(functionVal(new)) > epsilon:
    new = old2 - functionVal(old2) * (old2 - old1) / (functionVal(old2) - functionVal(old1))
    old2 = new
    count += 1
    print("%d\t\t%.8f\t\t%.8f" % (old1, new, functionVal(new)))


f.write('equation: e^(-0.7 * x) - 0.3 * (x^5) + 1\n')
f.write('\ninitial: 10.5 and 11.5')
f.write('\nnumber of steps: '+ str(count))
f.write('\nresult: '+ str(new))