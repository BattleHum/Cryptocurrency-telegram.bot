# be sure to install - pyTelegramBotAPI
# cryptocurrency exchange rate: https://incryptoview.info/currencies/
# cryptocurrency ip: https://docs.google.com/spreadsheets/d/1wTTuxXt8n9q7C4NDXqQpI3wpKu1_5bGVmP9Xz0XGSyU/edit#gid=0
import telebot
from pycoingecko import CoinGeckoAPI
from telebot import types
from py_currency_converter import convert
cg = CoinGeckoAPI()
bot = telebot.TeleBot('token')
#---------------------------
# commands from starting bot
#---------------------------
@bot.message_handler(commands=['start'])
def main(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Cryptocurrency course'),
           types.KeyboardButton('Exchange rate'),
           types.KeyboardButton('Converter(USD)'),
           types.KeyboardButton('Converter(EUR)'))
    cr = bot.send_message(message.chat.id, 'We are on the main one', reply_markup=b1)
    bot.register_next_step_handler(cr, step)
#-------------------------------
# Function buttons main menu
def step(message):
    if message.text == 'Cryptocurrency course':
        step2(message)
    elif message.text == 'Exchange rate':
        fiat(message)
    elif message.text == 'Converter(USD)':
        convert1(message)
    elif message.text == 'Converter(EUR)':
        convertEUR(message)
#----------------------------------
# Converter from cryptocurrency(USD)
def convert1(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Bitcoin'),types.KeyboardButton('Bitcoin Cash'), types.KeyboardButton('Wrapped bitcoin'),  types.KeyboardButton('Ethereum'),
           types.KeyboardButton('Ethereum Classic'), types.KeyboardButton('Litecoin'), types.KeyboardButton('Uniswap'), types.KeyboardButton('Solana'), types.KeyboardButton('BNB'),
           types.KeyboardButton('Binance USD'), types.KeyboardButton('USD Coin'), types.KeyboardButton('DogeCoin'), types.KeyboardButton('Back'))
    msg = bot.send_message(message.chat.id, 'Choose a cryptocurrency', reply_markup=b1)
    bot.register_next_step_handler(msg, convert2)


def convert2(message):
    if message.text == 'Bitcoin':
        msg = bot.send_message(message.chat.id, 'How many bitcoins do you want to convert?')
        bot.register_next_step_handler(msg, btc)
    elif message.text == 'Bitcoin Cash':
        msd = bot.send_message(message.chat.id, 'How many bitcoins cash do you want to convert?')
        bot.register_next_step_handler(msd, btcc)
    elif message.text == 'Wrapped bitcoin':
        msd = bot.send_message(message.chat.id, 'How many wrapped bitcoins do you want to convert?')
        bot.register_next_step_handler(msd, wbt)
    elif message.text == 'Ethereum':
        msd = bot.send_message(message.chat.id, 'How many ethereums do you want to convert?')
        bot.register_next_step_handler(msd, eth)
    elif message.text == 'Ethereum Classic':
        msd = bot.send_message(message.chat.id, 'How many classic etereums cash do you want to convert?')
        bot.register_next_step_handler(msd, ethc)
    elif message.text == 'Litecoin':
        msd = bot.send_message(message.chat.id, 'How many litecoins cash do you want to convert?')
        bot.register_next_step_handler(msd, lit)
    elif message.text == 'Uniswap':
        msd = bot.send_message(message.chat.id, 'How many uniswaps cash do you want to convert?')
        bot.register_next_step_handler(msd, unis)
    elif message.text == 'Solana':
        msd = bot.send_message(message.chat.id, 'How many solans cash do you want to convert?')
        bot.register_next_step_handler(msd, solan)
    elif message.text == 'BNB':
        msd = bot.send_message(message.chat.id, 'How many bnbs cash do you want to convert?')
        bot.register_next_step_handler(msd, bnb)
    elif message.text == 'Binance USD':
        msd = bot.send_message(message.chat.id, 'How many binanse usds cash do you want to convert?')
        bot.register_next_step_handler(msd, bnu)
    elif message.text == 'USD Coin':
        msd = bot.send_message(message.chat.id, 'How many usd coins cash do you want to convert?')
        bot.register_next_step_handler(msd, usc)
    elif message.text == 'DogeCoin':
        msd = bot.send_message(message.chat.id, 'How many dogecoins cash do you want to convert?')
        bot.register_next_step_handler(msd, dogc)
    elif message.text == 'Back':
        main(message)

