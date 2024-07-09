import configparser

config = configparser.RawConfigParser()
config.read('./config.ini')
first_name = config.get('credentials', 'first_name')
last_name = config.get('credentials', 'last_name')
email = config.get('credentials', 'email')
password = config.get('credentials', 'password')
home_page = config.get('URLs', 'home_page')
sign_up_page = config.get('URLs', 'sign_up_page')
sign_in_page = config.get('URLs', 'sign_in_page')
men_page = config.get('URLs', 'men_page')

