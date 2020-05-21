import csv
import os

# ==================== Формування CSV файлу із загальними характеристиками будинків ==================================

def csv1(total1, total2, key, area, street, org, house):
    xar1 = total1[5:36]
    if len(xar1) == 0:
        return
    xar2 = total2[2:17]
    column5 = column6 = column7 = column8 = column9 = column10 = column11 = column12 = column13 = column14 = column15 = ''
    column16 = column17 = column18 = column19 = column20 = column21 = column22 = column23 = column24 = column25 = ''
    column26 = column27 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar1[i+1]
        elif i == 6:
            column8 = xar1[i+1]
        elif i == 8:
            column9 = xar1[i+1]
        elif i == 10:
            column10 = xar1[i+1]
        elif i == 12:
            column11 = xar1[i+1]
        elif i == 14:
            column12 = xar2[0]
        elif i == 15:
            column13 = xar2[1]
        elif i == 16:
            column14 = xar2[2]
        elif i == 17:
            column15 = xar1[i+1]
        elif i == 19:
            column16 = xar2[3]
        elif i == 20:
            column17 = xar2[4]
        elif i == 21:
            column18 = xar2[5]
        elif i == 22:
            column19 = xar2[6]
        elif i == 23:
            column20 = xar2[7]
        elif i == 24:
            column21 = xar2[8]
        elif i == 25:
            column22 = xar2[9]
        elif i == 26:
            column23 = xar2[10]
        elif i == 27:
            column24 = xar2[11]
        elif i == 28:
            column25 = xar2[12]
        elif i == 29:
            column26 = xar2[13]
        elif i == 30:
            column27 = xar2[14]
        i = i + 1
    file_path = 'zibrani_dani/1_osnovni_pokaznyky_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Первинний ключ (код будинку в файлі)', 'Район міста', 'Найменування вулиці', 'Обслуговуюча організація', 'Номер будинку', 'Технічний стан', 'Форма власності',
                             'Форма управління', 'Статус', 'Клас пожежної безпеки', 'Тип забудови', 'Клас', 'Загальна площа будинку (м2)', 'Загальна площа житлових та нежитлових будинків (м2)',
                             'Площа житлових та нежитлових приміщень, які обслуговуються у суб\'єкта господарювання (м2)', 'Серійний номер', 'Дата будівлі', 'Дата капітального ремонту',
                             'Дата останнього ремонту', 'Кількість поверхів (низька секція)', 'Кількість поверхів (висока секція)', 'Загальна кількість квартир',
                             'Кількість приватизованих квартир', 'Кількість неприватизованих квартир', 'Кількість викуплених квартир', 'Загальна площа квартир житлового будинку (м2)',
                             'Житлова площа квартир (м2)', 'Кількість суб\'єктів господарювання в будинку (шт)'))
            writer.writerow(('kod', 'rayon', 'vulytsya', 'organization', 'budynok', 'tekhnichnyy_stan', 'forma_vlasnosti', 'forma_upravlinnya', 'status', 'klas_bezpeky', 'typ_zabudovy',
                             'klas', 'ploshcha_budynku', 'zhytlova_nezhytlova_ploshcha', 'ploshcha_inshykh_prymishchen', 'seriynyy_nomer', 'data_budivli',
                             'data_kap_remontu', 'data_ostan_remontu', 'kilk_poverkhiv1', 'kilk_poverkhiv2', 'zahalna_kilk_kvartyr', 'kilk_pryvat_kvartyr',
                             'kilk_nepryvat_kvartyr', 'kilk_vykupl_kvartyr', 'zahalna_ploshcha_kvartyr', 'zhytlova_ploshcha_kvartyr', 'kilk_subyektiv_hospodar'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, area, street, org, house, column5, column6, column7, column8, column9, column10, column11, column12, column13, column14, column15,
                         column16, column17, column18, column19, column20, column21, column22, column23, column24, column25, column26, column27))
    return

# ==================== Формування CSV файлу з характеристиками фундаментів будинків ==================================