def btc(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='bitcoin',vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} BTC == {price["bitcoin"]["usd"] * convert2} $')
    convert1(message)

def btcc(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='bitcoin-cash', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} BTC Cash == {price["bitcoin"]["usd"] * convert2} $')
    convert1(message)
def wbt(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='wrapped-bitcoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} WR BTC == {price["wrapped bitcoins"]["usd"] * convert2} $')
    convert1(message)
def eth(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='ethereum', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} ETH == {price["ethereum"]["usd"] * convert2} $')
    convert1(message)
def ethc(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='ethereum-classic', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} ETH Classic == {price["ethereum-classic"]["usd"] * convert2} $')
    convert1(message)
def lit(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='litecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} LIT == {price["litecoin"]["usd"] * convert2} $')
    convert1(message)
def unis(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='uniswap', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} UNS == {price["uniswap"]["usd"] * convert2} $')
    convert1(message)
def solan(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='solana', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} SOL == {price["solana"]["usd"] * convert2} $')
    convert1(message)
def bnb(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='binancecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} BNB == {price["binancecoin"]["usd"] * convert2} $')
    convert1(message)
def bnu(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='binance-usd', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} Binance USD == {price["binance-usd"]["usd"] * convert2} $')
    convert1(message)
def usc(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='usd-coin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} USD Coin == {price["usd-coin"]["usd"] * convert2} $')
    convert1(message)
def dogc(message):
    convert2 = message.text
    convert2 = int(convert2)
    price = cg.get_price(ids='dogecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convert2} DogeCoin == {price["dogecoin"]["usd"] * convert2} $')
    convert1(message)
#-----------------------------
# Cryptocurrency converter(EUR)
def convertEUR(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Bitcoin'),types.KeyboardButton('Bitcoin Cash'), types.KeyboardButton('Wrapped bitcoin'),  types.KeyboardButton('Ethereum'),
           types.KeyboardButton('Ethereum Classic'), types.KeyboardButton('Litecoin'), types.KeyboardButton('Uniswap'), types.KeyboardButton('Solana'), types.KeyboardButton('BNB'),
           types.KeyboardButton('Binance USD'), types.KeyboardButton('USD Coin'), types.KeyboardButton('DogeCoin'), types.KeyboardButton('Back'))
    msg = bot.send_message(message.chat.id, 'Choose a cryptocurrency', reply_markup=b1)
    bot.register_next_step_handler(msg, convert3)
