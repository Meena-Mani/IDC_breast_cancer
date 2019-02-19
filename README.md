# IDC_breast_cancer
Classification of IDC in breast cancer histology images

### Data Description
IDC breast cancer data is available in different repositories. We use the [Invasive Ductal Carcinoma (IDC) breast cancer dataset](https://www.kaggle.com/paultimothymooney/breast-histopathology-images) on Kaggle which was first curated and presented by [5]<a href="#ref5">,[6]<a href="#ref6">. This dataset consists of 277,524 50x50 image patches extracted from 162 whole slide images. The IDC(-/+) ratio is 2:1.

We need to organize the data in accordance with the Keras data directory structure (i.e. data/train/class, data/val/class). The [make_directory.py](https://github.com/Meena-Mani/IDC_breast_cancer/blob/master/make_directory.py) script is used for this.

### Project 1
#### [Experiments with learning rates:  cyclical, 1cycle, fixed, range test](https://github.com/Meena-Mani/IDC_breast_cancer/blob/master/FT_LR_experiments.ipynb)
The learning rate is the most important tuning parameter in a deep learning system. In this exercise we look at the use of cyclical learning rates to train faster. This follows the work of Leslie Smith <a href="#ref1">[1]</a>, <a href="#ref2">[2]</a> and has been popularized by its inclusion in the FastAI deep learning course and library <a href="#ref3">[3]</a>. 

We will report on three learning rate experiments: (i) Cyclical Learning Rate, (ii) 1cycle, (iii) Fixed.  The *learning rate range test* is a method of calibrating a curve in order to find a good learning rate for the model. It is an important first step for the cycling schedules. We will use it to baseline all three experiments.  The [LR range test](https://github.com/Meena-Mani/IDC_breast_cancer/blob/master/lrate_callback.py) and [LR schedules](https://github.com/Meena-Mani/IDC_breast_cancer/blob/master/clr_callback.py) have been implemented in Keras via callbacks building on [starter code available on Github](https://github.com/bckenstler/CLR) <a href="#ref4">[4]</a>.

### References
<a name="ref1"></a>[1] [Leslie N. Smith. (2016). Cyclical Learning Rates for Training Neural Networks](https://arxiv.org/pdf/1506.01186.pdf)  
<a name="ref2"></a>[2] [Leslie N. Smith. (2018). A disciplined approach to neural network hyper-parameters: Part 1 -- learning rate, batch size, momentum, and weight decay.  CoRR abs/1803.09820 (2018)](https://arxiv.org/abs/1803.09820)  
<a name="ref3"></a>[3] [Jeremy Howard and others. (2018) fastai. On Github](https://github.com/fastai/fastai)     
<a name="ref4"></a>[4] [Brad Kentsler. (2018) CLR. On Github](https://github.com/bckenstler/CLR)   
<a name="ref4"></a>[5] [Janowczyk A, Madabhushi A. Deep learning for digital pathology image analysis: A comprehensive tutorial with selected use cases. J Pathol Inform. 2016.](https://www.ncbi.nlm.nih.gov/pubmed/27563488)   
<a name="ref4"></a>[6] [Cruz-Roa A. et. al. Proc. SPIE 9041, Medical Imaging 2014: Digital Pathology, 904103](http://spie.org/Publications/Proceedings/Paper/10.1117/12.2043872)
