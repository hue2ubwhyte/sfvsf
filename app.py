import telebot
from datetime import datetime

# 替换 'YOUR_TOKEN_HERE' 为你的 Telegram Bot Token
TOKEN = '6825207495:AAEdlZhWKNFi5EOvTqAaRyg_55pGWYRk3Fw'
bot = telebot.TeleBot(TOKEN)

# 定义命令 '/uuu' 的处理器
@bot.message_handler(commands=['uuu'])
def send_current_time(message):
    # 获取当前时间
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now)
    # 发送时间到用户
    bot.send_message(message.chat.id, f"当前时间是: {now}")

# 轮询
bot.polling()
