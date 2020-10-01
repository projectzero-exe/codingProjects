from pprint import pprint

import requests

base_url = 'https://restcountries.eu/rest/v2/'

"""
r = requests.get(base_url + 'name/iran')
json_result = r.json()

formatted = json.dumps(json_result, indent=4)

print(formatted)

"""
# print('What info would you like query about a country? Select and choose a number.\n 1. Population\n '
#       '2. Languages\n 3. Timezone')
# option = int(input(">>> "))
# print(f"You chose {option}.")

print('What country do you want that information for?')
country = input('>>> ')
#params = {'fields': 'population;languages;timezones', 'fullText': 'true'}

r = requests.get(base_url + f'name/{country}?')

json_result = r.json()
pprint(json_result)
#formatted = json.dumps(json_result, indent=4)
#
#pprint.pprint(json_result)

country = json_result[0]['borders']

print(country)
#
# if option == 1:
#     populus = country['population']
#     print('Population is: {}.'.format(populus))
#
# elif option == 2:
#     langs = []
#     for language in country['languages']:
#         langs.append(language['name'])
#     print('The languages are: {}'.format(', '.join(langs)))
#
# else:
#     timez = country['timezones']
#    print('The Timezones are: {}'.format(', '.join(timez)))