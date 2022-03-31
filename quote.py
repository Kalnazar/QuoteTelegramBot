import telebot
from telebot import TeleBot, types

TOKEN = '1451005724:AAGDppvvt0vhMNelXrXiDZmZeSYDchZNd5M'
bot: TeleBot = telebot.TeleBot("1451005724:AAGDppvvt0vhMNelXrXiDZmZeSYDchZNd5M")


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Let's start📚")
    markup.add(item1)
    sti = open('images/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, "Welcome, <i>{0.first_name}</i>!\n"
                                      "I'm - <b>{1.first_name}</b>, quote bot."
                                      "\nI will help you by choosing a quote".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':

        if message.text == 'English🇺🇸':
            markup_reply_english = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_english = types.KeyboardButton(text='Life')
            button2_english = types.KeyboardButton(text='Love')
            button3_english = types.KeyboardButton(text='Humor')
            button4_english = types.KeyboardButton(text='Success')
            button5_english = types.KeyboardButton(text='Money')
            button6_english = types.KeyboardButton(text='Inspirational')
            markup_reply_english.add(
                button1_english, button2_english, button3_english, button4_english, button5_english, button6_english)
            bot.send_message(message.chat.id,
                             'Okay, please choose your genre of quote!', reply_markup=markup_reply_english)

        elif message.text == 'Russian🇷🇺':
            markup_reply_russian = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_russian = types.KeyboardButton(text='Жизненные')
            button2_russian = types.KeyboardButton(text='Любовь')
            button3_russian = types.KeyboardButton(text='Смешные')
            button4_russian = types.KeyboardButton(text='Мотивирующие')
            button5_russian = types.KeyboardButton(text='Деньги')
            button6_russian = types.KeyboardButton(text='Мужественность')
            markup_reply_russian.add(
                button1_russian, button2_russian, button3_russian, button4_russian, button5_russian, button6_russian)
            bot.send_message(message.chat.id,
                             'Окей, выберите свой жанр цитаты пожалуйста!', reply_markup=markup_reply_russian)

        if message.text == "Let's start📚":
            markup_wel = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1_wel = types.KeyboardButton(text="English🇺🇸")
            item2_wel = types.KeyboardButton(text="Russian🇷🇺")
            markup_wel.add(item1_wel, item2_wel)
            bot.send_message(message.chat.id, 'Choose one language', reply_markup=markup_wel)

        if message.text == 'More quotes on the topic of life':
            bot.send_message(message.chat.id, "“Everything you can imagine is real.”"
                                              "\n\n― Pablo Picasso")
            bot.send_message(message.chat.id, "“Life isn't about finding yourself. Life is about creating yourself.”"
                                              "\n\n― George Bernard Shaw")
            bot.send_message(message.chat.id, "“I'm not afraid of death; "
                                              "I just don't want to be there when it happens.”"
                                              "\n\n― Woody Allen")
            bot.send_message(message.chat.id, "“Sometimes the questions are complicated and the answers are simple.”"
                                              "\n\n― Dr. Seuss")
            bot.send_message(message.chat.id, "“Life is like riding a bicycle. "
                                              "To keep your balance, you must keep moving.”"
                                              "\n\n― Albert Einstein")

        if message.text == 'Life':
            photo = open('images/life.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "“You've gotta dance like there's nobody watching,"
                                              "\nLove like you'll never be hurt,"
                                              "\nSing like there's nobody listening,"
                                              "\nAnd live like it's heaven on earth.”"
                                              "\n\n― William W. Purkey")
            bot.send_message(message.chat.id, "“You only live once,"
                                              "but if you do it right,"
                                              "once is enough.”"
                                              "\n\n― Mae West")
            bot.send_message(message.chat.id, "“Good friends, good books, "
                                              "and a sleepy conscience: this is the ideal life.”"
                                              "\n\n― Mark Twain")
            bot.send_message(message.chat.id, "“Life is what happens to us while we are making other plans.”"
                                              "\n\n― Allen Saunders")
            bot.send_message(message.chat.id, "“This life is what you make it. No matter what, "
                                              "you're going to mess up sometimes, it's a universal truth. "
                                              "But the good part is you get to decide how you're going to mess it up. "
                                              "Girls will be your friends - they'll act like it anyway. "
                                              "But just remember, some come, some go. "
                                              "The ones that stay with you through everything "
                                              "- they're your true best friends. Don't let go of them. "
                                              "Also remember, sisters make the best friends in the world. "
                                              "As for lovers, well, they'll come and go too. "
                                              "And baby, I hate to say it, most of them - "
                                              "actually pretty much all of them are going to break your heart, "
                                              "but you can't give up because if you give up, "
                                              "you'll never find your soulmate. "
                                              "You'll never find that half who makes you whole "
                                              "and that goes for everything. "
                                              "Just because you fail once, "
                                              "doesn't mean "
                                              "you're gonna fail at everything. Keep trying, "
                                              "hold on, and always, always, always believe in yourself, "
                                              "because if you don't, then who will, sweetie? "
                                              "So keep your head high, keep your chin up, "
                                              "and most importantly, keep smiling, "
                                              "because life's a beautiful thing and there's so much to smile about.”"
                                              "\n\n― Marilyn Monroe")
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='More quotes on the topic of life')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'If you want more quotes on this topic click on the "More quotes on the topic of life"',
                             reply_markup=markup_reply_life)

        if message.text == "More quotes on the topic of love":
            bot.send_message(message.chat.id, "“Love is like the wind, you can't see it but you can feel it.”"
                                              "\n\n― Nicholas Sparks")
            bot.send_message(message.chat.id, "“You don't love someone because they're perfect, "
                                              "you love them in spite of the fact that they're not.”"
                                              "\n\n― Jodi Picoult")
            bot.send_message(message.chat.id, "“If you can make a woman laugh, you can make her do anything.”"
                                              "\n\n― Marilyn Monroe")
            bot.send_message(message.chat.id, "“I'm selfish, impatient and a little insecure. "
                                              "I make mistakes, I am out of control and at times hard to handle. "
                                              "But if you can't handle me at my worst, "
                                              "then you sure as hell don't deserve me at my best.”"
                                              "\n\n― Marilyn Monroe")
            bot.send_message(message.chat.id, "“Love never dies a natural death. "
                                              "It dies because we don't know how to replenish its source. "
                                              "It dies of blindness and errors and betrayals. "
                                              "It dies of illness and wounds; it dies of weariness, "
                                              "of witherings, of tarnishings.”"
                                              "\n\n― Anais Nin")

        if message.text == "Love":
            photo = open('images/love.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "“You know you're in love when you can't fall asleep because "
                                              "reality is finally better than your dreams.”"
                                              "\n\n― Dr. Seuss")
            bot.send_message(message.chat.id, "We accept the love we think we deserve.”"
                                              "\n\n― Stephen Chbosky")
            bot.send_message(message.chat.id, "“As he read, I fell in love the way you fall asleep: "
                                              "slowly, and then all at once.”"
                                              "\n\n― John Green")
            bot.send_message(message.chat.id, "“Love all, trust a few, do wrong to none.”"
                                              "\n\n― William Shakespeare")
            bot.send_message(message.chat.id, "“Love is that condition in which the happiness "
                                              "of another person is essential to your own.”"
                                              "\n\n― Robert A. Heinlein")
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='More quotes on the topic of love')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'If you want more quotes on this topic click on the "More quotes on the topic of love"',
                             reply_markup=markup_reply_life)

        if message.text == "More quotes on the topic of humor":
            bot.send_message(message.chat.id, "“Two things are infinite: the universe and human stupidity,"
                                              "and I'm not sure about the universe.”"
                                              "\n\n― Albert Einstein")
            bot.send_message(message.chat.id, "Everyone is out of place! I dropped my brains."
                                              "\n\n― Pirates of the Caribbean")
            bot.send_message(message.chat.id, "“It’s no use going back to yesterday, "
                                              "because I was a different person then.”"
                                              "\n\n― Lewis Carroll")
            bot.send_message(message.chat.id, "“Be nice to nerds. You may end up working for them. We all could.”"
                                              "\n\n― Charles J. Sykes")
            bot.send_message(message.chat.id, "Everyone is out of place! I dropped my brains."
                                              "\n\n― Pirates of the Caribbean")
            bot.send_message(message.chat.id, "“So many books, so little time.”"
                                              "\n\n― Frank Zappa")

        if message.text == "Humor":
            sti = open('images/humor.webp', 'rb')
            bot.send_sticker(message.chat.id, sti)
            bot.send_message(message.chat.id, "There are people who just want to approach and "
                                              "ask if it is difficult to live without brains."
                                              "\n\n― Faina Ranevskaya")
            bot.send_message(message.chat.id, "“I love mankind ... it's people I can't stand!!”"
                                              "\n\n― Charles M. Schulz")
            bot.send_message(message.chat.id, "— Shut up."
                                              "\n— I didn't say anything."
                                              "\n— You were thinking. It's annoying."
                                              "\n\n Sherlock― ")
            bot.send_message(message.chat.id, "“Have no fear of perfection - you'll never reach it.”"
                                              "\n\n― Salvador Dali")
            bot.send_message(message.chat.id, "Theory is when you know everything and nothing works, "
                                              "practice is when everything works and nobody knows why. "
                                              "Here we combine theory with practice: "
                                              "nothing works and nobody knows why."
                                              "― Albert Einstein")
            markup_reply_humor = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_humor = types.KeyboardButton(text='More quotes on the topic of humor')
            markup_reply_humor.add(button1_humor)
            bot.send_message(message.chat.id,
                             'If you want more quotes on this topic click on the "More quotes on the topic of humor"',
                             reply_markup=markup_reply_humor)

        if message.text == "More quotes on the topic of success":
            bot.send_message(message.chat.id, "“Success is getting what you want, happiness is wanting what you get”"
                                              "\n\n― W. P. Kinsella")
            bot.send_message(message.chat.id, "“Failure is the condiment that gives success its flavor.”"
                                              "\n\n― Truman Capote")
            bot.send_message(message.chat.id, "“Have no fear of perfection - you'll never reach it.”"
                                              "\n\n― Salvador Dali")
            bot.send_message(message.chat.id, "Success is stumbling from failure to "
                                              "failure with no loss of enthusiasm.”"
                                              "\n\n― Winston S. Churchill")
            bot.send_message(message.chat.id, "“Don't spend time beating on a wall, "
                                              "hoping to transform it into a door. ”"
                                              "\n\n― Coco Chanel")

        if message.text == "Success":
            photo = open('images/success.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "“Success is not final, failure is not fatal: "
                                              "it is the courage to continue that counts.”"
                                              "\n\n― Winston S. Churchill")
            bot.send_message(message.chat.id, "“I can't give you a sure-fire formula for success, "
                                              "but I can give you a formula for failure: "
                                              "try to please everybody all the time.”"
                                              "\n\n― Herbert Bayard Swope")
            bot.send_message(message.chat.id, "“If at first you don't succeed, try, try again. "
                                              "Then quit. No use being a damn fool about it.”"
                                              "\n\n― W.C. Fields")
            bot.send_message(message.chat.id, "“Try not to become a man of success. Rather become a man of value.”"
                                              "\n\n― Albert Einstein")
            bot.send_message(message.chat.id, "“It is better to fail in originality than to succeed in imitation.”"
                                              "\n\n― Herman Melville")
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='More quotes on the topic of success')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'If you want more quotes on this topic click on the "More quotes on the topic of success"',
                             reply_markup=markup_reply_life)

        if message.text == "More quotes on the topic of money":
            bot.send_message(message.chat.id, "“Too many people spend money they haven't earned, "
                                              "to buy things they don't want, "
                                              "to impress people that they don't like.”"
                                              "\n\n― Will Rogers")
            bot.send_message(message.chat.id, "“Libraries will get you through times of no money better"
                                              " than money will get you through times of no libraries.”"
                                              "\n\n― Anne Herbert")
            bot.send_message(message.chat.id, "“Making money isn't hard in itself... "
                                              "What's hard is to earn it doing something "
                                              "worth devoting one’s life to.”"
                                              "\n\n― Carlos Ruiz Zafón")
            bot.send_message(message.chat.id, "“The hardest thing in the world to understand is the income tax.”"
                                              "\n\n― Albert Einstein")
            bot.send_message(message.chat.id, "“Money may not buy happiness, "
                                              "but I'd rather cry in a Jaguar than on a bus.”"
                                              "\n\n― Françoise Sagan")

        if message.text == "Money":
            photo = open('images/money.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "“Anyone who lives within their means "
                                              "suffers from a lack of imagination.”"
                                              "\n\n― Oscar Wilde")
            bot.send_message(message.chat.id, "“Everyone wants to ride with you in the limo, "
                                              "but what you want is someone who will take "
                                              "the bus with you when the limo breaks down.”"
                                              "\n\n― Oprah Winfrey")
            bot.send_message(message.chat.id, "“A Penny Saved is a Penny Earned”"
                                              "\n\n― Benjamin Franklin")
            bot.send_message(message.chat.id, "“Wealth consists not in having great possessions, "
                                              "but in having few wants.”"
                                              "\n\n― Epictetus")
            bot.send_message(message.chat.id, "“While money can't buy happiness, "
                                              "it certainly lets you choose your own form of misery.”"
                                              "\n\n― Groucho Marx")
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='More quotes on the topic of money')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'If you want more quotes on this topic click on the "More quotes on the topic of money"',
                             reply_markup=markup_reply_life)

        if message.text == "More quotes on the topic of Inspirational":
            bot.send_message(message.chat.id, "“You never have to change anything "
                                              "you got up in the middle of the night to write.”"
                                              "\n\n― Saul Bellow")
            bot.send_message(message.chat.id, "“The unexamined life is not worth living.”"
                                              "\n\n― Socrates")
            bot.send_message(message.chat.id, "“Pain is temporary. Quitting lasts forever.”"
                                              "\n\n― Lance Armstrong Sally Jenkins")
            bot.send_message(message.chat.id, "“I was never really insane except "
                                              "upon occasions when my heart was touched.”"
                                              "\n\n― Edgar Allan Poe")
            bot.send_message(message.chat.id, "“Don't be pushed around by the fears in your mind. "
                                              "Be led by the dreams in your heart.”"
                                              "\n\n― Roy T. Bennett")

        if message.text == "Inspirational":
            photo = open('images/Inspirational.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "“Do one thing every day that scares you.”"
                                              "\n\n― Eleanor Roosevelt")
            bot.send_message(message.chat.id, "“We are what we pretend to be, "
                                              "so we must be careful about what we pretend to be.”"
                                              "\n\n― Kurt Vonnegut")
            bot.send_message(message.chat.id, "“Sometimes you wake up. Sometimes the fall kills you. "
                                              "And sometimes, when you fall, you fly.”"
                                              "\n\n― Neil Gaiman, Fables & Reflections")
            bot.send_message(message.chat.id, "“What's meant to be will always find a way”"
                                              "\n\n― Trisha Yearwood")
            bot.send_message(message.chat.id, "“The flower that blooms in adversity "
                                              "is the rarest and most beautiful of all.”"
                                              "\n\n― Walt Disney Company")
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='More quotes on the topic of Inspirational')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'If you want more quotes on this topic click on the "More quotes on the topic '
                             'of Inspirational"',
                             reply_markup=markup_reply_life)

        if message.text == 'Больше цитат':
            bot.send_message(message.chat.id, 'Не совершай классическую ошибку всех умников: не думай, '
                                              'что нет людей умнее тебя.'
                                              '\n\n- Области тьмы')
            bot.send_message(message.chat.id, '— Это не ответ.'
                                              '— Нет, это ответ. Просто это не то, что вы хотите услышать.'
                                              '\n\n- Неадекватные люди')
            bot.send_message(message.chat.id, 'Денег, которые я заработал, хватит мне до конца жизни, '
                                              'если я умру сегодня в 16.00.'
                                              '\n\n- Хенни Янгман')
            bot.send_message(message.chat.id, 'Иногда момент, который ты так долго ждал, '
                                              'приходит в самое неподходящее время...'
                                              '\n\n- Клиника')
            bot.send_message(message.chat.id, 'Ничто так не выдает человека, как то, над чем он смеётся.'
                                              '\n\n- Иоганн')

        if message.text == 'Жизненные':
            photo = open('images/life.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Проще расстаться с человеком, чем с иллюзиями на его счёт.'
                                              '\n\n- Марта Кетро')
            bot.send_message(message.chat.id, 'Такой вот парадокс: мы совершаем подвиги для тех, '
                                              'кому до нас уже нет никакого дела, а любят нас те, '
                                              'кому мы нужны и без всяких подвигов...'
                                              '\n\n- Смешарики')
            bot.send_message(message.chat.id, 'Самое худшее, когда нужно ждать и не можешь ничего сделать. '
                                              'От этого можно сойти с ума.'
                                              '\n\n- Эрих Мария Ремарк')
            bot.send_message(message.chat.id, 'Сильные люди не любят свидетелей своей слабости.'
                                              '\n\n- Маргарет Митчел')
            bot.send_message(message.chat.id, 'Как же неприятно потратить на человека так '
                                              'много времени лишь для того, чтобы узнать,'
                                              ' что он так и остался для тебя лишь посторонним.'
                                              '\n\n- Вечное сияние чистого разума')
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='Больше цитат')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'Если хотите больше цитат, то нажмите на '
                             '"Больше цитат"',
                             reply_markup=markup_reply_life)

        if message.text == 'Любовь':
            photo = open('images/love.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Если человек умер, его нельзя перестать любить, черт возьми. '
                                              'Особенно если он был лучше всех живых, понимаешь?'
                                              '\n\n- Джером Дэвид')
            bot.send_message(message.chat.id, 'У самого злого человека расцветает лицо, когда ему говорят, '
                                              'что его любят. Стало быть, в этом счастье...'
                                              '\n\n- Лев Николаевич Толстой')
            bot.send_message(message.chat.id, 'Кому-то не хватает одной женщины, '
                                              'и он переключается на пятую, десятую. '
                                              'А другому не хватает жизни, чтобы любить одну-единственную.'
                                              '\n\n- Константин Хабенский')
            bot.send_message(message.chat.id, 'Влюбиться можно в красоту, но полюбить – лишь только душу!'
                                              '\n\n- Уильям Шекспир')
            bot.send_message(message.chat.id, 'В идеальных отношениях чистая любовь и грязный секс дополняют, '
                                              'а не исключают друг друга.'
                                              '\n\n- Брайанна Рид')
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='Больше цитат')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'Если хотите больше цитат, то нажмите на '
                             '"Больше цитат"',
                             reply_markup=markup_reply_life)

        if message.text == 'Смешные':
            photo = open('images/humor.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Теория — это когда все известно, но ничего не работает.'
                                              ' Практика — это когда все работает, но никто не знает почему. '
                                              'Мы же объединяем теорию и практику: ничего не работает... '
                                              'и никто не знает почему!'
                                              '\n\n- Альберт Эйнштейн')
            bot.send_message(message.chat.id, 'Есть такие люди, к которым просто хочется подойти и'
                                              ' поинтересоваться, сложно ли без мозгов жить.'
                                              '\n\n- Фаина Раневская')
            bot.send_message(message.chat.id, 'Все это видели?! Ибо я отказываюсь это повторять!'
                                              '\n\n- Капитан Джек Воробей')
            bot.send_message(message.chat.id, 'Меня вообще-то сложно удивить... О! Синяя машина!'
                                              '\n\n- Симпсоны')
            bot.send_message(message.chat.id, '— О, Господи!..'
                                              '\n— Зови меня просто Дин.'
                                              '\n\n- Дин Винчестер')
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='Больше цитат')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'Если хотите больше цитат, то нажмите на '
                             '"Больше цитат"',
                             reply_markup=markup_reply_life)

        if message.text == 'Мотивирующие':
            photo = open('images/Inspirational.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Обязательно дружите с теми, кто лучше вас.'
                                              ' Будете мучиться, но расти.'
                                              '\n\n- Вера Полозкова')
            bot.send_message(message.chat.id, 'Столько есть всего, о чём надо подумать. '
                                              'Зачем забивать себе голову тем, чего уже не вернёшь, '
                                              '— надо думать о том, что ещё можно изменить.'
                                              '\n\n- Скарлетт')
            bot.send_message(message.chat.id, 'Если ты плачешь не от счастья, то перестань.'
                                              '\n\n- Футурама')
            bot.send_message(message.chat.id, 'Все, что делаешь, надо делать хорошо, даже если совершаешь'
                                              ' безумство.'
                                              '\n\n- Оноре Де Бальзак')
            bot.send_message(message.chat.id, 'Ты — это то, что ты делаешь. '
                                              'Ты — это твой выбор. Тот, в кого себя превратишь.'
                                              '\n\n- Джонни Деп')
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='Больше цитат')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'Если хотите больше цитат, то нажмите на '
                             '"Больше цитат"',
                             reply_markup=markup_reply_life)

        if message.text == 'Деньги':
            photo = open('images/money.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, '— И сколько же это будет стоить?'
                                              '\n— Это бесплатно!'
                                              '\n— Звучит дороговато.'
                                              '\n\n- Симпсоны')
            bot.send_message(message.chat.id, 'Для того, чтобы понять, что счастье не в деньгах, '
                                              'нужно сперва узнать и то, и другое – счастье и деньги.'
                                              '\n\n- Фредрик Бегбедер')
            bot.send_message(message.chat.id, 'Не лажу с бытом! Деньги мешают мне и когда их нет, и когда они есть.'
                                              '\n\n- Фаина Раневская')
            bot.send_message(message.chat.id, 'Деньги нужно срочно пропить, так как потом их просто не будет...'
                                              '\n\n- Наруто')
            bot.send_message(message.chat.id, 'Это только кажется, что за всё платят деньгами. '
                                              'За всё действительно важное платят кусочками души.'
                                              '\n\n- Дмитрий Емец')
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='Больше цитат')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'Если хотите больше цитат, то нажмите на '
                             '"Больше цитат"',
                             reply_markup=markup_reply_life)

        if message.text == 'Мужественность':
            photo = open('images/success.webp', 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, 'Всякий мужественный, всякий правдивый человек приносит честь '
                                              'своей родине.'
                                              '\n\n- Роман Роллан')
            bot.send_message(message.chat.id, 'Мужчины любят быть более мужественными, чем тот, '
                                              'с кем они находятся вместе. '
                                              'То же происходит с некоторыми женщинами.'
                                              '\n\n- Эрик Берн')
            bot.send_message(message.chat.id, 'Выбирая между гордостью и ответственностью, '
                                              'мужчина почти всегда выберет гордость —'
                                              ' если ответственность отнимает его мужественность.'
                                              '\n\n- Стивен Кинг')
            bot.send_message(message.chat.id, 'Быть несгибаемым, как пень, помогут жизненные бури.'
                                              '\n\n- Геннадий')
            bot.send_message(message.chat.id, 'Боль – это пустяк. Поражение – тоже пустяк. '
                                              'Очень скоро вы в этом убедитесь!'
                                              '\n\n- Эрин Хантер')
            markup_reply_life = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1_life = types.KeyboardButton(text='Больше цитат')
            markup_reply_life.add(button1_life)
            bot.send_message(message.chat.id,
                             'Если хотите больше цитат, то нажмите на '
                             '"Больше цитат"',
                             reply_markup=markup_reply_life)


bot.polling(none_stop=True, interval=0)
