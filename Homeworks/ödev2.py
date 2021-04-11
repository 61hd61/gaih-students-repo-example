
my_dic = {'user_name': 'hakan', 'password': '12345' }

for i in range(5):
	user_name1 = input("lütfen kullanıcı adınızı girin: ")
	password1 = input ("lütfen parolanızı girin: ")

	if my_dic['user_name'] != user_name1 and my_dic['password'] == password1:
		print("kullanıcı adınızı yanlış girdiniz!!!")
		i += 1
		
	elif my_dic['user_name'] == user_name1 and my_dic['password'] != password1:
		print("parolanızı yanlış girdiniz!!!")
		
		i += 1
	elif my_dic['user_name'] != user_name1 and my_dic['password'] != password1:
		print("kullanıcı adınız ve parolanız yanlış!!!")
		
		i += 1
	else:
		print("tebrikler doğru giriş yaptınız...")
		break
		print("kullanıcı adınız ve parolanız bloke oldu. lütfen müşteri hizmetlerini arayınız!!!")
