import hackchat
import random

admin_trip=["XXXXXX"]

# 定义每日一言列表
daily_quotes = [
    "世界上没有绝对的黑暗，只有被遗忘的光明。",
    "勇气不是不害怕，而是克服恐惧之后继续前进。",
    "成功的秘诀在于坚持不懈。",
    "生活就像骑自行车，想要保持平衡就得不断前行。",
    "梦想不是等待机会，而是创造机会。",
    "人生没有彩排，每一天都是现场直播。",
    "决定你成为什么样的人的不是能力，而是选择。",
    "最困难的时刻往往是距离成功最近的时刻。",
    "不要等待机会，而要创造机会。",
    "每一次的挑战都是成长的机会。"
]

# afk
def afk():
    if "afk"==msg:
        chat.send_message("已经将您的状态标记为afk")
    elif "stop"==msg:
        chat.send_message("您的状态为在线")

# 每日一言
def day():
    if "HiyoDay"==msg:
        quote = random.choice(daily_quotes)
        chat.send_message(daily_quotes)

# 协管可执行的操作
def manage_actions():
    if msg.startswith("ban"):
        # 检查管理员识别码是否正确
        if trip in admin_trip:
            # 提取用户名
            user_to_ban = msg.split(" ")[1]
            # 执行封禁操作
            chat.send_message(f"/ban {user_to_ban}")
            chat.send_message(f"已经封禁用户 {user_to_ban}")
        else:
            chat.send_message("权限不足")
    elif msg.startswith("mute"):
        # 检查管理员识别码是否正确
        if trip in admin_trip:
            # 提取用户名
            user_to_mute = msg.split(" ")[1]
            # 执行禁言操作
            chat.send_message(f"/mute {user_to_mute}")
            chat.send_message(f"已经禁言用户 {user_to_mute}")
        else:
            chat.send_message("权限不足")

# 在消息到达时执行相应的操作
@chat.on_message()
def handle_message(sender, message):
    global msg
    msg = message.lower()
    afk()
    day()
    manage_actions()

# 运行客户端
chat.run()
