import pandas
sözlük = {'Hakan Durmuş': {'Ara Sınav Notu': 65, 'Proje Notu': 90, 
                          'Final Notu': 85, 'Başarı Notu': 00},
          'Kağan Durmuş': {'Ara Sınav Notu': 90, 'Proje Notu': 85, 
                          'Final Notu': 75, 'Başarı Notu': 00},
          'Ecenaz Durmuş': {'Ara Sınav Notu': 95, 'Proje Notu': 85, 
                            'Final Notu': 80, 'Başarı Notu': 00},
          'Kerem Durmuş': {'Ara Sınav Notu': 95, 'Proje Notu': 95, 
                           'Final Notu': 85, 'Başarı Notu': 00},
          'Leyla Durmuş': {'Ara Sınav Notu': 80, 'Proje Notu': 75, 
                           'Final Notu': 65, 'Başarı Notu': 00}}

a0 = sözlük['Hakan Durmuş']['Ara Sınav Notu']*0.30 + sözlük['Hakan Durmuş']['Proje Notu']*0.30 + sözlük['Hakan Durmuş']['Final Notu']*0.40
a1 = sözlük['Kağan Durmuş']['Ara Sınav Notu']*0.30 + sözlük['Kağan Durmuş']['Proje Notu']*0.30 + sözlük['Kağan Durmuş']['Final Notu']*0.40
a2 = sözlük['Ecenaz Durmuş']['Ara Sınav Notu']*0.30 + sözlük['Ecenaz Durmuş']['Proje Notu']*0.30 + sözlük['Ecenaz Durmuş']['Final Notu']*0.40
a3 = sözlük['Kerem Durmuş']['Ara Sınav Notu']*0.30 + sözlük['Kerem Durmuş']['Proje Notu']*0.30 + sözlük['Kerem Durmuş']['Final Notu']*0.40
a4 = sözlük['Leyla Durmuş']['Ara Sınav Notu']*0.30 + sözlük['Leyla Durmuş']['Proje Notu']*0.30 + sözlük['Leyla Durmuş']['Final Notu']*0.40

sözlük['Hakan Durmuş']['Başarı Notu'] = a0
sözlük['Kağan Durmuş']['Başarı Notu'] = a1
sözlük['Ecenaz Durmuş']['Başarı Notu'] = a2
sözlük['Kerem Durmuş']['Başarı Notu'] = a3
sözlük['Leyla Durmuş']['Başarı Notu'] = a4


liste = [a0, a1, a2, a3, a4]
liste.sort()
print(liste)



    
    
    
    




