import requests
import csv
import os

def main():
   ss = requests.Session()
   ss.get('https://www.municipal.kiev.ua/kiev/')
   json1 = ss.get('https://www.municipal.kiev.ua/kiev/daemons/locator?cmd=street&id=9298e5e4e3a1549e751e60d93b20a1ad').json()
   street = []
   kod1 = []
   mas1 = json1['data'][1:len(json1['data'])]
   file_path = 'zibrani_dani/0_perelik_budynkiv_ta_kodiv.csv'
   if os.path.exists(file_path) == False:
       with open(file_path, mode='w', newline='', encoding='utf-8') as f:
           writer = csv.writer(f)
           writer.writerow(('key', 'area', 'street', 'organization', 'house', 'id'))
   for tx1 in mas1:
       street.append(tx1['name'].strip())
       kod1.append(tx1['id'].strip())
   # max1 = len(kod1)
   i1 = 0
   for i in range(20, 25):
       path1 = 'https://www.municipal.kiev.ua/kiev/daemons/locator?cmd=house&id='+kod1[i]
       json2 = ss.get(path1).json()
       mas2 = json2['data'][1:len(json2['data'])]
       for tx2 in mas2:
           house = tx2['name'].strip()
           kod2 = tx2['id'].strip()
           path2 = 'https://www.municipal.kiev.ua/kiev/daemons/locator?cmd=district&id='+kod2
           area = ss.get(path2).text
           path3 = 'https://www.municipal.kiev.ua/kiev/daemons/locator?cmd=condominimum&id='+kod2
           json3 = ss.get(path3).json()
           mas3 = json3['data'][1:len(json3['data'])]
           for tx3 in mas3:
               i1 = i1 + 1
               id = tx3['id'].strip()
               org = tx3['name'].strip()
               with open(file_path, mode='a', newline='', encoding='utf-8') as f:
                   writer = csv.writer(f)
                   writer.writerow((i1, area, street[i], org, house, id))

if __name__ == '__main__':
    main()
 
