import numpy as np



num_data_pts = 4763
data_pts = np.arange(0,num_data_pts)

np.random.seed(2)

train_pts = np.random.choice(data_pts, int(0.75*num_data_pts), replace= False)
train_pts = set(train_pts)
data_pts = set(data_pts)

val_pts = data_pts - train_pts

file_train = open("train.txt", "w+")
file_val = open("val.txt", "w+")

for i in train_pts:
	file_train.write(str(i)+"\n")

for k in val_pts:
	file_val.write(str(k)+"\n")



