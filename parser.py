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

        for k in range(1, table.shape[1]):
            business_roles = np.append(business_roles, table[0, k])

        for l in range(1, table.shape[0]):
            users = np.append(users, table[l, 0])

        for z in range(0,len(users)+1):
            for i in range(1, len(business_roles) + 1):
                if table[z, i] == 'x':
                    output_string = str(users[z - 1]) + ',' + str(business_roles[i - 1]) + '\n'
                    self.save_as_csv(output_string, 'PARSED_CSV.csv')

    def save_as_csv(self, input_text, file_name):
        with open(file_name, 'a') as file:
            file.write(input_text)

def main():
    Parser = CSV_Parser(sys.argv[1])
    Parser.transform_to_key_value_pairs()

if __name__ == '__main__':
    main()

