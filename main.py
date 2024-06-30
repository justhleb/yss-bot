import telebot
from telebot import types
import sqlite3
import random

#7380357980:AAFzhfgLQN25MSS9nWbJNgCRLmf6BAto0p4
bot = telebot.TeleBot('7222778040:AAG7Z6bxbggATsZBx2qFz7cin1z-b0Yf748')


# {'content_type': 'text', 'id': 76, 'message_id': 76,

# 'from_user': {'id': 797860340, 'is_bot': False, 'first_name':
# 'Just', 'username': 'just_hlebuchek', 'last_name': 'Hleb', 'language_code': 'ru', 'can_join_groups': None,
# 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': True,
# 'added_to_attachment_menu': None, 'can_connect_to_business': None},
#
# 'date': 1718547311, 'chat': {'id': 797860340,
# 'type': 'private', 'title': None, 'username': 'just_hlebuchek', 'first_name': 'Just', 'last_name': 'Hleb',
# 'is_forum': None, 'max_reaction_count': None, 'photo': None, 'bio': None, 'join_to_send_messages': None,
# 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None,
# 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None,
# 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set':
# None, 'linked_chat_id': None, 'location': None, 'active_usernames': None, 'emoji_status_custom_emoji_id': None,
# 'has_hidden_members': None, 'has_aggressive_anti_spam_enabled': None, 'emoji_status_expiration_date': None,
# 'available_reactions': None, 'accent_color_id': None, 'background_custom_emoji_id': None,
# 'profile_accent_color_id': None, 'profile_background_custom_emoji_id': None, 'has_visible_history': None,
# 'unrestrict_boost_count': None, 'custom_emoji_sticker_set_name': None, 'business_intro': None, 'business_location':
# None, 'business_opening_hours': None, 'personal_chat': None, 'birthdate': None}, 'sender_chat': None,
# 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None,
# 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': '/start', 'entities': [
# <telebot.types.MessageEntity object at 0x000001418A3AC950>], 'caption_entities': None, 'audio': None, 'document':
# None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None,
# 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_members': None,
# 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None,
# 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id':
# None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None,
# 'connected_website': None, 'reply_markup': None, 'message_thread_id': None, 'is_topic_message': None,
# 'chat_background_set': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None,
# 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None,
# 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'users_shared': None, 'chat_shared': None,
# 'story': None, 'external_reply': None, 'quote': None, 'link_preview_options': None, 'giveaway_created': None,
# 'giveaway': None, 'giveaway_winners': None, 'giveaway_completed': None, 'forward_origin': None, 'boost_added':
# None, 'sender_boost_count': None, 'reply_to_story': None, 'sender_business_bot': None, 'business_connection_id':
# None, 'is_from_offline': None, 'effect_id': None, 'show_caption_above_media': None, 'json': {'message_id': 76,
# 'from': {'id': 797860340, 'is_bot': False, 'first_name': 'Just', 'last_name': 'Hleb', 'username': 'just_hlebuchek',
# 'language_code': 'ru', 'is_premium': True}, 'chat': {'id': 797860340, 'first_name': 'Just', 'last_name': 'Hleb',
# 'username': 'just_hlebuchek', 'type': 'private'}, 'date': 1718547311, 'text': '/start', 'entities': [{'offset': 0,
# 'length': 6, 'type': 'bot_command'}]}}

