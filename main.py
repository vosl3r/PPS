import pandas as pd
import datetime
from tabulate import tabulate

# PATH = '/home/lumpy/PycharmProjects/Addres/'

link_dataset = {
    "Перечень государственных учреждений по делам молодежи в Санкт-Петербурге":
        ["https://classif.gov.spb.ru/irsi/7830002078-Perechen-gosudarstvennyh-uchrezhdenij-po-delam-molodezhi-v-Sankt-Peterburge/structure_version/357/",
         "dataset/Perechen-gosudarstvennyh-uchrezhdenij-po-delam-molodezhi-v-Sankt-Peterburge.csv", "Адрес"],

    "Перечень государственных учреждений, подведомственных Комитету по социальной политике Санкт-Петербурга":
        [
            "https://classif.gov.spb.ru/irsi/7825675663-perechen-gosudarstvennyh-uchrezhdenij-podvedomstvennyh-Komitetu-po-socialnoj-politike-Sankt-Peterburga/structure_version/171/",
            "dataset/perechen-gosudarstvennyh-uchrezhdenij-podvedomstvennyh-Komitetu-po-socialnoj-politike-Sankt-Peterburga.csv", "Адрес"],
    "TEST":
        [
            "TEST",
            "dataset/test.csv",
            "Адрес"],
}


class Analitic():
    def __init__(self, path, colum):
        self.path = path
        self.colum = colum
        self.list_gorod = pd.read_csv("goroda/koord_russia.csv", delimiter=',')
        self.list_poch_index = pd.read_csv("goroda/postindexes_postindexes.csv", delimiter=',')
        self.list_gerion = pd.read_csv("goroda/region.csv", delimiter=',')


    # Взыращает датафрейм по столбцу адреса
    def read_csv_colum(self):
        col  = pd.read_csv(self.path, delimiter=',')
        return col[self.colum]

    # количество записей в наборе
    def count_csv(self):
        count_csv = pd.read_csv(self.path).count()
        return count_csv[0]

    # количество не пустых адресов
    def count_not_null_address(self):
        return self.read_csv_colum().count()



    # количество адресов, содержащих индекс
    def count_index_city(self):
        count_index = 0
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for gor in addr.split(','):
                    for index in self.list_poch_index["index"]:
                        if isinstance(index, int):
                            if gor.lower() == str(index).lower():
                                count_index = count_index+1
        # print(count_index)
        return  count_index

    # количество адресов, содержащих название региона"
    def count_region(self):
        count_region= 0
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for reg in addr.split(','):
                    for region in self.list_gerion["name"]:
                        if isinstance(region, str):
                            reg = reg.strip(",")
                            reg = reg.strip()
                            if reg.lower() == region.lower():
                                count_region = count_region + 1
        # print(count_region)
        return  count_region


    # количество адресов, содержащих название города
    # Все датасеты должны содержать разделитель для города ","
    def count_name_city(self):
        count_city = 0
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for gor in addr.split(','):
                    for gorod in self.list_gorod["Город"]:
                        if isinstance(gorod, str):
                            if gor.startswith("г."):
                                gor = gor.lstrip("г.")
                            elif gor.startswith("Г."):
                                gor = gor.lstrip("Г.")
                            if gor.lower() == gorod.lower() :
                                count_city = count_city+1
        # print(count_city)
        return  count_city

    # количество адресов, содержащих название улицы
    def street_count(self):
        count_street  = 0
        list_word_street = [ "улица", "ул.", ]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for street in addr.split():
                    street = street.strip(",")
                    if street in list_word_street:
                        count_street= count_street+1
        # print(count_street)
        return count_street


    # количество адресов, содержащих номер дома
    def home_count(self):
        count_home  = 0
        list_home_street = ["дома","дом","д.", ]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for home in addr.split():
                    home = home.strip(",")
                    if home in list_home_street:
                        count_home= count_home+1

                #Пусть пока тут полежит
                # addr  =addr.split()
                # for street in range(len(addr)-1):
                #     if addr[street] in list_home_street and addr[street+1].strip(",").isnumeric():
                        # print(addr[street])
                        # print(addr[street+1].strip(","))
        # print(count_home)
        return count_home


    # количество адресов, содержащих номер корпуса или строения
    def corpus_count(self):
        count_corpus  = 0
        list_corpus_street = ["корпус","к.", "стр."]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for corpus in addr.split():
                    corpus = corpus.strip(",")
                    if corpus in list_corpus_street:
                        count_corpus= count_corpus+1
        # print(count_corpus)
        return count_corpus


    # количество адресов, содержащих литеру
    def lit_count(self):
        count_liter  = 0
        list_liter_street = ["литера", "лит.", "литер", "лит"]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for liter in addr.split():
                    liter = liter.strip(",")
                    if liter in list_liter_street:
                        count_liter= count_liter+1
        # print(count_liter)
        return count_liter

    # количество адресов, содержащих номер помещения или квартиры
    def kv_count(self):
        count_kv  = 0
        list_kv= ["кв.", "пом.", "квартира"]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for kv in addr.split():
                    kv = kv.strip(",")
                    if kv in list_kv:
                        count_kv= count_kv+1
        # print(count_kv)
        return count_kv


    def view_table(self, namedataset, linkdataset ):
        newdata = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        data = [{'Название набора данных': namedataset, 'Ссылка на набор данных': linkdataset, 'Количество записей в наборе': self.count_csv(),
                 "Название столбца с адресом":self.colum, 'Количество не пустых адресов':self.count_not_null_address(),
                 'Количество адресов, содержащих индекс':self.count_index_city(),'Количество адресов, содержащих название региона':self.count_region(),
                 'Количество адресов, содержащих название города':self.count_name_city(),'Количество адресов, содержащих название улицы':self.street_count(),
                 'Количество адресов, содержащих номер дома':self.home_count(), 'Количество адресов, содержащих номер корпуса или строения':self.corpus_count(),
                 'Количество адресов, содержащих литеру':self.lit_count(), 'Количество адресов, содержащих номер помещения или квартиры':self.kv_count()
                 }]
        view = pd.DataFrame(data)
        view.to_csv(f"{namedataset}_{newdata}.csv", index=False)
        print(tabulate(view, headers=view.keys(), tablefmt="grid", showindex="always"))





if __name__=="__main__":
    for name, link in link_dataset.items():
        dt = Analitic(link[1], link[2], )
        dt.view_table(name, link[0])
    # print(dt.count_not_null_address())

