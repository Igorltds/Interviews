# question-3
import pandas as pd
import datetime as dt
import json

class Faturamento(): # faturamento_diario
    def __init__(self, locale='files/'): 
        self.locale = locale
    
    #Def's
    def start_json_df(self):
        try: 
            with open("files/faturamentos.json", 'r', encoding='utf-8') as file_json:
                self.__df = pd.read_json(json.load(file_json))
            print('Json Iniciado\n')
        except: 
            self.creat_json_df()
            self.start_json_df()
        

    def creat_json_df(self):
        self.__df = pd.DataFrame({
                                    "Date":["2022-08-04","2022-08-05","2002-08-06"],
                                    "Value":[200.00,300.00,200.00]
                                })
        self.df_to_date()
        self.save_df_in_json()
        print('Json criado')

    def df_to_date(self):
        date = self.__df["Date"]
        new_date = []
        for x in date:
            new_date.append(dt.datetime.strptime(x, '%Y-%m-%d').date())
        self.__df["Date"] = new_date



    def save_df_in_json(self):
        print(type(self.__df["Date"][0]))
        with open('files/faturamentos.json', "w", encoding='utf-8') as file_json:
            json.dump(self.__df.to_json(), file_json)
        print(type(self.__df["Date"][0]))

    def get_df(self):
        return self.__df
 
    

print("\nInicio\n")

# Instanciando classe
system = Faturamento()

# Iniciando DF
system.start_json_df()
system.df_to_date()

# others
print("\n ---\n ")
print(system.get_df())
print(type(system.get_df()["Date"][0]))