@bot.message_handler(commands=['start'])
def main(message):
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS students ('
                'id int auto_increment primary key'
                ',name varchar(100)'
                ',school varchar(100)'
                ',moc_partner varchar(100)'
                ',coffee_partner varchar(100)'
                ',is_moc_subscribe bool'
                ',is_coffee_subscribe bool)')

    cur.execute("SELECT * FROM students WHERE id = '%s'" %
                (message.chat.id,))
    if len(cur.fetchall()) != 0:
        pass
    else:
        bot.send_message(message.chat.id, 'Круто, добро пожаловать')
        cur.execute("INSERT INTO students (id, name, school, moc_partner, coffee_partner, is_moc_subscribe, "
                    "is_coffee_subscribe) VALUES ("
                    "'%s', '%s','%s','%s','%s','%s','%s')" % (
                        message.chat.id, message.from_user.username, 'base', 'no', 'no', False, False))
        mrk = types.ReplyKeyboardMarkup()
        mrk.add(types.KeyboardButton('ШМР iOS'))
        mrk.add(types.KeyboardButton('ШМР Flutter'))
        mrk.add(types.KeyboardButton('ШМР Android'))
        mrk.add(types.KeyboardButton('ШАР'))
        mrk.add(types.KeyboardButton('ШМЯ'))
        mrk.add(types.KeyboardButton('ШБР Python'))
        mrk.add(types.KeyboardButton('ШБР Java'))
        mrk.add(types.KeyboardButton('ШБР C++'))
        mrk.add(types.KeyboardButton('ШРИ'))
        bot.send_message(message.chat.id, "Привет! Подскажи из какой ты школы?", reply_markup=mrk)
        bot.register_next_step_handler(message, school_click)
    conn.commit()
    cur.close()


@bot.callback_query_handler(func=lambda callback: True)
def school_click(message):
    print(1)
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()
    if message.text in ["ШМР iOS", 'ШМР Flutter', 'ШМР Android', 'ШАР', 'ШМЯ', 'ШБР Python', 'ШБР Java', 'ШБР C++',
                        'ШРИ']:
        cur.execute("UPDATE students SET school='%s' WHERE id='%s'" % (message.text, message.chat.id))
    else:
        bot.send_message(message.chat.id, "Неверное название школы")
        bot.register_next_step_handler(message, school_click)
    bot.send_message(message.chat.id, 'Отлично!', reply_markup=types.ReplyKeyboardRemove())
    markup = types.ReplyKeyboardMarkup()
    moc_sub = markup.add(types.KeyboardButton("Подписаться на мок интервью"))
    moc_unsub = markup.add(types.KeyboardButton("Отписаться от мок интервью"))
    coffee_sub = markup.add(types.KeyboardButton("Подписаться на random coffee"))
    coffee_unsub = markup.add(types.KeyboardButton("Отписаться от random coffee"))
    bot.send_message(message.chat.id, 'Теперь ты можешь подписаться на мок интервью или отписаться от них',
                     reply_markup=markup)
    conn.commit()
    cur.close()


@bot.callback_query_handler(func=lambda callback: True)
def school_change(message):
    bot.send_message(message.chat.id, 'Окей, давай сменим школу', reply_markup=types.ReplyKeyboardRemove())
    mrk = types.ReplyKeyboardMarkup()
    mrk.add(types.KeyboardButton('ШМР iOS'))
    mrk.add(types.KeyboardButton('ШМР Flutter'))
    mrk.add(types.KeyboardButton('ШМР Android'))
    mrk.add(types.KeyboardButton('ШАР'))
    mrk.add(types.KeyboardButton('ШМЯ'))
    mrk.add(types.KeyboardButton('ШБР Python'))
    mrk.add(types.KeyboardButton('ШБР Java'))
    mrk.add(types.KeyboardButton('ШБР C++'))
    mrk.add(types.KeyboardButton('ШРИ'))
    bot.send_message(message.chat.id, "Привет! Подскажи из какой ты школы?", reply_markup=mrk)


@bot.message_handler(commands=['admin'])
def admin(message):
    if message.chat.id == 797860340:
        markup = types.ReplyKeyboardMarkup()
        markup.add(types.KeyboardButton("/moc_broadcast"))
        markup.add(types.KeyboardButton("/moc_clean"))
        markup.add(types.KeyboardButton("/coffee_broadcast"))
        markup.add(types.KeyboardButton("/coffee_clean"))
        bot.send_message(message.chat.id, 'admin mode activated', reply_markup=markup)


