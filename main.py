from helper_functions import request_smhi_api, request_owm_api, create_excel, print_last_update

def fetch_data_from_smhi():
    try:
        print('Hämtar data från SMHI')
        create_excel(request_smhi_api())
    except Exception as e:
        print(f'Något gick fel: {e}')

def fetch_data_from_owm():
    try:
        print('Hämtar data från OpenWeatherMap')
        create_excel(request_owm_api())
    except Exception as e:
        print(f'Något gick fel: {e}')

def fetch_data_from_both():
    try:
        print('Hämtar data från SMHI och OpenWeatherMap')
        create_excel(request_smhi_api())
        create_excel(request_owm_api())
    except Exception as e:
        print(f'Något gick fel: {e}')

def print_smhi_forecast():
    print_last_update('SMHI')

def print_owm_forecast():
    print_last_update('OpenWeatherMap')

def data_menu():
    while True:
        print('\n   Hämta data: ')
        print('1. Hämta data från SMHI')
        print('2. Hämta data from OpenWeatherMap')
        print('3. Hämta data från både SMHI och OpenWeatherMap')
        print('9. Tillbaka')
        choice = input('Välj 1, 2, 3 eller 9: ')

        if choice == '1':
            fetch_data_from_smhi()
        elif choice == '2':
            fetch_data_from_owm()
        elif choice == '3':
            fetch_data_from_both()
        elif choice == '9':
            break

def forecast_menu():
    while True:
        print('\n   Skriv ut prognos:')
        print('1. Skriv ut prognos för SMHI')
        print('2. Skriv ut prognos för OpenWeatherMap')
        print('9. Tillbaka')
        choice = input('Välj 1, 2 eller 9: ')

        if choice == '1':
            print_smhi_forecast()
        elif choice == '2':
            print_owm_forecast()
        elif choice == '9':
            break

def main_menu():
    while True:
        print('\nVäderprognos från SMHI och OpenWeatherMap.')
        print('1. Hämta data')
        print('2. Skriv ut prognos')
        print('9. Avsluta')
        choice = input('Välj 1, 2 eller 9: ')

        if choice == '1':
            data_menu()
        elif choice == '2':
            forecast_menu()
        elif choice == '9':
            break

if __name__ == '__main__':
    main_menu()
