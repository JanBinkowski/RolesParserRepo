import numpy as np
import csv
import sys


class CSV_Parser:
    global end_file_name
    end_file_name =  'PARSED_CSV.csv'


    def __init__(self, file_name):
        self.file_name = file_name


    def read_csv(self, path):
        with open(path, 'r') as f:
            data = list(csv.reader(f, delimiter=","))
        table = np.array(data,dtype=str)

        return table


    def extract_users_and_roles(self):
        global table
        table= self.read_csv(str(self.file_name))
        business_roles = []
        users = []

        for every_business_role in range(1, table.shape[1]):
            business_roles = np.append(business_roles, table[0, every_business_role])

        for every_user in range(1, table.shape[0]):
            users = np.append(users, table[every_user, 0])

        return users, business_roles


    def transform_to_key_value_pairs(self, mode):
        users, business_roles = self.extract_users_and_roles()

        for iter_in_every_user in range(0,len(users)+1):
            for iter_in_every_business_role in range(1, len(business_roles) + 1):
                if table[iter_in_every_user, iter_in_every_business_role] == 'x':
                    if mode == 'przecinek':
                        output_string = str(users[iter_in_every_user - 1]) + ',' + str(
                            business_roles[iter_in_every_business_role - 1]) + '\n'
                    elif mode == 'srednik':
                        output_string = str(users[iter_in_every_user - 1]) + ';' + str(
                            business_roles[iter_in_every_business_role - 1]) + '\n'
                    self.save_as_csv(output_string, end_file_name)


    def save_as_csv(self, input_text, file_name):
        with open(file_name, 'a') as file:
            file.write(input_text)


    def add_role_to_all_users(self,role_name):
        users, business_roles = self.extract_users_and_roles()
        for iter_in_every_user in range(0,len(users)+1):
            if iter_in_every_user > 0:
                output_string = users[iter_in_every_user - 1] + ';' + str(role_name) + '\n'
                self.save_as_csv(output_string, end_file_name)

def main():
    Parser = CSV_Parser(sys.argv[1])
    ans = True
    while ans:
        print("""
        1.Parsuj dane z oddzileaczem jako srednik (dla User Self Service) 
        2.Parsuj dane z oddzileaczem jako przecinek (dla Maintain Business Users/Roles)
        3.Dopisz 1 role do kazdego usera w pliku .csv
        4.Wyjdz
        """)
        ans = input()
        if ans == "1":
            Parser.transform_to_key_value_pairs('srednik')
            print('\n Dane sparsowane pomyslnie. Zapisane jako plik',str(end_file_name),'\n')
        elif ans == "2":
            Parser.transform_to_key_value_pairs('przecinek')
            print('\n Dane sparsowane pomyslnie. Zapisane jako plik',str(end_file_name),'\n')
        elif ans == "3":
            role_name = input('Wprowadz nazwe roli: ')
            if len(role_name) != 0:
                Parser.add_role_to_all_users(role_name)
                print('\nRola przypisana pomyslnie. Zapisane jako',str(end_file_name),'\n')
        elif ans == "4":
            print("\n Zamykanie ....\n")
            break
        elif ans != "":
            print("\n Niepoprawny wybor. Sprobuj ponownie.")

if __name__ == '__main__':
    main()

