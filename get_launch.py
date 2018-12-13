import json
import requests

base_url = 'https://api.spacexdata.com/v3/launches/'
payload = {}
headers = {'Content-Type': 'application/json'}


def get_launch_info(argument):
	# Deals with the api, getting the information and identifying errors
	api_url = base_url + str(argument)
	response = requests.request('GET', api_url, headers = headers, data = payload, allow_redirects = False)
    
	if response.status_code >= 500:
		print('[!] [{0}] Erro no Servidor'.format(response.status_code))
		return None
	elif response.status_code == 404:
		print('[!] [{0}] URL não encontrada: [{1}]'.format(response.status_code,api_url))
		return None  
	elif response.status_code == 401:
		print('[!] [{0}] Falha de autenticação'.format(response.status_code))
		return None
	elif response.status_code == 400:
		print('[!] [{0}] Solicitação inválida'.format(response.status_code))
		return None
	elif response.status_code >= 300:
		print('[!] [{0}] Redirecionamento inesperado'.format(response.status_code))
		return None
	elif response.status_code == 200:
		return  json.loads(response.content.decode('utf-8'))
	else:
		print('[?] Erro inesperado: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
	return None

def print_launch_information(launch):
	# Print the information on the screen for 1 launch only
	if launch is not None:
		print('\nNúmero do Vôo: ' + str(launch['flight_number']))
		print('Nome da missão: ' + str(launch['mission_name']))
		print('Ano do lançamento: ' + str(launch['launch_year']))
		print('Detalhes: ' + str(launch['details']))
		return launch
	else:
		print('[!] Solicitação inválida')
		return None

def print_launches_information(launches):
	# Print the information on the screen for 2 or more launches
	if launches is not None:
		for k in launches:
			print('\nNúmero do Vôo: ' + str(k['flight_number']))
			print('Nome da missão: ' + str(k['mission_name']))
			print('Ano do lançamento: ' + str(k['launch_year']))
			print('Detalhes: ' + str(k['details']))
		return launches
	else:
		print('[!] Solicitação inválida')
		return None

def print_information():
	# menu of choices
	print('O que você deseja visualizar?')
	print('\n1 - Próximo Lançamento')
	print('2 - Último Lançamento')
	print('3 - Próximos Lançamentos')
	print('4 - Lançamentos Passados')

	option = input('\nInsira uma opção: ')
	
	if option == '1':
		next_launch = get_launch_info('next')
		print('\nINFORMAÇÕES DO PRÓXIMO LANÇAMENTO')
		print_launch_information(next_launch)
		return 1

	elif option == '2':
		latest_launch = get_launch_info('latest')
		print('\nINFORMAÇÕES DO ÚLTIMO LANÇAMENTO')
		print_launch_information(latest_launch)
		return 2

	elif option == '3':
		upcoming_launches = get_launch_info('upcoming')
		print('\nINFORMAÇÕES DOS PRÓXIMOS LANÇAMENTOS')
		print_launches_information(upcoming_launches)
		return 3

	elif option == '4':
		past_launches = get_launch_info('past')
		print('\nINFORMAÇÕES DOS LANÇAMENTOS PASSADOS')
		print_launches_information(past_launches)
		return 4
	else:
		print('\n[!] Opção inválida, escolha um número de 1 a 4.\n')
		return -1