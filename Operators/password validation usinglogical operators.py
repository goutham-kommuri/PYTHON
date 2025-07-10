p='12345@6789'
if len(p)>= 8 and '@' in p and ' ' not in p:
    print("valid password")
else:
    print("invald password")
