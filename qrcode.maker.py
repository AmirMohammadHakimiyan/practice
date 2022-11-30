import qrcode
name=input("wrait your name please")
number=input("wrait your number please")
lastname=input("wraet your last name")
wwww=name+number+lastname
x=qrcode.make(wwww)
x.save("qrcode.png")