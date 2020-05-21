from bs4 import BeautifulSoup
from createcsv import *
import requests
import csv
import os

# ==================== Функція для збору всіх реквізитів технічного паспорта будинку ====================
def total_mas1(html):
    soup = BeautifulSoup(html, 'lxml')
    mas0 = soup.find_all('td',class_='egine-cell-description')
    total1 = []
    for tx in mas0:
        t1 = tx.text.strip()
        if t1:
            total1.append(t1)
    if len(total1) > 0:
        if (total1[2] == 'Статус' and total1[3] == 'Характеристики будинку'):
            total1.insert(2, 'Не вказано')
        if (total1[22] == 'Серійний номер' and total1[23] == 'Дата будівлі'):
            total1.insert(23, 'Не вказано')
        if (total1[39] == 'Тип фундаменту' and total1[40] == 'Матеріал фундаменту'):
            total1.insert(40, 'Не вказано')
        if (total1[41] == 'Матеріал фундаменту' and total1[42] == 'Підвал'):
            total1.insert(42, 'Не вказано')
        if (total1[70] == 'Матеріал' and total1[71] == 'Вбудовані нежитлові приміщення'):
            total1.insert(71, 'Не вказано')
        if (total1[121] == 'Тип зливу' and total1[122] == 'Матеріал'):
            total1.insert(122, 'Не вказано')
        if (total1[129] == 'Тип' and total1[130] == 'Матеріал'):
            total1.insert(130, 'Не вказано')
        if (total1[131] == 'Матеріал' and total1[132] == 'Фасад'):
            total1.insert(132, 'Не вказано')
        if (total1[237] == 'Тип' and total1[238] == 'Опалення'):
            total1.insert(238, 'Не вказано')
        if (total1[244] == 'Тип' and total1[245] == 'Лічильник холодного водопостачання'):
            total1.insert(245, 'Не вказано')
        if (total1[287] == 'Назва послуги' and total1[288] == 'Назва послуги'):
            total1.insert(288, 'Не вказано')
        if (total1[289] == 'Назва послуги' and total1[290] == 'Назва послуги'):
            total1.insert(290, 'Не вказано')
        if (total1[291] == 'Назва послуги' and total1[292] == 'Наявність пандусів'):
            total1.insert(292, 'Не вказано')
    return total1

# ==================== Функція для збору всіх параметрів технічного паспорта будинку ====================
def total_mas2(html):
    soup = BeautifulSoup(html, 'lxml')
    mas0 = soup.find_all('td',class_='decoration-table-cell engine-cell-value')
    i = 0
    total2 = []
    for tx in mas0:
       t1 = tx.text.strip()
       if t1=='':
           t1 = 'Не вказано'
       total2.append(t1)
       i = i + 1
    return total2

# ============= Функція для зчитування основних вихідних даних з основного CSV файлу і передачі їх в програму =============
def base_date():
    file_path = 'zibrani_dani/0_perelik_budynkiv_ta_kodiv.csv'
    if os.path.exists(file_path) == True:
        key = []
        area = []
        street = []
        org = []
        house = []
        id = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file_csv:
            reader = csv.reader(file_csv, delimiter=',')
            for col in reader:
                key.append(col[0])
                area.append(col[1])
                street.append(col[2])
                org.append(col[3])
                house.append(col[4])
                id.append(col[5])
    return key[1:], area[1:], street[1:], org[1:], house[1:], id[1:]

# ============= Функція для отримання коду сторінки паспорта будинку по цього паспорта ==============
def load_html(id):
   ss = requests.Session()
   ss.get('https://www.municipal.kiev.ua/kiev/')
   path = 'https://www.municipal.kiev.ua/kiev/renderers/house/index.jsp?id='+id
   ss.get(path)
   ss.get('https://www.municipal.kiev.ua/kiev/renderers/house/info/index.jsp')
   ss.get('https://www.municipal.kiev.ua/kiev/renderers/house/menu.jsp?item=passport')
   ss.get('https://www.municipal.kiev.ua/kiev/renderers/engine/index.jsp?domain=passport')
   ss.get('https://www.municipal.kiev.ua/kiev/renderers/engine/menu.jsp?item=view')
   html = ss.get('https://www.municipal.kiev.ua/kiev/renderers/engine/content.jsp').text
   return html

# ==================== Основна (об'єднуюча) функція виконання програми ===========================

def prohr_parsynhu():
   key, area, street, org, house, id = base_date()
   count = len(key)
   for i in range(1, count):
       html = load_html(id[i])
       total1 = total_mas1(html)
       total2 = total_mas2(html)
       csv1(total1, total2, key[i], area[i], street[i], org[i], house[i])
       csv2(total1, key[i])
       csv3(total1, total2, key[i])
       csv4(total1, total2, key[i])
       csv5(total1, key[i])
       csv6(total1, key[i])
       csv7(total1, total2, key[i])
       csv8(total1, total2, key[i])
       csv9(total1, total2, key[i])
       csv10(total1, total2, key[i])
       csv11(total1, total2, key[i])
       csv12(total1, total2, key[i])
       csv13(total1, total2, key[i])
       csv14(total1, total2, key[i])
       csv15(total1, total2, key[i])
       csv16(total1, total2, key[i])
       csv17(total1, total2, key[i])
       csv18(total1, total2, key[i])
       csv19(total1, total2, key[i])
       csv20(total1, total2, key[i])
       csv21(total1, total2, key[i])
       csv22(total1, total2, key[i])
       csv23(total1, total2, key[i])
       csv24(total1, total2, key[i])
       csv25(total1, total2, key[i])
       csv26(total1, total2, key[i])
       csv27(total1, total2, key[i])
       csv28(total1, key[i])
       csv29(total1, key[i])
       csv30(total1, total2, key[i])
       csv31(total1, total2, key[i])
       csv32(total1, total2, key[i])
       csv33(total1, total2, key[i])
       csv34(total1, total2, key[i])
       csv35(total1, key[i])
       csv36(total1, total2, key[i])
   return


if __name__ == '__main__':
    main()
