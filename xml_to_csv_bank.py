from xml.etree import ElementTree
import os
import csv
import re


def xml_to_csv_bank(path_to_xml, dir_for_csv):
    parser = ElementTree.iterparse(path_to_xml)

    family_name_list = []
    given_name_list = []
    middle_name_list = []
    account_number_list = []
    amount_list = []

    for x, y in parser:
        a = re.findall(r'\w+', y.tag)
        if 'Фамилия' in a:
            family_name_list.append(y.text)
        if 'Имя' in a:
            given_name_list.append(y.text)
        if 'Отчество' in a:
            middle_name_list.append(y.text)
        if 'ЛицевойСчет' in a:
            account_number_list.append(y.text)
        if 'Сумма' in a:
            amount_list.append(y.text)

    staff_list = []
    for i in range(len(family_name_list)):
        staff_list.append({'account_number': account_number_list[i],
                           'name': str(family_name_list[i] + ' ' + given_name_list[i] + ' ' + middle_name_list[i]),
                           'amount': amount_list[i]})
    result_data_file = os.path.join(dir_for_csv, os.path.basename(path_to_xml).replace('.xml', '.csv'))
    result_data = open(result_data_file, 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(result_data)
    col_names = ['account_number', 'amount', 'name']
    csvwriter.writerow(col_names)
    for staff in staff_list:
        csvwriter.writerow((staff['account_number'],
                            staff['amount'],
                            staff['name']
                            ))
    return result_data_file


# x = xml_to_csv_bank(r'L:\P\.projects\xml_to_csv_bank\0000548z.xml', r'L:\P\.projects\xml_to_csv_bank')
# print(x)
