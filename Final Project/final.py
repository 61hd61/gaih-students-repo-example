basl�k = """
==================================

GlobalAiHub Bilgi Yar��mas� Oyunu

==================================
"""

bilgi = """ 
Her Soru 10 Puan De�erindedir. Yar��mada
Ba�ar�l� Olabilmek ��in En Az 50 Puan Almal�s�n�z.
Cevaplar B�y�k/K���k Harflere Dikkat Ederek
Cevaplay�n�z. Yar��mada Ba�ar�lar!!!!! 

                                                        GlobalAiHub Ekibi
 """
print (basl�k)

print(bilgi)


def sor():
	puan = 0
	print("Soru1: ", "Tarihin s�f�r noktas� olarak bilinen, insanl�k tarihinin ilk somut kal�nt�lar�n�n bulundu�u G�bekli tepe hangi ilimizdedir?")
	c1 = input("1. Sorunun Cevab�: ")
	if c1 == '�anl�urfa':
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru2: ", "Tarihin bir ba�ka d�n�m noktas� olarak g�sterilir. Sultanahmet Meydan�'nda, Yerebatan Sarn�c� �st�nde yer al�r. �stanbul'a gelen turistlerin mutlaka u�rak yerleri aras�ndad�r. Bu �nl� dikili ta��n ad� nedir?")
	c2 = input("2. Sorunun Cevab�: ")
	if c2 == "Milenyum Ta��":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru3: ", "D�nyan�n en b�y�k deniz kazalar�ndan biri olarak tarihe ge�ti. 1912 y�l�nda 1.550 ki�iye mezar olan �nl� transatlanti�in ad� nedir? �d�ll� Filmlere konu olmu�tur")
	c3 = input("3. Sorunun Cevab�: ")
	if c3 == "Titanik":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru4: ", "D���nlerde ��lenlerde davulla birlikte �al�nan enstruman hangisidir??")
	c4 = input("4. Sorunun Cevab�: ")
	if c4 == "Zurna":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5
	
	print("Soru5: ", "Su�lular�n yakalanmas�nda kullan�lan en �nemli delillerden biridir, su�lunun geride b�rakt��� iz? ")
	c5 = input("5. Sorunun Cevab�: ")
	if c5 == "Parmak �zi":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru6: ", "�imdiki sorumuz ayd�nlatmada kulland���m�z �ok eski kadim bir ara�. Erimi� parafin i�ine pamuk ipli�i ile s�k��t�r�larak y�zlerce y�ld�r yap�l�r. Nedir bu ayd�nlatma arac�n�n ad�.")
	c6 = input("6. Sorunun Cevab�: ")
	if c6 == "Mum":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru7: ", "Bursa'n�n en �nl� tatl�s�d�r, Bursa'n�n bir il�esiyle ayn� ad� ta��r?")
	c7 = input("7. Sorunun Cevab�: ")
	if c7 == "Mustafa Kemal Pa�a tatl�s�" or c7 == "Kemalpa�a tatl�s�":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru8: ", "Haberle�menin eski dildeki ad� nedir? ")
	c8 = input("8. Sorunun Cevab�: ")
	if c8 == "Muhabere":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru9: ", "M�sade, izin veya ruhsat anlam�ndaki s�z")
	c9 = input("9. Sorunun Cevab�: ")
	if c9 == "Destur":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5

	print("Soru10: ", "Kap� kolu? Eski evlerin giri�lerine as�lan, zilden �nce s�k�a kulland���m�z, her biri sanat eseri gibi demir ve d�k�mden yap�lan bir ara�")
	c10 = input("10. Sorunun Cevab�: ")
	if c10 == "Tokmak":
		print("Cevab�n�z Do�ru")
		puan += 10
	else:
		print("Cevab�n�z Yanl��")
		puan -= 5
	
	
	if puan >= 50:
		print(f"Toplam Puan�n�z: {puan}. Tebrikler Yar��may� Ba��r�l� Bir �ekilde Tamamlad�n�z!!!")
	else:
		print(f"Toplam Puan�n�z: {puan}. Yar��mada Ge�erli Bir Puan Alamad�n�z!!!")
	
	
	
sor()




	