@bot.message_handler(commands=['moc_broadcast'])
def broadcast(message):
    if message.chat.id == 797860340:
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM students WHERE is_moc_subscribe = '%s'" % (True,))
        users = cur.fetchall()

        for user in users:
            # print()
            # print()
            # print(list(user))
            cur.execute(f"SELECT * FROM students WHERE id = '%s'" % (user[0],))
            test_partner = cur.fetchone()
            if test_partner[3] != 'no':
                continue
            # print(test_partner)
            cur.execute(f"SELECT * FROM students WHERE school='%s' AND id NOT IN ('%s') AND moc_partner='%s'"
                        % (user[2], user[0], 'no'))
            partners = cur.fetchall()
            # print(partners)
            if partners:
                user_partner = list(random.choice(partners))
                # print(user_partner)
                cur.execute("UPDATE students SET moc_partner='%s' WHERE id='%s'" % (user_partner[1], user[0]))
                # print(user_partner[0])
                cur.execute("UPDATE students SET moc_partner='%s' WHERE id='%s'" % (user[1], user_partner[0]))
                # cur.execute(f"SELECT * FROM students WHERE school='%s'"
                #             % (user[2],))
                # print(cur.fetchall())
                conn.commit()

        cur.execute(f"SELECT * FROM students WHERE is_moc_subscribe = '%s'" % (True,))
        users = cur.fetchall()
        for user in users:
            try:
                if user[3] != 'no':
                    #print(f"Привет, сегодня твоим партнёром на мок интервью будет @{user[3]}")
                    bot.send_message(user[0], f"Привет {users[1]}, сегодня "
                                              f"твоим партнёром на мок интервью будет {user[3]}")
                else:
                    #print('Привет, к сожалению я не смог найти тебе пару, извини :(')
                    bot.send_message(user[0], "Привет, к сожалению я не смог найти тебе пару, извини :(")
            except:
                pass
        conn.commit()
        cur.close()
    else:
        pass


@bot.message_handler(commands=['coffee_broadcast'])
def broadcast(message):
    if message.chat.id == 797860340:
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM students WHERE is_coffee_subscribe = '%s'" % (True,))
        users = cur.fetchall()

        for user in users:
            cur.execute(f"SELECT * FROM students WHERE id = '%s'" % (user[0],))
            test_partner = cur.fetchone()
            if test_partner[4] != 'no':
                continue
            cur.execute(f"SELECT * FROM students WHERE id NOT IN ('%s') AND coffee_partner='%s'"
                        % (user[0], 'no'))
            partners = cur.fetchall()
            # print(partners)
            if partners:
                user_partner = list(random.choice(partners))
                cur.execute("UPDATE students SET coffee_partner='%s' WHERE id='%s'" % (user_partner[1], user[0]))
                cur.execute("UPDATE students SET coffee_partner='%s' WHERE id='%s'" % (user[1], user_partner[0]))
                conn.commit()

        cur.execute(f"SELECT * FROM students WHERE is_coffee_subscribe = '%s'" % (True,))
        users = cur.fetchall()
        for user in users:
            try:
                if user[4] != 'no':
                    #print(f"Привет, сегодня твоим партнёром на random coffee будет @{user[4]}")
                    bot.send_message(user[0], f"Привет {users[1]}, сегодня твоим партнёром на random coffee будет @{user[4]}")
                else:
                    #print('Привет, к сожалению я не смог найти тебе пару, извини :(')
                    bot.send_message(user[0], "Привет, к сожалению я не смог найти тебе пару, извини :(")
                # bot.send_message(users[z][0], f"Привет {users[z][1]}, сегодня "
                #                               f"твоим партнёром на мок интервью будет {users[z][2]}")
            except:
                pass
        conn.commit()
        cur.close()
    else:
        pass


