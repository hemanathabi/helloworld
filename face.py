from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D,MaxPooling2D
from keras.layers.core import Activation,Flatten,Dense,Dropout
from keras import backend as keras

class tinyVGG:
  @staticmethod
  def build(height,width,depth,classes):
    model = Sequential()
    input_shape = (height,width,depth)
    channel_dim = -1
    if(k.image_data_format()=='channels_first'):
      input_shape = (depth, height, width)
      channel_dim = 1
	  
print('doytne')
	