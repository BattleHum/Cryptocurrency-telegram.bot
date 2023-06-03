# be sure to install - pyTelegramBotAPI
# cryptocurrency exchange rate: https://incryptoview.info/currencies/
# cryptocurrency ip: https://docs.google.com/spreadsheets/d/1wTTuxXt8n9q7C4NDXqQpI3wpKu1_5bGVmP9Xz0XGSyU/edit#gid=0
import telebot
from pycoingecko import CoinGeckoAPI
from telebot import types
from py_currency_converter import convert
cg = CoinGeckoAPI()
bot = telebot.TeleBot('token')
print("Im online!")
#---------------------------
# commands from starting bot
#--------------------------
@bot.message_handler(commands=['start'])
def main(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Cryptocurrency course'),
           types.KeyboardButton('Exchange rate'),
           types.KeyboardButton('Converter(USD)'),
           types.KeyboardButton('Converter(EUR)'),
           types.KeyboardButton('Converter(UAH)'))
    cr = bot.send_message(message.chat.id, 'We are on the main one', reply_markup=b1)
    bot.register_next_step_handler(cr, step)
#-------------------------------
# Function buttons main menu
def step(message):
    if message.text == 'Cryptocurrency course':
        CryptocurrencyCourse1(message)
    elif message.text == 'Exchange rate':
        fiat(message)
    elif message.text == 'Converter(USD)':
        convertUSD1(message)
    elif message.text == 'Converter(EUR)':
        convertEUR(message)
    elif message.text == 'Converter(UAH)':
        converterUAH(message)


#----------------------------------
# Converter from cryptocurrency(USD)
def convertUSD1(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Bitcoin'),types.KeyboardButton('Bitcoin Cash'), types.KeyboardButton('Wrapped bitcoin'),  types.KeyboardButton('Ethereum'),
           types.KeyboardButton('Ethereum Classic'), types.KeyboardButton('Litecoin'), types.KeyboardButton('Uniswap'), types.KeyboardButton('Solana'), types.KeyboardButton('BNB'),
           types.KeyboardButton('Binance USD'), types.KeyboardButton('USD Coin'), types.KeyboardButton('DogeCoin'), types.KeyboardButton('Back'))
    msg = bot.send_message(message.chat.id, 'Choose a cryptocurrency', reply_markup=b1)
    bot.register_next_step_handler(msg, convertUSD2)


def convertUSD2(message):
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
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='bitcoin',vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} BTC == {price["bitcoin"]["usd"] * convertUSD2} $')
    convertUSD1(message)

def btcc(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='bitcoin-cash', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} BTC Cash == {price["bitcoin-cash"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def wbt(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='wrapped-bitcoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} WR BTC == {price["wrapped-bitcoin"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def eth(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='ethereum', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} ETH == {price["ethereum"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def ethc(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='ethereum-classic', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} ETH Classic == {price["ethereum-classic"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def lit(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='litecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} LIT == {price["litecoin"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def unis(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='uniswap', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} UNS == {price["uniswap"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def solan(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='solana', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} SOL == {price["solana"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def bnb(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='binancecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} BNB == {price["binancecoin"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def bnu(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='binance-usd', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} Binance USD == {price["binance-usd"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def usc(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='usd-coin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} USD Coin == {price["usd-coin"]["usd"] * convertUSD2} $')
    convertUSD1(message)
def dogc(message):
    convertUSD2 = message.text
    convertUSD2 = int(convertUSD2)
    price = cg.get_price(ids='dogecoin', vs_currencies='usd')
    bot.send_message(message.chat.id, f'{convertUSD2} DogeCoin == {price["dogecoin"]["usd"] * convertUSD2} $')
    convertUSD1(message)
#-----------------------------
# Cryptocurrency converter(EUR)
def convertEUR(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Bitcoin'),types.KeyboardButton('Bitcoin Cash'), types.KeyboardButton('Wrapped bitcoin'),  types.KeyboardButton('Ethereum'),
           types.KeyboardButton('Ethereum Classic'), types.KeyboardButton('Litecoin'), types.KeyboardButton('Uniswap'), types.KeyboardButton('Solana'), types.KeyboardButton('BNB'),
           types.KeyboardButton('Binance USD'), types.KeyboardButton('USD Coin'), types.KeyboardButton('DogeCoin'), types.KeyboardButton('Back'))
    msg = bot.send_message(message.chat.id, 'Choose a cryptocurrency', reply_markup=b1)
    bot.register_next_step_handler(msg, convertEUR2)
def convertEUR2(message):
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
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='bitcoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} BTC == {price["bitcoin"]["eur"] * convertEUR2} €')
    convertEUR(message)
def btcc1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='bitcoin-cash', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} BTC Cash == {price["bitcoin-cash"]["eur"] * convertEUR2} €')
    convertEUR(message)
def wbt1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='wrapped-bitcoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} WR BTC == {price["wrapped-bitcoin"]["eur"] * convertEUR2} €')
    convertEUR(message)
def eth1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='ethereum', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} ETH == {price["ethereum"]["eur"] * convertEUR2} €')
    convertEUR(message)
def ethc1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='ethereum-classic', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} ETH Classic == {price["ethereum-classic"]["eur"] * convertEUR2} €')
    convertEUR(message)
def lit1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='litecoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} LIT == {price["litecoin"]["eur"] * convertEUR2} €')
    convertEUR(message)
def unis1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='uniswap', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} UNS == {price["uniswap"]["eur"] * convertEUR2} €')
    convertEUR(message)
def solan1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='solana', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} SOL == {price["solana"]["eur"] * convertEUR2} €')
    convertEUR(message)