def csv2(total1, key):
    xar1 = total1[37:43]
    if len(xar1) == 0:
       return
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/2_fundament_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан фундаменту',
                             'Тип фундаменту', 'Матеріал фундаменту'))
            writer.writerow(('kod', 'stan_fundamentu', 'typ_fundamentu', 'material_fundamentu'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками підвалів будинків ==================================

def csv3(total1, total2, key):
    xar1 = total1[44:49]
    if len(xar1) == 0:
       return
    xar2 = total2[19]
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2
        i = i + 1
    file_path = 'zibrani_dani/3_pidval_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність підвалу',
                             'Технічний стан', 'Площа підвалу (м2)'))
            writer.writerow(('kod', 'nayavnist_pidvalu', 'tekhnichnyy_stan', 'ploshcha pidvalu'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками несучих стін будинків ==================================

def csv4(total1, total2, key):
    xar1 = total1[50:62]
    if len(xar1) == 0:
       return
    xar2 = total2[21:25]
    column5 = column6 = column7 = column8 = column9 = column10 = column11 = column12 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar1[i+1]
        elif i == 6:
            column8 = xar2[0]
        elif i == 7:
            column9 = xar2[1]
        elif i == 8:
            column10 = xar1[i+1]
        elif i == 10:
            column11 = xar2[2]
        elif i == 11:
            column12 = xar2[3]
        i = i + 1
    file_path = 'zibrani_dani/4_nesuchi_stiny_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність несучих стін', 'Технічний стан', 'Матеріал зовнішніх стін',
                             'Мінімальна товщина (м)', 'Максимальна товщина (м)', 'Матеріал внутрішніх стін',
                             'Площа стін (м2)', 'Площа стель (м2)'))
            writer.writerow(('kod', 'nayavnist_nesuchykh_stin', 'tekhnichnyy_stan', 'material_zovnishnikh_stin',
                             'minimalna_tovshchyna', 'maksymalna_tovshchyna', 'material_vnutrishnikh_stin', 'ploshcha_stin', 'ploshcha stel'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9, column10, column11, column12))
    return

# ==================== Формування CSV файлу з характеристиками перекриттів будинків ==================================

def csv5(total1, key):
    xar1 = total1[63:67]
    if len(xar1) == 0:
       return
    column5 = column6 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/5_perekryttya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан перекриттів',
                             'Матеріал перекриттів'))
            writer.writerow(('kod', 'stan_perekryttiv', 'material_perekryttiv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6))
    return

# ==================== Формування CSV файлу з характеристиками внутрішніх перегородок будинків ==================================

def csv6(total1, key):
    xar1 = total1[68:72]
    if len(xar1) == 0:
       return
    column5 = column6 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/6_vnutríshní_peregorodki.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність внутрішніх перегородок',
                             'Матеріал внутрішніх перегородок'))
            writer.writerow(('kod', 'nayavnist_perehorodok', 'material_perehorodok'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6))
    return

# ==================== Формування CSV файлу з характеристиками вбудованих нежитлових приміщень будинків ==================================

def csv7(total1, total2, key):
    xar1 = total1[73:80]
    if len(xar1) == 0:
       return
    xar2 = total2[28:31]
    column5 = column6 = column7 = column8 = column9 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        i = i + 1
    file_path = 'zibrani_dani/7_vbudovani_prymishchennya.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність вбудованих нежитлових приміщень', 'Технічний стан приміщень',
                             'Площа приміщень (м2)', 'Площа приватизованих приміщень (м2)', 'Площа орендованих приміщень (м2)'))
            writer.writerow(('kod', 'nayavnist_vbudovanykh_prymishchen', 'tekhnichnyy_stan',
                             'ploshcha_prymishchen', 'ploshcha_pryvat_prymishchen', 'ploshcha_orendov_prymishchen'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9))
    return

# ==================== Формування CSV файлу з характеристиками технічних поверхів будинків ==================================

