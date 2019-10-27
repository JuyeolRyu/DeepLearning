import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import LSTM, Dropout,Dense,Activation
import datetime

data = pd.read_csv("./005930.KS.csv")
#data.head()

high_prices = data['High'].values
low_prices = data['Low'].values
mid_prices = (high_prices + low_prices) / 2

seq_len = 50 #윈도우의 크기 ==> 최근 50일을 보고 미래를 예측하겠다
sequence_length = seq_len + 1

result = []
for index in range(len(mid_prices) - sequence_length):
    result.append(mid_prices[index: index + sequence_length])

#print(result)

normalized_data = []
for window in result:
    normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
    normalized_data.append(normalized_window)

result = np.array(normalized_data)

row = int(round(result.shape[0] * 0.9))  # 차원이 몇개인지 확인(행의 개수) == 윈도우의 개수
train = result[:row, :]  # train 셋
np.random.shuffle(train)

x_train = train[:, :-1]  # 앞의 50개
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
y_train = train[:, -1]  # 뒤의 1개

x_test = result[row:, :-1]
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = result[row:, -1]

x_train.shape, x_test.shape
print(row)


model = Sequential()
model.add(LSTM(50,return_sequences=True, input_shape=(50,1)))
         #LSTM 첫번째 인자 : 메모리 셀의 수?
         #return_sequences = True ==>

model.add(LSTM(64,return_sequences=False))

model.add(Dense(1,activation='linear'))

model.compile(loss='mse',optimizer='rmsprop')

model.summary()

model.fit(x_train,y_train,
         validation_data=(x_test,y_test),
         batch_size=10, #한번에 몇개 학습?
         epochs=20) #학습 몇번시킴?
#loss 가 작을수록 좋음

pred = model.predict(x_test)

fig = plt.figure(facecolor='white')
ax=fig.add_subplot(111)

ax.plot(y_test,label='True')
ax.plot(pred,label='Prediction')
ax.legend()
plt.show()