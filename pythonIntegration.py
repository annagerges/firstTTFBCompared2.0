import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

integralAnswer=0.0
result=0
sError=0
s=0

errorTrack={l:{'n':[],'error':[]}for l in range(2)}


def errorPrintAddDictionary(sError, n):
    print(f"\nError: {sError}")
    errorTrack[0]['n'].append(n);
    errorTrack[0]['error'].append(sError)

def addDictionaryPredict(m, a,b,n):
    error=m*(pow(b-a,5))/(180*pow(n,4))
    errorTrack[1]['n'].append(n);
    errorTrack[1]['error'].append(error)


def simpsonsRule(func, a, b, n):
    if n % 2 != 0:
            n += 1

    deltaX=(b-a)/float(n)
    sum=func(a)+func(b)

    mult=deltaX/3.0

    for i in range(1,n):
        x=a+i*deltaX
        if i%2==0:
            sum+=2.0*func(x)
        else:
            sum+=4.0*func(x)

    print(f"\nSimpson's Rule approximation with {n} sunintervals: {sum*mult}")
    return sum*mult


print("\n1. Integral of x^2 from 0 to 3")
print("2. Integral of sin(x) from 0 to pi")
print("3. Integral of e^x from 0 to 1")

choice=int(input("\nChoose a well known integral: "))

if(choice<1 or choice>3):
    print("\nINVALID OPTION. TRY AGAIN NEXT TIME.")
elif (choice==1):
    integralAnswer=9.0;
    print(f"\nActual Answer: {integralAnswer}")

    def f(x):
        return x*x

    result, error=quad(f,0,3)

    s=simpsonsRule(f,0,3,10)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 10)

    
    s=simpsonsRule(f,0,3,50)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 50)

    s=simpsonsRule(f,0,3,100)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 100)

    addDictionaryPredict(0, 0,3,10)
    addDictionaryPredict(0, 0,3,50)
    addDictionaryPredict(0, 0,3,100)

elif choice==2:
    integralAnswer=2.0
    print(f"\nActual Answer: {integralAnswer}")

    def f(x):
        return np.sin(x)

    result, error=quad(f,0,np.pi)

    s=simpsonsRule(f,0,np.pi,10)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 10)
    
    s=simpsonsRule(f,0,np.pi,50)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 50)

    s=simpsonsRule(f,0,np.pi,100)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 100)

    addDictionaryPredict(1, 0,np.pi,10)
    addDictionaryPredict(1, 0,np.pi,50)
    addDictionaryPredict(1, 0,np.pi,100)

else:
    integralAnswer=np.e-1
    print(f"\nActual Answer: {integralAnswer}")

    def f(x):
        return np.exp(x)

    result, error=quad(f,0,1)

    s=simpsonsRule(f,0,1,10)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 10)
    
    s=simpsonsRule(f,0,1,50)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 50)

    s=simpsonsRule(f,0,1,100)
    sError = abs(integralAnswer - s)
    errorPrintAddDictionary(sError, 100)

    addDictionaryPredict(np.e, 0,1,10)
    addDictionaryPredict(np.e, 0,1,50)
    addDictionaryPredict(np.e, 0,1,100)

print(f"\nSimpson's Rule Scipy Approximation: {result}")
print(f"\nScipy Error: {error}")

plt.ticklabel_format(style='plain', useOffset=False, axis='y')
plt.title("Number of Subintervals vs Error: Predicted vs Actual Error lines Of Simpson's Rule Integration")
plt.xlabel("n(subintervals)")
plt.ylabel("Error")
plt.plot(errorTrack[0]['n'],errorTrack[0]['error'],label="Actual Error")
plt.plot(errorTrack[1]['n'],errorTrack[1]['error'],label="Predicted Error")
plt.legend()
plt.show()