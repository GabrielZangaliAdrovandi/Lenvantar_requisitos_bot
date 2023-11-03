
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

Vou me referir ao código revisado que usa a biblioteca python-telegram-bot versão 12.x

import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

As linhas iniciais/acimas são responsáveis por importar os módulos necessários. requests é usado para fazer solicitações HTTP à API da OpenWeatherMap, enquanto telegram e telegram.ext são bibliotecas para interagir com o Telegram e criar botões. Update é usado para representar uma atualização do Telegram, Updater é a classe principal para interagir com a API do Telegram, CommandHandler é usado para criar manipuladores de comandos e CallbackContext é usado para fornecer contexto.


BOT_TOKEN = 'YOUR_BOT_TOKEN'
WEATHER_API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'

Essas duas linhas a cima definem constantes para o token do bot do Telegram e a chave da API da OpenWeatherMap. Substitua 'YOUR_BOT_TOKEN' e 'YOUR_OPENWEATHERMAP_API_KEY' pelos tokens reais que você obteve ao criar o bot no Telegram e a chave de API da OpenWeatherMap.



def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bem-vindo ao seu bot de previsão do tempo! Use /tempo [cidade] para verificar o tempo.")

Esta função, chamada start, é um manipulador de comando que é executado quando o usuário envia o comando /start. Ela recebe um objeto Update que contém informações sobre a atualização (a mensagem enviada pelo usuário) e um objeto CallbackContext. A função responde enviando uma mensagem de boas-vindas ao usuário.


def get_weather(update: Update, context: CallbackContext):
    city = " ".join(context.args)
    if not city:
        update.message.reply_text("Por favor, forneça uma cidade. Exemplo: /tempo São Paulo")
        return

A função get_weather é outro manipulador de comando. Ela é executada quando o usuário envia o comando /tempo [cidade]. A função recebe o nome da cidade como argumento. Se nenhum nome de cidade for fornecido, o bot responde pedindo ao usuário que forneça o nome da cidade.


   url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

Essas linhas constroem a URL para fazer uma solicitação à API da OpenWeatherMap, incluindo a cidade e a chave da API. Em seguida, o código faz uma solicitação GET para a URL e converte a resposta em um formato JSON.


   if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        update.message.reply_text(f"Em {city}: {weather_description}, temperatura: {temperature}°C")
    else:
        update.message.reply_text("Cidade não encontrada. Verifique a ortografia ou tente outra cidade.")

Essa parte do código verifica a resposta da API da OpenWeatherMap. Se o código de resposta for 200, isso significa que a cidade foi encontrada, e o bot responde com informações sobre o clima, incluindo a descrição do clima e a temperatura. Caso contrário, se a cidade não for encontrada, o bot informa ao usuário que a cidade não foi encontrada.


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tempo", get_weather, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

A função main é a função principal do programa. Ela cria uma instância do Updater com o token do bot e um objeto Dispatcher para gerenciar os comandos. Em seguida, ela adiciona dois manipuladores de comandos, um para /start e outro para /tempo. Finalmente, a função inicia o bot para receber atualizações e fica em execução continuamente.A linha if __name__ == "__main__": garante que o código seja executado apenas se o script for executado como um programa independente, não se for importado como um módulo.