@bot.message_handler(commands=['moc_clean'])
def moc_clean(message):
    if message.chat.id == 797860340:
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute("UPDATE students SET moc_partner='%s'" % ('no',))
        conn.commit()
        cur.close()


@bot.message_handler(commands=['coffee_clean'])
def coffee_clean(message):
    if message.chat.id == 797860340:
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute("UPDATE students SET coffee_partner='%s'" % ('no',))
        conn.commit()
        cur.close()


@bot.message_handler()
def just_text(message):
    if message.text == "Подписаться на мок интервью":
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = '%s' AND is_moc_subscribe = '%s'" %
                    (message.chat.id, False))
        if len(cur.fetchall()) != 0:
            cur.execute("UPDATE students SET is_moc_subscribe='%s' WHERE id='%s'" % (True, message.chat.id))
            bot.send_message(message.chat.id, 'Ты подписался на мок интервью')
        else:
            cur.execute("SELECT EXISTS(SELECT * FROM students WHERE id = '%s' AND is_moc_subscribe = '%s')" %
                        (message.chat.id, True))
            if cur.fetchone():
                bot.send_message(message.chat.id, 'Ты переподписался')
                cur.execute("UPDATE students SET is_moc_subscribe='%s' WHERE id='%s'" % (True, message.chat.id))
        conn.commit()
        cur.close()

    elif message.text == "Отписаться от мок интервью":
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute("SELECT EXISTS(SELECT * FROM students WHERE id = '%s' AND is_moc_subscribe = '%s')" %
                    (message.chat.id, True))
        if len(cur.fetchall()) != 0:
            cur.execute("UPDATE students SET is_moc_subscribe='%s' WHERE id='%s'" % (False, message.chat.id))
            bot.send_message(message.chat.id, 'Ты отписался от мок интервью')
        else:
            print('Ты и так не подписан :(')

        conn.commit()
        cur.close()

    elif message.text == "Подписаться на random coffee":
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE id = '%s' AND is_coffee_subscribe = '%s'" %
                    (message.chat.id, False))
        if len(cur.fetchall()) != 0:
            cur.execute("UPDATE students SET is_coffee_subscribe='%s' WHERE id='%s'" % (True, message.chat.id))
            bot.send_message(message.chat.id, 'Ты подписался на random coffee')
        else:
            cur.execute("SELECT EXISTS(SELECT * FROM students WHERE id = '%s' AND is_coffee_subscribe = '%s')" %
                        (message.chat.id, True))
            if cur.fetchone():
                bot.send_message(message.chat.id, 'Ты переподписался')
                cur.execute("UPDATE students SET is_coffee_subscribe='%s' WHERE id='%s'" % (True, message.chat.id))
        conn.commit()
        cur.close()

    elif message.text == "Отписаться от random coffee":
        conn = sqlite3.connect('students.db')
        cur = conn.cursor()
        cur.execute("SELECT EXISTS(SELECT * FROM students WHERE id = '%s' AND is_coffee_subscribe = '%s')" %
                    (message.chat.id, True))
        if len(cur.fetchall()) != 0:
            cur.execute("UPDATE students SET is_coffee_subscribe='%s' WHERE id='%s'" % (False, message.chat.id))
            bot.send_message(message.chat.id, 'Ты отписался от random coffee')
        else:
            print('Ты и так не подписан :(')

        conn.commit()
        cur.close()

    else:
        file = open('./error_cat.jpg', 'rb')
        bot.send_photo(message.chat.id, file)
        bot.send_message(message.chat.id, f"Извини {message.from_user.first_name}, но я не понимаю, что тебе нужно")


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("подписаться на мок интервью"))
    bot.reply_to(message, 'Ну и вот зачем спрашивается? Вот что ты ожидал? Что я сломаюсь? А зачем тебе меня ломать, '
                          'иди делом займись лучше')


bot.infinity_polling(timeout=10000, long_polling_timeout=5)
