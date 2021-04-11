veriable = int(input("0 ile 10 arasında bir tam sayı seçiniz: "))
if 0 <= veriable <= 10:
	list = [i  for i in (range(veriable)) if i%2 == 0]
	print(list)
else:
	print("0 ile 10 arasında bir tam sayı girmelisiniz!!!")