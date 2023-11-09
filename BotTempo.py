import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# trocar a 'YOUR_BOT_TOKEN' pelo token do seu bot do Telegram
BOT_TOKEN = '6560484151:AAHFqSp7c98OQKSVn2hft2b7L0zz7q3WsIU'
# trocar a'YOUR_OPENWEATHERMAP_API_KEY' pela sua chave de API OpenWeatherMap
WEATHER_API_KEY = '66f2805257505dd3dc9e4af9a7b29581'
# digite um "/start" para esse comenado
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bem-vindo ao seu bot de previsão do tempo! Use /tempo [cidade] para verificar o tempo.")

def get_weather(update: Update, context: CallbackContext):
    city = " ".join(context.args)
    if not city:
        update.message.reply_text("Por favor, forneça uma cidade. Exemplo: /tempo São Paulo")
        return

    # Consulta à API OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        update.message.reply_text(f"Em {city}: {weather_description}, temperatura: {temperature}°C")#informou uma cidade valida
    else:
        update.message.reply_text("Cidade não encontrada. Verifique a ortografia ou tente outra cidade.")#informou uma cidade invalida
#comandos
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("tempo", get_weather, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