def convert3(message):
    if message.text == 'Bitcoin':
        msg = bot.send_message(message.chat.id, 'How many bitcoins do you want to convert?')
        bot.register_next_step_handler(msg, btk1)
    elif message.text == 'Bitcoin Cash':
        msd = bot.send_message(message.chat.id, 'How many bitcoins cash do you want to convert?')
        bot.register_next_step_handler(msd, btcc1)
    elif message.text == 'Wrapped bitcoin':
        msd = bot.send_message(message.chat.id, 'How many wrapped bitcoins do you want to convert?')
        bot.register_next_step_handler(msd, wbt1)
    elif message.text == 'Ethereum':
        msd = bot.send_message(message.chat.id, 'How many ethereums do you want to convert?')
        bot.register_next_step_handler(msd, eth1)
    elif message.text == 'Ethereum Classic':
        msd = bot.send_message(message.chat.id, 'How many classic etereums cash do you want to convert?')
        bot.register_next_step_handler(msd, ethc1)
    elif message.text == 'Litecoin':
        msd = bot.send_message(message.chat.id, 'How many litecoins cash do you want to convert?')
        bot.register_next_step_handler(msd, lit1)
    elif message.text == 'Uniswap':
        msd = bot.send_message(message.chat.id, 'How many uniswaps cash do you want to convert?')
        bot.register_next_step_handler(msd, unis1)
    elif message.text == 'Solana':
        msd = bot.send_message(message.chat.id, 'How many solans cash do you want to convert?')
        bot.register_next_step_handler(msd, solan1)
    elif message.text == 'BNB':
        msd = bot.send_message(message.chat.id, 'How many bnbs cash do you want to convert?')
        bot.register_next_step_handler(msd, bnb1)
    elif message.text == 'Binance USD':
        msd = bot.send_message(message.chat.id, 'How many binanse usds cash do you want to convert?')
        bot.register_next_step_handler(msd, bnu1)
    elif message.text == 'USD Coin':
        msd = bot.send_message(message.chat.id, 'How many usd coins cash do you want to convert?')
        bot.register_next_step_handler(msd, usc1)
    elif message.text == 'DogeCoin':
        msd = bot.send_message(message.chat.id, 'How many dogecoins cash do you want to convert?')
        bot.register_next_step_handler(msd, dogc1)
    elif message.text == 'Back':
        main(message)
def btk1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='bitcoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} BTC == {price["bitcoin"]["eur"] * convert3} €')
    convertEUR(message)
def btcc1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='bitcoin-cash', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} BTC Cash == {price["bitcoin-cash"]["eur"] * convert3} €')
    convertEUR(message)
def wbt1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='wrapped-bitcoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} WR BTC == {price["wrapped bitcoins"]["eur"] * convert3} €')
    convertEUR(message)
def eth1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='ethereum', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} ETH == {price["ethereum"]["eur"] * convert3} €')
    convertEUR(message)
def ethc1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='ethereum-classic', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} ETH Classic == {price["ethereum-classic"]["eur"] * convert3} €')
    convertEUR(message)
def lit1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='litecoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} LIT == {price["litecoin"]["eur"] * convert3} €')
    convertEUR(message)
def unis1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='uniswap', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} UNS == {price["uniswap"]["eur"] * convert3} €')
    convertEUR(message)
def solan1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='solana', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} SOL == {price["solana"]["eur"] * convert3} €')
    convertEUR(message)
def bnb1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='binancecoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} BNB == {price["binancecoin"]["eur"] * convert3} €')
    convertEUR(message)
def bnu1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='binance-usd', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} Binance USD == {price["binance-usd"]["eur"] * convert3} €')
    convertEUR(message)
def usc1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='usd-coin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} USD Coin == {price["usd-coin"]["eur"] * convert3} €')
    convertEUR(message)
def dogc1(message):
    convert3 = message.text
    convert3 = int(convert3)
    price = cg.get_price(ids='dogecoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convert3} DogeCoin == {price["dogecoin"]["eur"] * convert3} €')
    convertEUR(message)
#-----------------------------
# Exchange Rate

def fiat(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('USD'),types.KeyboardButton('EUR'), types.KeyboardButton('UAH'), types.KeyboardButton('Back'))
    q = bot.send_message(message.chat.id, 'Today course', reply_markup=b1)
    bot.register_next_step_handler(q, fiat_step2)

