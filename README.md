## Informações
Python: v3.6.7

## Instalação
Ativar o ambiente virtual
- clone o repositório
- `cd spacexapi-client`
- `source spacexapi-client/bin/activate`

Desativar o ambiente virtual
- `deactivate`

## Execução do programa
- `python3 main.py`

## Execução dos testes unitários
- `python3 test_get_launch.py`

## Explicação da solução

Foram utilizadas as bibliotecas requests, para lidar com as requisições http, e unittests para realização dos testes unitários.

Na documentação do Postman da SpaceX foram identificados os endpoints correspondentes aos requeridos no desafio.

Foi então utilizado o requests para retornar as informações do endpoint.

Os dados foram selecionados, como esse ponto era de livre escolha do participante eu escolhi o número do võo, Nome da missão, ano do lançamento e detalhes da missão (em inglês).

O programa apresenta 4 opções de visualização de informações:
 1 - Próximo lançamento
 2 - Último lançamento
 3 - Próximos lançamentos (mostra as 4 informações de todos os lançamentos futuros)
 4 - Lançamentos passados (mostra as 4 informações de todos os lançamentos já realizados)

