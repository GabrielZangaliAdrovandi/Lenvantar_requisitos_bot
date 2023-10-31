#Isso para fazer funcionar o venv
- Python funcionando no pc ou seja instalar python no pc;
- Crie uma pasta com o nome "Venv" para o anbiente venv;
- Abra o terminal dessa pasta:
- Coloque esse codigo `python3 -m venv venv && source ./venv/bin/activate && which python`;
- Criar arquivo de texto requirements.txt na pasta "Venv", escreva nesse arquivo de texto isso `telepot` e 'requests';(sem aspas)
- Atualizar pacotes e instalar dependências no venv com `pip install --upgrade pip && pip install -r requirements.txt` (ou poetry init e add)
- Registrar bot com @botfather e obter o token;
- Criar `helloworld.py` apenas com print();
- Criar um bot que retorne "Hello World" no Telegram após o usuário disser "Oi"

  
  #Site ajuda
  https://medium.com/@douglasgusson/desenvolvimento-de-um-bot-para-o-telegram-em-python-do-zero-ao-deploy-parte-1-95d5096b8ea
  
