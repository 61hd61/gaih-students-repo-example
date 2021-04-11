baslýk = """
==================================

GlobalAiHub Bilgi Yarýþmasý Oyunu

==================================
"""

bilgi = """ 
Her Soru 10 Puan Deðerindedir. Yarýþmada
Baþarýlý Olabilmek Ýçin En Az 50 Puan Almalýsýnýz.
Cevaplar Büyük/Küçük Harflere Dikkat Ederek
Cevaplayýnýz. Yarýþmada Baþarýlar!!!!! 

                                                        GlobalAiHub Ekibi
 """
print (baslýk)

print(bilgi)


def sor():
	puan = 0
	print("Soru1: ", "Tarihin sýfýr noktasý olarak bilinen, insanlýk tarihinin ilk somut kalýntýlarýnýn bulunduðu Göbekli tepe hangi ilimizdedir?")
	c1 = input("1. Sorunun Cevabý: ")
	if c1 == 'Þanlýurfa':
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru2: ", "Tarihin bir baþka dönüm noktasý olarak gösterilir. Sultanahmet Meydaný'nda, Yerebatan Sarnýcý üstünde yer alýr. Ýstanbul'a gelen turistlerin mutlaka uðrak yerleri arasýndadýr. Bu ünlü dikili taþýn adý nedir?")
	c2 = input("2. Sorunun Cevabý: ")
	if c2 == "Milenyum Taþý":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru3: ", "Dünyanýn en büyük deniz kazalarýndan biri olarak tarihe geçti. 1912 yýlýnda 1.550 kiþiye mezar olan ünlü transatlantiðin adý nedir? Ödüllü Filmlere konu olmuþtur")
	c3 = input("3. Sorunun Cevabý: ")
	if c3 == "Titanik":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru4: ", "Düðünlerde þölenlerde davulla birlikte çalýnan enstruman hangisidir??")
	c4 = input("4. Sorunun Cevabý: ")
	if c4 == "Zurna":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5
	
	print("Soru5: ", "Suçlularýn yakalanmasýnda kullanýlan en önemli delillerden biridir, suçlunun geride býraktýðý iz? ")
	c5 = input("5. Sorunun Cevabý: ")
	if c5 == "Parmak Ýzi":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru6: ", "Þimdiki sorumuz aydýnlatmada kullandýðýmýz çok eski kadim bir araç. Erimiþ parafin içine pamuk ipliði ile sýkýþtýrýlarak yüzlerce yýldýr yapýlýr. Nedir bu aydýnlatma aracýnýn adý.")
	c6 = input("6. Sorunun Cevabý: ")
	if c6 == "Mum":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru7: ", "Bursa'nýn en ünlü tatlýsýdýr, Bursa'nýn bir ilçesiyle ayný adý taþýr?")
	c7 = input("7. Sorunun Cevabý: ")
	if c7 == "Mustafa Kemal Paþa tatlýsý" or c7 == "Kemalpaþa tatlýsý":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru8: ", "Haberleþmenin eski dildeki adý nedir? ")
	c8 = input("8. Sorunun Cevabý: ")
	if c8 == "Muhabere":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru9: ", "Müsade, izin veya ruhsat anlamýndaki söz")
	c9 = input("9. Sorunun Cevabý: ")
	if c9 == "Destur":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5

	print("Soru10: ", "Kapý kolu? Eski evlerin giriþlerine asýlan, zilden önce sýkça kullandýðýmýz, her biri sanat eseri gibi demir ve dökümden yapýlan bir araç")
	c10 = input("10. Sorunun Cevabý: ")
	if c10 == "Tokmak":
		print("Cevabýnýz Doðru")
		puan += 10
	else:
		print("Cevabýnýz Yanlýþ")
		puan -= 5
	
	
	if puan >= 50:
		print(f"Toplam Puanýnýz: {puan}. Tebrikler Yarýþmayý Baþýrýlý Bir Þekilde Tamamladýnýz!!!")
	else:
		print(f"Toplam Puanýnýz: {puan}. Yarýþmada Geçerli Bir Puan Alamadýnýz!!!")
	
	
	
sor()




	

