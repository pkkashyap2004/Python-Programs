def cel_to_far(cel):
    far = cel * 9/5 +32
    return far
celt = float(input("Enter temperature in celsius : "))
fart=cel_to_far(celt)
print( "Entered temperature in farenhiet",fart)
