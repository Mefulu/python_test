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

# Как по дням недели распределяется активность студентов?
df_messages = pd.DataFrame(messages, columns=['id', 'task', 'variant', 'group', 'time'])
df_messages['time'] = df_messages['time'].apply(parse_time)
df_messages['day_of_week'] = df_messages['time'].dt.day_name()
df_messages.groupby('day_of_week').count()['id'].plot(kind='bar')
plt.xlabel('День недели')
plt.ylabel('Количество сообщений')
plt.title('Активность студентов по дням недели')
plt.show()
