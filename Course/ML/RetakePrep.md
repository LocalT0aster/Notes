# Intro to ML Retake 1
### Lecture 1
> Machine Learning - Computer programs that improve their performance at some task through experience

Bias Variance Tradeoff
$$
E(y_0-\hat{f}(x_0))^2=Var(\hat{f}(x_0))+[Bias(\hat{f}(x_0))]^2+Var(\epsilon)
$$
Where $(x_0, y_0)$ is a test observation
Typically, as the **flexibility or complexity** of $\hat{f}$ increases, its variance increases, and its bias decreases. So choosing the flexibility based on average test error amounts to a **bias-variance trade-off**.
![](Pasted%20image%2020260309234548.png)
![](Pasted%20image%2020260309234624.png)
### Lecture 2
Linear Regression, lol
$$
f(x_i)=w_0+w_1x_i
$$
Mean Square Error
$$
MSE=\frac{1}{n}\sum_{i=1}^n{(y_i - f(x_i))^2}
$$
Least Squares for linear
$$
w_0=\overline{y}-w_1\overline{x},\ w_1=\frac{\overline{xy}-\overline{x}\,\overline{y}}{\overline{x^2}-(\overline{x})^2}
$$
Polynomial Regression
$$
y=w_0+w_1x+w_2x^2+\cdots +w_dx^d
$$
Logistic Regression (z=polynomial)
$$
p(x)=\frac{1}{1+e^{-z}}
$$
![](Pasted%20image%2020260310003826.png)
Sensitivity = True Positive Rate = Recall
**Specificity = TN / (TN + FP)**
FPR = FP / (TN + FP)
$$
F1=2\times\frac{Prec\times Recall}{Prec+Recall}
$$
### Lecture 4
KNN Rule of thumb: $k<\sqrt{n}$.
![](Pasted%20image%2020260310010618.png)
![](Pasted%20image%2020260310010639.png)
![](Pasted%20image%2020260310010707.png)
Principal Component Analysis
![](Pasted%20image%2020260310020927.png)
![](Pasted%20image%2020260310021137.png)
Support Vector Machines
![](Pasted%20image%2020260310022227.png)
![](Pasted%20image%2020260310022250.png)
![](Pasted%20image%2020260310022329.png)
![](Pasted%20image%2020260310022402.png)
![](Pasted%20image%2020260310022503.png)
Deep Learning
1. **Feature learning** is better than using hand-crafted features
2. Feature learning should aim for learning hierarchical features
3. Higher level features should not be simple linear combinations of low-level features
We want these features to be:
- Informative, discriminative, and invariant to common variations, such as rotation, scaling, and noise
- Generalizable – able to capture and represent the underlying patterns and structure of the data in a way that can be effectively used to make predictions on new, unseen data.
- Hierarchical – hierarchical features are learned by progressively combining and abstracting lower-level features to form more complex and informative higher-level features
Regularization techniques for DNN
Dropout
![](Pasted%20image%2020260310025307.png)
- Only applied during the training.
- Dropout is a regularization technique used to reduce overfitting by randomly disabling a subset of neurons during training. It is particularly effective in large networks, long training sessions, or when training data is limited.
- Usually the dropping probability p is 0.5 or lower. Researchers recommend values between 0.2 and 0.5
- Dropout is most commonly applied after fully connected (dense) layers and is rarely used after convolutional layers. When used with convolutional layers, it typically involves a low dropout rate (i.e., low probability p of dropping units).

TODO
Regularization techniques for DNNs
- Dropout, Batch Normalization, Early Stopping, Data augmentation
Optimizers
- Adam, RMSProps, SGD with momentum
Pretrained Layers

![](Pasted%20image%2020260310034329.png)
![](Pasted%20image%2020260310034254.png)
![](Pasted%20image%2020260310034921.png)
$$
\text{Gini} = 1 - \sum_{i=1}^{C} p_i^2
$$
Where $p_i$ is the probability of class $i$.
