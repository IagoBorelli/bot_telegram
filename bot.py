import telebot

token = '7041052334:AAGKmUdY6iqXuG_N5aexrpXdm0To675p3kk'
id = '6767934438'

bot = telebot.TeleBot(token)

def send_telegram_msg(hamburguer, endereco, complemento, forma_pagamento):
    msg_final = f'''
    Novo pedido recebido:
    Hambúrguer: {hamburguer}
    Endereço: {endereco}
    Complemento: {complemento}
    Forma de pagamento: {forma_pagamento}
    '''
    bot.send_message(id, msg_final, parse_mode="Markdown")

print("Qual o hambúrguer: ")
hamburguer = input()
print("Qual o endereço: ")
endereco = input()
print("Qual o complemento: ")
complemento = input()
print("Qual a forma de pagamento pagamento: ")
forma_pagamento = input()

send_telegram_msg(hamburguer, endereco, complemento, forma_pagamento)