import json
def employees_rewrite(sort_type):
    with open('employees.json', 'r') as file1:
        data = json.load(file1)

    result = []
    for key, message in data.items():
        result = message

    data_formatted = [
        {
            'firstName': record['firstName'],
            'lastName': record['lastName'],
            'department': record['department'],
            'salary': str(record['salary']),
        }
        for record in result
    ]

    try:
        if sort_type == 'salary':
            sorted_list = sorted(data_formatted, key=lambda x: x[sort_type], reverse=True)
        else:
            sorted_list = sorted(data_formatted, key=lambda x: x[sort_type])
        data['employees'] = sorted_list

        json_data = json.dumps(data, indent=4)
        with open(f'employees_{sort_type}_sorted.json', "w") as file2:
            # json.dump(data, file2)
            file2.write(json_data)
    except KeyError:
        print('Bad key for sorting')
    #finally:
    #    print('Укажите правильный ключ')

employees_rewrite('firstName')
employees_rewrite('lastName')
employees_rewrite('department')
employees_rewrite('salary')
employees_rewrite('soft')