def bnb1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='binancecoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} BNB == {price["binancecoin"]["eur"] * convertEUR2} €')
    convertEUR(message)
def bnu1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='binance-usd', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} Binance USD == {price["binance-usd"]["eur"] * convertEUR2} €')
    convertEUR(message)
def usc1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='usd-coin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} USD Coin == {price["usd-coin"]["eur"] * convertEUR2} €')
    convertEUR(message)
def dogc1(message):
    convertEUR2 = message.text
    convertEUR2 = int(convertEUR2)
    price = cg.get_price(ids='dogecoin', vs_currencies='eur')
    bot.send_message(message.chat.id, f'{convertEUR2} DogeCoin == {price["dogecoin"]["eur"] * convertEUR2} €')
    convertEUR(message)

#_____________________________
# Cryptocurrency convert(UAH)
def converterUAH(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('Bitcoin'), types.KeyboardButton('Bitcoin Cash'),
           types.KeyboardButton('Wrapped bitcoin'), types.KeyboardButton('Ethereum'),
           types.KeyboardButton('Ethereum Classic'), types.KeyboardButton('Litecoin'), types.KeyboardButton('Uniswap'),
           types.KeyboardButton('Solana'), types.KeyboardButton('BNB'),
           types.KeyboardButton('Binance USD'), types.KeyboardButton('USD Coin'), types.KeyboardButton('DogeCoin'),
           types.KeyboardButton('Back'))
    msg = bot.send_message(message.chat.id, 'Choose a cryptocurrency', reply_markup=b1)
    bot.register_next_step_handler(msg, convertUAH2)

def convertUAH2(message):
    if message.text == 'Bitcoin':
        msg = bot.send_message(message.chat.id, 'How many bitcoins do you want to convert?')
        bot.register_next_step_handler(msg, btk2)
    elif message.text == 'Bitcoin Cash':
        msd = bot.send_message(message.chat.id, 'How many bitcoins cash do you want to convert?')
        bot.register_next_step_handler(msd, btcc2)
    elif message.text == 'Wrapped bitcoin':
        msd = bot.send_message(message.chat.id, 'How many wrapped bitcoins do you want to convert?')
        bot.register_next_step_handler(msd, wbt2)
    elif message.text == 'Ethereum':
        msd = bot.send_message(message.chat.id, 'How many ethereums do you want to convert?')
        bot.register_next_step_handler(msd, eth2)
    elif message.text == 'Ethereum Classic':
        msd = bot.send_message(message.chat.id, 'How many classic etereums cash do you want to convert?')
        bot.register_next_step_handler(msd, ethc2)
    elif message.text == 'Litecoin':
        msd = bot.send_message(message.chat.id, 'How many litecoins cash do you want to convert?')
        bot.register_next_step_handler(msd, lit2)
    elif message.text == 'Uniswap':
        msd = bot.send_message(message.chat.id, 'How many uniswaps cash do you want to convert?')
        bot.register_next_step_handler(msd, unis2)
    elif message.text == 'Solana':
        msd = bot.send_message(message.chat.id, 'How many solans cash do you want to convert?')
        bot.register_next_step_handler(msd, solan2)
    elif message.text == 'BNB':
        msd = bot.send_message(message.chat.id, 'How many bnbs cash do you want to convert?')
        bot.register_next_step_handler(msd, bnb2)
    elif message.text == 'Binance USD':
        msd = bot.send_message(message.chat.id, 'How many binanse usds cash do you want to convert?')
        bot.register_next_step_handler(msd, bnu2)
    elif message.text == 'USD Coin':
        msd = bot.send_message(message.chat.id, 'How many usd coins cash do you want to convert?')
        bot.register_next_step_handler(msd, usc2)
    elif message.text == 'DogeCoin':
        msd = bot.send_message(message.chat.id, 'How many dogecoins cash do you want to convert?')
        bot.register_next_step_handler(msd, dogc2)
    elif message.text == 'Back':
        main(message)

