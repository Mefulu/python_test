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

# Как по времени суток распределяется активность студентов?
df_messages['hour'] = df_messages['time'].dt.hour
df_messages.groupby('hour').count()['id'].plot(kind='bar')
plt.xlabel('Час суток')
plt.ylabel('Количество сообщений')
plt.title('Активность студентов по времени суток')
plt.show()
