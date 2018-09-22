
# coding: utf-8

# In[ ]:


import tensorflow


# In[ ]:


import keras


# In[ ]:


import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation,Dense
from keras.optimizers import SGD


# In[ ]:


X=np.array([[0,0],[0,1],[1,0],[1,1]])
Y=np.array([[0],[1],[1],[0]])


# In[ ]:


model= Sequential()


# In[ ]:


model.add(Dense(2,input_dim=2,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))


# In[ ]:


sgd= SGD(lr=0.1,decay=1e-6,momentum=0.9,nesterov=True)
model.compile(loss='mean_squared_error',optimizer=sgd)
to_be_predicted=np.array([[0,5],[0,1],[1,0],[1,1]])


# In[ ]:


history = model.fit(X,Y,nb_epoch=10000,batch_size=4)


# In[ ]:


print(model.predict(X))


# In[ ]:


from tensorflow.keras.datasets import fashion_mnist

from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


# In[ ]:


(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
print(X_train.shape)

X_train = X_train.reshape(60000, 784)


# In[19]:


num_classes = len(set(y_train))
y_train = to_categorical(y_train, num_classes)

assert y_train[0].shape[0] == num_classes


# In[20]:


model = Sequential()
model.add(Dense(num_classes, input_dim=784, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])


# In[21]:


model.summary()


# In[ ]:


model.fit(X_train, y_train, epochs=30, batch_size=10)


# In[ ]:


scores = model.evaluate(X_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

