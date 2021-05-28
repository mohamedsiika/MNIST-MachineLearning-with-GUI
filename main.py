import cv2
from skimage.feature import hog
from sklearn.svm import SVC
from mlxtend.data import loadlocal_mnist




def apply_hog(x):
    list=[]
    for i in x:
        img = i.reshape(28, 28)
        img = img.astype('float32')
        img /= 255
        features= hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(1, 1))
        list.append(features)
    return list

def accuracy(test,pred):
    sum=0
    for i in range(len(test)):
        if test[i]==pred[i]:
            sum+=1
    return sum/len(test)

x_train,y_train=loadlocal_mnist(
    images_path='train-images.idx3-ubyte',
    labels_path='train-labels.idx1-ubyte'
)

x_test,y_test=loadlocal_mnist(
    images_path='t10k-images.idx3-ubyte',
    labels_path='t10k-labels.idx1-ubyte'
)







x_train=apply_hog(x_train)




svm=SVC()
svm.fit(x_train,y_train)

def predict_image(path):
    img = cv2.imread('out.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)
    img = img.astype('float32')
    img = 255 - img
    img /= 255
    img_hog = hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(1, 1))
    img_hog=img_hog.reshape(1,-1)
    predsvm=svm.predict(img_hog)
    return predsvm

print(predict_image("out.png"))







