import numpy as np
import csv
import sys

class CSV_Parser:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_csv(self, path):
        with open(path, 'r') as f:
            data = list(csv.reader(f, delimiter=","))
        table = np.array(data,dtype=str)

        return table

    def transform_to_key_value_pairs(self):
        table = self.read_csv(str(self.file_name))
        business_roles = []
        users = []

        for every_business_role in range(1, table.shape[1]):
            business_roles = np.append(business_roles, table[0, every_business_role])

        for every_user in range(1, table.shape[0]):
            users = np.append(users, table[every_user, 0])

        for iter_in_every_user in range(0,len(users)+1):
            for iter_in_every_business_role in range(1, len(business_roles) + 1):
                if table[iter_in_every_user, iter_in_every_business_role] == 'x':
                    output_string = str(users[iter_in_every_user - 1]) + ',' + str(business_roles[iter_in_every_business_role - 1]) + '\n'
                    self.save_as_csv(output_string, 'PARSED_CSV.csv')

    def save_as_csv(self, input_text, file_name):
        with open(file_name, 'a') as file:
            file.write(input_text)

def main():
    Parser = CSV_Parser(sys.argv[1])
    Parser.transform_to_key_value_pairs()

if __name__ == '__main__':
    main()

