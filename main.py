import pandas as pd


class Analitic():
    def __init__(self, path, colum):
        self.path =  path
        self.colum = colum
        self.list_gorod = pd.read_csv("goroda/koord_russia.csv", delimiter=',')
        self.list_poch_index = pd.read_csv("goroda/postindexes_postindexes.csv", delimiter=',')

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
        print(count_index)
        return  count_index

    # количество адресов, содержащих название региона"



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
                                print(gor)
                                count_city = count_city+1
        print(count_city)
        return  count_city

    # количество адресов, содержащих название улицы
    def street_count(self):
        count_street  = 0
        list_word_street = [ "улица", "ул.", ]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for street in addr.split():
                    if street in list_word_street:
                        count_street= count_street+1
        print(count_street)
        return count_street


    # количество адресов, содержащих номер дома
    def home_count(self):
        count_home  = 0
        list_home_street = ["дома","дом","д.", ]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for street in addr.split():
                    if street in list_home_street:
                        count_home= count_home+1

                #Пусть пока тут полежит
                # addr  =addr.split()
                # for street in range(len(addr)-1):
                #     if addr[street] in list_home_street and addr[street+1].strip(",").isnumeric():
                        # print(addr[street])
                        # print(addr[street+1].strip(","))
        print(count_home)
        return count_home


    # количество адресов, содержащих номер корпуса или строения
    def corpus_count(self):
        count_corpus  = 0
        list_corpus_street = ["корпус","к.", "стр."]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for corpus in addr.split():
                    if corpus in list_corpus_street:
                        count_corpus= count_corpus+1
        print(count_corpus)
        return count_corpus


    # количество адресов, содержащих литеру
    def lit_count(self):
        count_liter  = 0
        list_liter_street = ["литера", "лит."]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for liter in addr.split():
                    if liter in list_liter_street:
                        count_liter= count_liter+1
        print(count_liter)
        return count_liter

    # количество адресов, содержащих номер помещения или квартиры
    def kv_count(self):
        count_kv  = 0
        list_kv= ["кв.", "пом.", "квартира"]
        for addr in self.read_csv_colum():
            if isinstance(addr, str):
                for kv in addr.split():
                    if kv in list_kv:
                        count_kv= count_kv+1
        print(count_kv)
        return count_kv



if __name__=="__main__":
    dt = Analitic("test.csv", "Адрес")
    # print(dt.count_not_null_address())
    dt.kv_count()
