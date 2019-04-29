from math import exp

def functionVal(x):
    return exp(-x) - x
def derivativeVal(x):
    return -exp(-x) - 1

print("old\t\tnew\t\t\tfunction")

f = open('217_newton.txt', 'w')
epsilon = 0.00000001
old = new = 0.5
count = 0

while abs(functionVal(new) > epsilon):
    count += 1
    old = new
    new = old - functionVal(new) / derivativeVal(new)
    print("%d\t\t%.8f\t\t%.8f" % (old, new, functionVal(new)))


f.write('equation: e^(-0.7 * x) - 0.3 * (x^5) + 1\n')
f.write('\ninitial: ' + str(10.5))
f.write('\nnumber of steps: '+ str(count))
f.write('\nresult: '+ str(new))
