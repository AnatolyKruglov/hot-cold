import numpy as np
import plotly.graph_objects as go
from sentence_transformers import SentenceTransformer
from sklearn.decomposition import PCA
import telebot

class Game():
    def set(self, word):
        self.attempts, self.rs = [], []
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.word = word
        self.embedding = np.array(self.model.encode(word))

    def draw_map(self):
        pca = PCA(n_components=2)
        X = np.stack(self.attempts)
        pca.fit(X)
        X, y = pca.transform(X), pca.transform(np.array([self.embedding]))
        fig = go.Figure()\
          .add_trace(go.Scatter(x = X[:,0], y = X[:,1], mode="lines+markers", marker= dict(size=10,symbol= "arrow-bar-up", angleref="previous"), name='Attempts'))\
          .add_trace(go.Scatter(x = y[:,0], y = y[:,1], mode="markers", name='Отгадка'))\
          .update_layout(width=800, height=500, title='Route').update_yaxes(scaleanchor = "x", scaleratio = 1)
        fig.write_image("fig1.jpg")
        return "fig1.jpg"

    def guess(self, attempt_word):
        attempt_embedding = np.array(self.model.encode(attempt_word))
        r = np.linalg.norm(self.embedding - attempt_embedding)
        self.attempts.append(attempt_embedding)
        self.rs.append(r)
        if r == 0:
            return '100°, congratulations!'
        if len(self.attempts) == 1:  # first attempt
            return '0°, good start!'
        temperature = round(100 * (1 - (self.rs[-1] / self.rs[-2])))
        if temperature > 40:
            return f'+{temperature}°, BOILING HOT!'
        elif temperature > 0:
            return f'+{temperature}°, warm)'
        elif temperature > -40:
            return f'-{-temperature}°, cold('
        else:
            return f'-{-temperature}°, FREEZING COLD!'

bot = telebot.TeleBot('6337441024:AAEZja1zmak4ONxffNQpmICU5gSHhuKAgcc')  # I obviously revoked that token) but here is where it is inserted
game = Game()

# @bot.message_handler(commands=['set'])
# def send_welcome(message):
#     game.set(message.text)
#     bot.reply_to(message, f"Вы загадали слово '{message.text}'")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Отгадайте слово по подсказкам типа 'тепло-холодно'")
    word = 'green'  # а надо чтение бд, где юзеры загадывают друг другу слова
    print(word)
    game.set(word)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    ans = game.guess(message.text)
    bot.reply_to(message, ans)
    if ans == '100°, Правильно, победа!':
        path = game.draw_map()
        with open(path, 'rb') as f:
            bot.send_photo(message.chat.id, f)

# @bot.message_handler(content_types=['join_game'])
# def get_text_messages(message):
#     bot.reply_to(message,
#         "Введите id игры..."
#     )

bot.infinity_polling()