def fiat_step2(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Go to'))
    if message.text == 'USD':
        price = convert(amount=1, to=['EUR', 'UAH'])
        bot.send_message(message.chat.id, f'1 USD == {price["UAH"]}₴\n'
                                          f'1 USD == {price["EUR"]}€')
        go_main = bot.send_message(message.chat.id, 'Go back?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    elif message.text == 'EUR':
        price = convert(amount=1, to=['USD', 'UAH'])
        bot.send_message(message.chat.id, f'1 USD == {price["USD"]}$\n'
                                          f'1 USD == {price["UAH"]}₴')
        go_main = bot.send_message(message.chat.id, 'Go back?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    elif message.text == 'UAH':
        price = convert(amount=1, to=['EUR', 'USD'])
        bot.send_message(message.chat.id, f'1 UAH == {price["USD"]}$\n'
                                          f'1 UAH == {price["EUR"]}€')
        go_main = bot.send_message(message.chat.id, 'Go back?', reply_markup=b1)
        bot.register_next_step_handler(go_main, fiat)
    elif message.text == 'Back':
        main(message)

#Cryptocurrency course
def step2(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('USD'), types.KeyboardButton('EUR'), types.KeyboardButton('Back'))
    q = bot.send_message(message.chat.id, 'Today course', reply_markup=b1)
    bot.register_next_step_handler(q, step3)


def step3(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Go to'))
    if message.text == 'USD':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, matic-network, uniswap, solana, binancecoin, binance-usd, usd-coin, dogecoin, ethereum-classic, wrapped-bitcoin, bitcoin-cash',vs_currencies='usd')
        bot.send_message(message.chat.id, f'Today course: \n\n'
                                          f'Bitcoin == {price["bitcoin"]["usd"]}$\n'
                                          f'Bitcoin Cash == {price["bitcoin-cash"]["usd"]}$\n'
                                          f'Wrapped Bitcoin == {price["wrapped-bitcoin"]["usd"]}$\n'
                                          f'Ethereum == {price["ethereum"]["usd"]}$\n'
                                          f'Ethereum Classsic == {price["ethereum-classic"]["usd"]}$\n'
                                          f'Litecoin == {price["litecoin"]["usd"]}$\n'
                                          f'Uniswap == {price["uniswap"]["usd"]}$\n'
                                          f'Solana == {price["solana"]["usd"]}$\n'
                                          f'BNB == {price["binancecoin"]["usd"]}$\n'
                                          f'Binance USD == {price["binance-usd"]["usd"]}$\n'
                                          f'USD Coin == {price["usd-coin"]["usd"]}$\n'
                                          f'Dogecoin == {price["dogecoin"]["usd"]}$', reply_markup=b1)
        go_main = bot.send_message(message.chat.id, 'Go back?', reply_markup=b1)
        bot.register_next_step_handler(go_main, step2)

    elif message.text == 'EUR':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, uniswap, solana, binancecoin, binance-usd, usd-coin, dogecoin, ethereum-classic, wrapped-bitcoin, bitcoin-cash', vs_currencies='eur')
        bot.send_message(message.chat.id, f'Today course: \n\n'
                                              f'Bitcoin == {price["bitcoin"]["eur"]}€\n'
                                              f'Bitcoin Cash == {price["bitcoin-cash"]["eur"]}€\n'
                                              f'Wrapped Bitcoin == {price["wrapped-bitcoin"]["eur"]}€\n'
                                              f'Ethereum == {price["ethereum"]["eur"]}$\n'
                                              f'Ethereum Classsic == {price["ethereum-classic"]["eur"]}€\n'
                                              f'Litecoin == {price["litecoin"]["eur"]}€\n'
                                              f'Uniswap == {price["uniswap"]["eur"]}€\n'
                                              f'Solana == {price["solana"]["eur"]}€\n'
                                              f'BNB == {price["binancecoin"]["eur"]}€\n'
                                              f'Binance USD == {price["binance-usd"]["eur"]}€\n'
                                              f'USD Coin == {price["usd-coin"]["eur"]}€\n'
                                              f'Dogecoin == {price["dogecoin"]["eur"]}€', reply_markup=b1)
        go_main = bot.send_message(message.chat.id, 'Back', reply_markup=b1)
        bot.register_next_step_handler(go_main, step2)
    elif message.text == 'Back':
        main(message)

bot.polling()

