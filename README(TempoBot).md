
Para fazer o bot de previsão do tempo funcionar

Python funcionando no pc ou seja instalar python no pc;

Crie uma pasta com o nome "Venv" para o anbiente venv;

Abra o terminal dessa pasta:
Coloque esse codigo python3 -m venv venv && source ./venv/bin/activate && which python;

Criação de um Bot no Telegram;

Acesso a uma API de Previsão do Tempo:
usou-se a OpenWeatherMap API. Para isso, foi necessário criar uma conta na OpenWeatherMap e obter uma chave de API para autenticação.

Configuração do Ambiente de Desenvolvimento:
Para desenvolver o bot, você configurou um ambiente de desenvolvimento Python. Certificou-se de que o Python estava instalado e usou o pip para instalar as bibliotecas python-telegram-bot e requests para interagir com o Telegram e fazer solicitações à API de previsão do tempo.

##Como funciona o codigo do Botempo:

-import requests
-from telegram import Update
-from telegram.ext import Updater, CommandHandler, CallbackContext

As linhas iniciais/acima são responsáveis por importar os módulos necessários. requests é usado para fazer solicitações HTTP à API da OpenWeatherMap, enquanto telegram e telegram.ext são bibliotecas para interagir com o Telegram e criar botões. Update é usado para representar uma atualização do Telegram, Updater é a classe principal para interagir com a API do Telegram, CommandHandler é usado para criar manipuladores de comandos e CallbackContext é usado para fornecer contexto.

-BOT_TOKEN = 'YOUR_BOT_TOKEN'
-WEATHER_API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
