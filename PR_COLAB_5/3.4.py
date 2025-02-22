import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
messages = load_csv('messages.csv')
# id, message_id, time, status
checks = load_csv('checks.csv')
# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

# Как за период с начала семестра менялась активность студентов по каждой из задач?
df_messages['date'] = df_messages['time'].dt.date
df_messages.groupby(['task', 'date']).count()['id'].unstack().plot()
plt.xlabel('Дата')
plt.ylabel('Количество сообщений')
plt.title('Активность студентов по задачам за период')
plt.legend()
plt.show()
