from math import exp, log

def functionVal(x):
    return exp(-0.7 * x) - 0.3 * (x ** 0.5) + 1

def fixedFunction(x):
    return (exp(-0.7 * x) + 1) ** 2 / 0.09

print("old\t\tnew\t\t\tfunction")
f = open('2017_fixedPoint.txt', 'w')
old = new = 10.5
epsilon = 0.00001
count = 0
while abs(functionVal(new)) > epsilon:
    new = fixedFunction(old)
    old = new
    count += 1
    print("%d\t\t%.8f\t\t%.8f" % (old, new, functionVal(new)))



f.write('equation: e^(-0.7 * x) - 0.3 * (x^5) + 1\n')
f.write('\ninitial: 10.5 and 11.5')
f.write('\nnumber of steps: '+ str(count))
f.write('\nresult: '+ str(new))