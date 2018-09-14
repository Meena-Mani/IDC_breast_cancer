from keras.callbacks import Callback
from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np

class LRFinder(Callback):
    
    '''
    The Learning Rate range test: a callback for finding the optimal learning rate range  
    This function will 
    
    # Usage
        ```
            lr_finder = LRFinder(min_lr=1e-5, 
                                 max_lr=1e-2, 
                                 steps_per_epoch=np.ceil(data_size/batch_size),  
                                 epochs=3
                                 beta=0.9)
            model.fit(X_train, Y_train, callbacks=[lr_finder])
            
            lr_finder.plot_loss()
        ```
    
    # Arguments
        min_lr: The lower bound of the learning rate  
        max_lr: The upper bound of the learning rate 
        steps_per_epoch: Number of iterations/mini-batches -- calculated as `np.ceil(data_size/batch_size)`. 
        epochs: Number of epochs to run experiment. Usually between 2 and 4 epochs is sufficient. 
        beta: the smoothing parameter. 0.99 ~ weighted over 100 previous values, 
                                       0.9 - 10 values.
        
    # Acknowledgements
        Author : Meena Mani (added a weighted average to plot loss)
        Stater code/blog: jeremyjordan.me/nn-learning-rate
        Original paper: https://arxiv.org/abs/1506.01186

    '''
    
    def __init__(self, min_lr=1e-5, max_lr=1e-2, steps_per_epoch=None, epochs=None, beta=0.9):
        super().__init__()
        
        self.min_lr = min_lr
        self.max_lr = max_lr
        self.total_iterations = steps_per_epoch * epochs
        self.iteration = 0
        self.history = {}
        self.beta = beta
        
    def clr(self):
        '''Calculate the learning rate.'''
        #use log fn to sample very small values
        x = np.log(1 + self.iteration / self.total_iterations) #use log fn to sample very small values
        return self.min_lr + (self.max_lr-self.min_lr) * x
        
    def on_train_begin(self, logs=None):
        '''Initialize the learning rate to the minimum value at the start of training.'''
        logs = logs or {}
        K.set_value(self.model.optimizer.lr, self.min_lr)
        
    def on_batch_end(self, epoch, logs=None):
        '''For every iteration, record batch statistics and update the learning rate.'''
        logs = logs or {}
        self.iteration += 1

        self.history.setdefault('lr', []).append(K.get_value(self.model.optimizer.lr))
        self.history.setdefault('iterations', []).append(self.iteration)

        for k, v in logs.items():
            self.history.setdefault(k, []).append(v)
            
        K.set_value(self.model.optimizer.lr, self.clr())
 

    def smooth_fn(self, y):
        '''Helper function to smooth input over a weighted average.'''
        n = len(self.history['iterations'])
        beta_c = 1 - self.beta
        ewa = np.zeros(n)
        ewa_corrected = np.zeros(n)
        ewa_corrected[0] = ewa[0] = y[0]
        for i in range (1,n):
            ewa[i] = self.beta*ewa[i-1] + beta_c*y[i] 
            ewa_corrected[i] = ewa[i] / (1 - self.beta**n)
        return ewa_corrected

    def plot_lr(self):
        '''Helper function to quickly inspect the learning rate schedule.'''
        plt.figure(figsize=(10,6))
        plt.plot(self.history['iterations'], self.history['lr'])
        plt.yscale('log')
        plt.xlabel('Iteration')
        plt.ylabel('LR')
        plt.title("Learning rate")
        
    def plot_loss(self):
        '''Plot the loss versus the learning rate'''
        plt.figure(figsize=(10,6))
        smoothed_loss = self.smooth_fn(self.history['loss'])
        plt.plot(self.history['lr'][1::10], smoothed_loss[1::10])
        plt.xscale('log')
        plt.xlabel('LR (log scale)')
        plt.ylabel('Loss')
        plt.title("Loss vs Learning Rate")