def csv8(total1, total2, key):
    xar1 = total1[81:86]
    if len(xar1) == 0:
       return
    xar2 = total2[32]
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2
        i = i + 1
    file_path = 'zibrani_dani/8_tekhnichnyy_poverkh_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність технічного поверху', 'Технічний стан',
                             'Площа технічного поверху (м2)'))
            writer.writerow(('kod', 'nayavnist_poverkhu', 'tekhnichnyy_stan',
                             'ploshcha_tekhnichnoho_poverkhu'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками цоколів будинків ==================================

def csv9(total1, total2, key):
    xar1 = total1[87:92]
    if len(xar1) == 0:
       return
    xar2 = total2[34]
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2
        i = i + 1
    file_path = 'zibrani_dani/9_tsokol_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність цоколя', 'Технічний стан', 'Площа цоколя (м2)'))
            writer.writerow(('kod', 'nayavnist_tsokolya', 'tekhnichnyy_stan', 'ploshcha_tsokolya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками сходових клітин будинків ==================================

def csv10(total1, total2, key):
    xar1 = total1[93:99]
    if len(xar1) == 0:
       return
    xar2 = total2[36:40]
    column5 = column6 = column7 = column8 = column9 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar2[0]
        elif i == 3:
            column7 = xar2[1]
        elif i == 4:
            column8 = xar2[2]
        elif i == 5:
            column9 = xar2[3]
        i = i + 1
    file_path = 'zibrani_dani/10_skhodovi_klitky_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Стан сходових клітін', 'Площа сходових клітін (м2)', 'Площа першого поверху (м2)',
                             'Площа інших поверхів (м2)', 'Площа прибирання (м2)'))
            writer.writerow(('kod', 'stan_skhodovykh_klitin', 'ploshcha_skhodovykh_klitin',
                             'ploshcha_pershoho_poverkhu', 'ploshcha_inshykh_poverkhiv', 'ploshcha_prybyrannya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9))
    return

# ==================== Формування CSV файлу з характеристиками ліфтів будинків ==================================

def csv11(total1, total2, key):
    xar1 = total1[100:109]
    if len(xar1) == 0:
       return
    xar2 = total2[41:47]
    column5 = column6 = column7 = column8 = column9 = column10 = column11 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        elif i == 7:
            column10 = xar2[3]
        elif i == 8:
            column11 = xar2[4]
        i = i + 1
    file_path = 'zibrani_dani/11_lifty_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність ліфтів', 'Технічний стан', 'Загальна кількість (шт)',
                             'Кількість пасажирських ліфтів (шт)', 'Кількість вантажних ліфтів (шт)', 'Дата встановлення', 'Дата модернізації'))
            writer.writerow(('kod', 'nayavnist_liftiv', 'tekhnichnyy_stan', 'zahalna_kilkist', 'kilkist_pasazhyrskykh_liftiv',
                             'kilkist_vantazhnykh_liftiv', 'data_vstanovlennya', 'data_modernizatsiyi'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9, column10, column11))
    return

# ==================== Формування CSV файлу з характеристиками горищ будинків ==================================

