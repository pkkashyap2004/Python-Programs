def SI(p,r,t):
    return (p*r*t)/100
p = float(input("Enter principal value : "))
r = float(input("Enter rate value : "))
t = float(input("Enter time : "))
simpleInterest = SI(p,r,t)
print("Simple Interest of given values : ",simpleInterest)
