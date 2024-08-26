import time
import sys
import threading
import telebot

# 假设这是你的 bot token
TOKEN = '6410852034:AAFVFKV7vex0sKsfbNuGHvKOCazpm1-r2LM'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "bot使用方法")
    
def bot_polling():
    bot.polling(none_stop=True)

def timeout_monitor(max_time):
    start_time = time.time()
    while True:
        time.sleep(1)  # 每秒检查一次
        if time.time() - start_time > max_time:
            print("Reached the maximum run time. Exiting...")
            bot.stop_polling()  # 停止 bot 轮询
            sys.exit(0)  # 退出程序

# 设置运行的最大时间（秒）
max_time = 180  # 3分钟

# 启动 bot 轮询线程
threading.Thread(target=bot_polling).start()

# 启动超时监控线程
threading.Thread(target=timeout_monitor, args=(max_time,)).start()
