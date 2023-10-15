from helper_functions import *

def menu():
    mainmenu = True
    while mainmenu:
        print('\nVäderprognos från SMHI och OpenWeatherMap.')
        print('1. Hämta data')
        print('2. Skriv ut prognos')
        print('9. Avsluta')
        val_main = input('Välj 1, 2 eller 9: ')

        
        if val_main == '1':
            submenu1 = True
            while submenu1:
                print('\n   Hämta data: ')
                print('1. Hämta data från SMHI')
                print('2. Hämta data from OpenWeatherMap')
                print('3. Hämta data från både SMHI och OpenWeatherMap')
                print('9. Tillbaka')
                val1 = input('Välj 1, 2, 3 eller 9: ')
                
                if val1 == '1':
                    try:
                        print('Hämtar data från SMHI')
                        create_excel(smhi_data)
                    except:
                        print('Något gick fel')
                elif val1 == '2':
                    try:
                        print('Hämtar data från OpenWeatherMap')
                        create_excel(owm_data)
                    except:
                        print('Något gick fel')
                elif val1 == '3':
                    try:
                        print('Hämtar data från SMHI och OpenWeatherMap')
                        create_excel(smhi_data)
                        create_excel(owm_data)
                    except:
                        print('Något gick fel')
                elif val1 == '9':
                    submenu1 = False 
        
        elif val_main== '2':
            submenu2 = True
            while submenu2:
                print('\n   Skriv ut prognos:')
                print('1. Skriv ut prognos för SMHI')
                print('2. Skriv ut prognos för OpenWeatherMap')
                print('9. Tillbaka')
                val2 = input('Välj 1, 2 eller 9: ')

                if val2 == '1':
                    print_last_update('SMHI')
                elif val2 == '2':
                    print_last_update('OpenWeatherMap')
                elif val2 == '9':
                    submenu2 = False  

        elif val_main == '9':
            mainmenu = False


if __name__ == '__main__':
    menu()