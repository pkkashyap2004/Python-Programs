def CI(p,r,t):
    return (p * pow ((1+r/100),t) - p)
p = float(input("Enter Principal value : "))
r = float(input("Enter reate value : "))
t = float(input("Enter time : "))
compoundInterest = CI(p,r,t)
print("Entered compound Interest of products : ",compoundInterest)