def csv12(total1, total2, key):
    xar1 = total1[110:115]
    if len(xar1) == 0:
       return
    xar2 = total2[47]
    column5 = column6 = column7 =  ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2
        i = i + 1
    file_path = 'zibrani_dani/12_horyshcha_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність горища', 'Технічний стан', 'Площа горища (м2)'))
            writer.writerow(('kod', 'nayavnist_horyshcha', 'tekhnichnyy_stan', 'ploshcha_horyshcha'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками дахів будинків ==================================

def csv13(total1, total2, key):
    xar1 = total1[116:125]
    if len(xar1) == 0:
       return
    xar2 = total2[49]
    column5 = column6 = column7 = column8 = column9 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar2
        elif i == 3:
            column7 = xar1[i+1]
        elif i == 5:
            column8 = xar1[i+1]
        elif i == 7:
            column9 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/13_dakh_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан даху', 'Площа даху (м2)', 'Форма', 'Тип зливу', 'Матеріал даху'))
            writer.writerow(('kod', 'tekhnichnyy_stan', 'ploshcha_dakhu', 'forma', 'typ_zlyvu', 'material_dakhu'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9))
    return

# ==================== Формування CSV файлу з характеристиками покрівлі будинків ==================================

def csv14(total1, total2, key):
    xar1 = total1[126:133]
    if len(xar1) == 0:
       return
    xar2 = total2[51]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar2
        elif i == 3:
            column7 = xar1[i+1]
        elif i == 5:
            column8 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/14_pokrivlya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан покрівлі', 'Площа покрівлі (м2)', 'Тип покрівлі', 'Матеріал покрівлі'))
            writer.writerow(('kod', 'tekhnichnyy_stan', 'ploshcha_pokrivli', 'typ_pokrivli', 'material_pokrivli'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками фасадів будинків ==================================

def csv15(total1, total2, key):
    xar1 = total1[134:137]
    if len(xar1) == 0:
       return
    xar2 = total2[53]
    column5 = column6 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar2
        i = i + 1
    file_path = 'zibrani_dani/15_fasad_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан', 'Площа фасаду (м2)'))
            writer.writerow(('kod', 'tekhnichnyy_stan', 'ploshcha fasadu'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6))
    return

# ==================== Формування CSV файлу з характеристиками під'їздів будинків ==================================

def csv16(total1, total2, key):
    xar1 = total1[138:147]
    if len(xar1) == 0:
       return
    xar2 = total2[55:60]
    column5 = column6 = column7 = column8 = column9 = column10 = column11 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        elif i == 7:
            column10 = xar2[3]
        elif i == 8:
            column11 = xar2[4]
        i = i + 1
    file_path = 'zibrani_dani/16_pidyizdy_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність під\'їздів', 'Технічний стан', 'Кількість під\'їздів (шт)', 'Площа (м2)',
                             'Площа підлоги (м2)', 'Площа стін під фарбування (м2)', 'Площа стін, стелі під побілення (м2)'))
            writer.writerow(('kod', 'nayavnist_pidyizdiv', 'tekhnichnyy_stan', 'kilkist_pidyizdiv', 'ploshcha', 'ploshcha_pidlohy',
                             'ploshcha_pid_farbuvannya', 'ploshcha_pid_pobilennya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9, column10, column11))
    return

# ==================== Формування CSV файлу з характеристиками місць для консьєржів ==================================

def csv17(total1, total2, key):
    xar1 = total1[148:156]
    if len(xar1) == 0:
       return
    xar2 = total2[61:63]
    column5 = column6 = column7 = column8 = column9 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/17_mistsya_dlya_konsyerzhiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність місць для консьєржів', 'Технічний стан', 'Кількість місць (шт)',
                             'Кількість консьєржів (особи)', 'Технічна можливість устаткування'))
            writer.writerow(('kod', 'nayavnist_mists_konsyerzhiv', 'tekhnichnyy_stan', 'kilkist_mists', 'kilkist_konsyerzhiv',
                             'mozhlyvist_ustatkuvannya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9))
    return

# ==================== Формування CSV файлу з характеристиками прибудинкових територій ==================================

def csv18(total1, total2, key):
    xar1 = total1[157:166]
    if len(xar1) == 0:
       return
    xar2 = total2[64:69]
    column5 = column6 = column7 = column8 = column9 = column10 = column11 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        elif i == 7:
            column10 = xar2[3]
        elif i == 8:
            column11 = xar2[4]
        i = i + 1
    file_path = 'zibrani_dani/18_prybudynkova_terytoriya.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність прибудинкової території', 'Технічний стан', 'Площа проїздів та вулиць (м2)',
                             'Площа будівлі (абрис) (м2)', 'Площа дворів (асфальт) (м2)', 'Озелення територій (газонів, вулиць) (м2)', 'Озелення територій (газонів, дворів) (м2)'))
            writer.writerow(('kod', 'nayavnist_prybudynkovoyi_terytoriyi', 'tekhnichnyy_stan', 'ploshcha_proyizdiv',
                             'ploshcha_budivli_abrys', 'ploshcha_dvoriv', 'ozelennya_vulyts', 'ozelennya_dvoriv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9, column10, column11))
    return

# ==================== Формування CSV файлу з характеристиками ґанків будинків ==================================

def csv19(total1, total2, key):
    xar1 = total1[167:172]
    if len(xar1) == 0:
       return
    xar2 = total2[70]
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        i = i + 1
    file_path = 'zibrani_dani/19_ganky_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність ганку', 'Технічний стан', 'Площа ганку (м2)'))
            writer.writerow(('kod', 'nayavnist_hanku', 'tekhnichnyy_stan', 'ploshcha hanku'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками дитячих майданчиків ==================================

def csv20(total1, total2, key):
    xar1 = total1[173:179]
    if len(xar1) == 0:
       return
    xar2 = total2[72:74]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/20_dytyachi_maydanchyky.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність дитячих майданчиків', 'Технічний стан', 'Кількість дитячих майданчиків (шт)', 'Площа (м2)'))
            writer.writerow(('kod', 'nayavnist_maydanchykiv', 'tekhnichnyy_stan', 'kilkist_maydanchykiv', 'ploshcha'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками спортивних майданчиків ==================================

def csv21(total1, total2, key):
    xar1 = total1[180:186]
    if len(xar1) == 0:
       return
    xar2 = total2[75:77]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/21_sportyvni_maydanchyky.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність спортивних майданчиків', 'Технічний стан', 'Площа спортивних майданчиків (м2)', 'Кількість (шт)'))
            writer.writerow(('kod', 'nayavnist_maydanchykiv', 'tekhnichnyy_stan', 'ploshcha_maydanchykiv', 'kilkist'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками майданчиків для відпочинку ==================================

def csv22(total1, total2, key):
    xar1 = total1[187:193]
    if len(xar1) == 0:
       return
    xar2 = total2[78:80]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/22_maydanchyky_dlya_vidpochynku.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність майданчиків для відпочинку', 'Технічний стан', 'Кількість майданчиків (шт)', 'Площа (м2)'))
            writer.writerow(('kod', 'nayavnist_maydanchykiv', 'tekhnichnyy_stan', 'kilkist_maydanchykiv', 'ploshcha'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками господарських майданчиків ==================================

def csv23(total1, total2, key):
    xar1 = total1[194:200]
    if len(xar1) == 0:
       return
    xar2 = total2[81:83]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/23_hospodarski_ploshchadky.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність господарської площадки', 'Технічний стан', 'Кількість площадок (шт)', 'Площа (м2)'))
            writer.writerow(('kod', 'nayavnist_ploshchadok', 'tekhnichnyy_stan', 'kilkist_ploshchadok', 'ploshcha'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками стоянок для автотранспорту ==================================

def csv24(total1, total2, key):
    xar1 = total1[201:209]
    if len(xar1) == 0:
       return
    xar2 = total2[84:86]
    column5 = column6 = column7 = column8 = column9 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/24_stoyanky_dlya_avtotransportu.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність стоянок для автотранспорту', 'Технічний стан', 'Кількість стоянок (шт)',
                             'Площа стоянок (м2)', 'Технічна можливість устаткування'))
            writer.writerow(('kod', 'nayavnist_stoyanok_avtotransportu', 'tekhnichnyy_stan', 'kilkist_stoyanok', 'ploshcha_stoyanok', 'mozhlyvist_ustatkuvannya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9))
    return

# ==================== Формування CSV файлу з характеристиками димовентиляційних каналів будинків ==================================

def csv25(total1, total2, key):
    xar1 = total1[210:215]
    if len(xar1) == 0:
       return
    xar2 = total2[87:90]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar2[0]
        elif i == 3:
            column7 = xar2[1]
        elif i == 4:
            column8 = xar2[2]
        i = i + 1
    file_path = 'zibrani_dani/25_dymoventylyatsiyni_kanaly_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан', 'Кількість димовентиляційних каналів (шт)', 'Кількість димоходів (шт)',
                             'Кількість вентиляційних каналів (шт)'))
            writer.writerow(('kod', 'tekhnichnyy_stan', 'kilkist_dym_kanaliv', 'kilkist_dymokhodiv', 'kilkist_vent_kanaliv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками холодного водопостачання будинків ==================================

def csv26(total1, total2, key):
    xar1 = total1[216:224]
    if len(xar1) == 0:
       return
    xar2 = total2[91:95]
    column5 = column6 = column7 = column8 = column9 = column10 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        elif i == 7:
            column10 = xar2[3]
        i = i + 1
    file_path = 'zibrani_dani/26_kholodne_vodopostachannya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність холодного водопостачання', 'Технічний стан', 'Загальна протяжність (п.м.)', 'Протяжність д. 15 (п.м.)',
                             'Протяжність д. 20 (п.м.)', 'Протяжність д. 50 (п.м.)'))
            writer.writerow(('kod', 'nayavnist_khol_vodopostachannya', 'tekhnichnyy_stan', 'zahalna_protyazhnist', 'protyazhnist_d_15',
                             'protyazhnist_d_20', 'protyazhnist_d_50'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9, column10))
    return

# ==================== Формування CSV файлу з характеристиками водовідведення для будинків ==================================

def csv27(total1, total2, key):
    xar1 = total1[225:232]
    if len(xar1) == 0:
       return
    xar2 = total2[96:99]
    column5 = column6 = column7 = column8 = column9 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        i = i + 1
    file_path = 'zibrani_dani/27_vodovidvedennya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність водовідведення', 'Технічний стан', 'Загальна протяжність (п.м.)',
                             'Протяжність д. 50 (п.м.)', 'Протяжність д. 110 (п.м.)'))
            writer.writerow(('kod', 'nayavnist_vodovidvedennya', 'tekhnichnyy_stan', 'zahalna_protyazhnist', 'protyazhnist_d_50',
                             'protyazhnist_d_110'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9))
    return

# ==================== Формування CSV файлу з характеристиками гарячого водопостачання для будинків ==================================

def csv28(total1, key):
    xar1 = total1[233:239]
    if len(xar1) == 0:
       return
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/28_haryache_vodopostachannya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність гарячого водопостачання', 'Технічний стан', 'Тип гарячого водопостачання'))
            writer.writerow(('kod', 'nayavnist_haryach_vodopostachannya', 'tekhnichnyy_stan',
                             'typ_haryach_vodopostachannya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками опалення для будинків ==================================

def csv29(total1, key):
    xar1 = total1[240:246]
    if len(xar1) == 0:
       return
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/29_opalennya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність опалення', 'Технічний стан', 'Тип опалення'))
            writer.writerow(('kod', 'nayavnist_opalennya', 'tekhnichnyy_stan', 'typ_opalennya'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками лічильників холодного водопостачання ==================================

def csv30(total1, total2, key):
    xar1 = total1[247:253]
    if len(xar1) == 0:
       return
    xar2 = total2[102:104]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/30_lichylnyky_kholodnoho_vodopostachannya.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність лічильників холодного водопостачання', 'Технічний стан',
                             'Кількість лічильників (шт)', 'Дата встановлення лічильників'))
            writer.writerow(('kod', 'nayavnist_lichyl_khol_vodopost', 'tekhnichnyy_stan', 'kilkist_lichylnykiv', 'data_vstanovlennya_lichylnykiv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками лічильників гарячого водопостачання ==================================

def csv31(total1, total2, key):
    xar1 = total1[254:260]
    if len(xar1) == 0:
       return
    xar2 = total2[105:107]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/31_lichylnyky_haryachoho_vodopostachannya.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність лічильників гарячого водопостачання', 'Технічний стан',
                             'Кількість лічильників (шт)', 'Дата встановлення лічильників'))
            writer.writerow(('kod', 'nayavnist_lichyl_haryach_vodopost', 'tekhnichnyy_stan', 'kilkist_lichylnykiv', 'data_vstanovlennya_lichylnykiv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками лічильників теплової енергії ==================================

def csv32(total1, total2, key):
    xar1 = total1[261:267]
    if len(xar1) == 0:
       return
    xar2 = total2[108:110]
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        i = i + 1
    file_path = 'zibrani_dani/32_lichylnyky_teplovoyi_enerhiyi.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність лічильників теплової енергії', 'Технічний стан',
                             'Кількість лічильників (шт)', 'Дата встановлення лічильників'))
            writer.writerow(('kod', 'nayavnist_lichyl_teplovoyi_enerhiyi', 'tekhnichnyy_stan', 'kilkist_lichylnykiv',
                             'data_vstanovlennya_lichylnykiv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу з характеристиками електрообладнання будинків ==================================

def csv33(total1, total2, key):
    xar1 = total1[268:278]
    if len(xar1) == 0:
       return
    xar2 = total2[111:117]
    column5 = column6 = column7 = column8 = column9 = column10 = column11 = column12 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2[0]
        elif i == 5:
            column8 = xar2[1]
        elif i == 6:
            column9 = xar2[2]
        elif i == 7:
            column10 = xar2[3]
        elif i == 8:
            column11 = xar2[4]
        elif i == 9:
            column12 = xar2[5]
        i = i + 1
    file_path = 'zibrani_dani/33_elektroobladnannya_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Технічний стан', 'Встановлено електроплити', 'Кількість електроплит (шт)',
                             'Загальна протяжність (п.м.)', 'Протяжність по стояках (п.м.)', 'Протяжність по підвалу (п.м.)',
                             'Кількість щитових (шт)', 'Кількість електроенергії (кВт/рік)'))
            writer.writerow(('kod', 'tekhnichnyy_stan', 'vstanovleno_elektroplyty', 'kilkist_elektroplyt', 'zahalna_protyazhnist',
                             'protyazhnist_po_stoyakakh', 'protyazhnist_po_pidvalu', 'kilkist_shchytovykh', 'kilkist_elektroenerhiyi'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8, column9, column10, column11, column12))
    return

# ==================== Формування CSV файлу з характеристиками газового господарства будинків ==================================

def csv34(total1, total2, key):
    xar1 = total1[279:284]
    if len(xar1) == 0:
       return
    xar2 = total2[118]
    column5 = column6 = column7 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar2
        i = i + 1
    file_path = 'zibrani_dani/34_hazove_hospodarstvo_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність газового господарства', 'Технічний стан', 'Загальна протяжність (п.м.)'))
            writer.writerow(('kod', 'nayavnist_hazovoho_hospodarstva', 'tekhnichnyy_stan', 'zahalna_protyazhnist'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7))
    return

# ==================== Формування CSV файлу з характеристиками комутаційних зручностей будинків ==================================

def csv35(total1, key):
    xar1 = total1[285:293]
    if len(xar1) == 0:
       return
    column5 = column6 = column7 = column8 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar1[i+1]
        elif i == 4:
            column7 = xar1[i+1]
        elif i == 6:
            column8 = xar1[i+1]
        i = i + 1
    file_path = 'zibrani_dani/35_komutatsiyni_zruchnosti_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Наявність комутаційних зручностей', 'Назва послуги 1', 'Назва послуги 2', 'Назва послуги 3'))
            writer.writerow(('kod', 'nayavnist_komut_zruchnostey', 'nazva_posluhy1', 'nazva_posluhy2', 'nazva_posluhy3'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6, column7, column8))
    return

# ==================== Формування CSV файлу який визначає наявність і кількість пандусів при будинках ==================================

def csv36(total1, total2, key):
    xar1 = total1[294:297]
    if len(xar1) == 0:
       return
    xar2 = total2[121]
    column5 = column6 = ''
    i = 0
    for tx in xar1:
        if i == 0:
            column5 = xar1[i+1]
        elif i == 2:
            column6 = xar2
        i = i + 1
    file_path = 'zibrani_dani/36_nayavnist_pandusiv_budynkiv.csv'
    if os.path.exists(file_path) == False:
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(('Код будинку в файлі', 'Чи існують пандуси', 'кількість пандусів (шт)'))
            writer.writerow(('kod', 'chy_isnuyut_pandusy', 'kilkist_pandusiv'))
    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((key, column5, column6))
    return


if __name__ == '__main__':
    main()