def btk2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='bitcoin', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} BTC == {price["bitcoin"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def btcc2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='bitcoin-cash', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} BTC Cash == {price["bitcoin-cash"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def wbt2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='wrapped-bitcoin', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} Wrapped-bitcoins == {price["wrapped-bitcoin"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def eth2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='ethereum', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} ETH == {price["ethereum"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def ethc2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='ethereum-classic', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} ETH Classic == {price["ethereum-classic"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def lit2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='litecoin', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} LIT == {price["litecoin"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def unis2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='uniswap', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} UNS == {price["uniswap"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def solan2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='solana', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} SOL == {price["solana"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def bnb2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='binancecoin', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} BNB == {price["binancecoin"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def bnu2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='binance-usd', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} Binance USD == {price["binance-usd"]["uah"] * convertUAH2} ₴')
    converterUAH(message)


def usc2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='usd-coin', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} USD Coin == {price["usd-coin"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

def dogc2(message):
    convertUAH2 = message.text
    convertUAH2 = int(convertUAH2)
    price = cg.get_price(ids='dogecoin', vs_currencies='uah')
    bot.send_message(message.chat.id, f'{convertUAH2} DogeCoin == {price["dogecoin"]["uah"] * convertUAH2} ₴')
    converterUAH(message)

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
        bot.send_message(message.chat.id, f'1 EUR == {price["USD"]}$\n'
                                          f'1 EUR == {price["UAH"]}₴')
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
def CryptocurrencyCourse1(message):
    b1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1.add(types.KeyboardButton('USD'), types.KeyboardButton('EUR'), types.KeyboardButton('UAH'), types.KeyboardButton('Back'))
    q = bot.send_message(message.chat.id, 'Today course', reply_markup=b1)
    bot.register_next_step_handler(q, CryptocurrencyCourse2)


def CryptocurrencyCourse2(message):
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
        bot.register_next_step_handler(go_main, CryptocurrencyCourse2)

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
        go_main = bot.send_message(message.chat.id, 'Go back?', reply_markup=b1)
        bot.register_next_step_handler(go_main, CryptocurrencyCourse2)

    elif message.text == 'UAH':
        price = cg.get_price(ids='bitcoin, ethereum, litecoin, uniswap, solana, binancecoin, binance-usd, usd-coin, dogecoin, ethereum-classic, wrapped-bitcoin, bitcoin-cash',vs_currencies='uah')
        bot.send_message(message.chat.id, f'Today course: \n\n'
                                          f'Bitcoin == {price["bitcoin"]["uah"]}₴\n'
                                          f'Bitcoin Cash == {price["bitcoin-cash"]["uah"]}₴\n'
                                          f'Wrapped Bitcoin == {price["wrapped-bitcoin"]["uah"]}₴\n'
                                          f'Ethereum == {price["ethereum"]["uah"]}₴\n'
                                          f'Ethereum Classsic == {price["ethereum-classic"]["uah"]}₴\n'
                                          f'Litecoin == {price["litecoin"]["uah"]}₴\n'
                                          f'Uniswap == {price["uniswap"]["uah"]}₴\n'
                                          f'Solana == {price["solana"]["uah"]}₴\n'
                                          f'BNB == {price["binancecoin"]["uah"]}₴\n'
                                          f'Binance USD == {price["binance-usd"]["uah"]}₴\n'
                                          f'USD Coin == {price["usd-coin"]["uah"]}₴\n'
                                          f'Dogecoin == {price["dogecoin"]["uah"]}₴', reply_markup=b1)
        go_main = bot.send_message(message.chat.id, 'Go back?', reply_markup=b1)
        bot.register_next_step_handler(go_main, CryptocurrencyCourse2)

    elif message.text == 'Go to':
        main(message)




bot.polling(none_stop=True)
