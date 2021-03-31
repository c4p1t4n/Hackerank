def conversao(hora):
    
    if hora[-2:] == "AM" and hora[:2] == "12":
       return "00" + hora[2:-2]
    elif hora[-2:] == "AM":
       return hora[:-2]

    elif hora[-2:] == "PM" and hora[:2] == 12:
       return "12"+ hora[2:-2]
    else:
        return str(int(hora[:2]) + 12) + hora[2:8]
n=input()
s=str(n)
print (conversao(s))
