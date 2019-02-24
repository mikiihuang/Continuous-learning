import numpy as np
import random
import torch
import torch.utils.data as Data
#
# data = [0,1,2,3]
# # after_shuffle = np.random.permutation(data)
# # print(after_shuffle)
# # np.random.shuffle(data)
# # print(data)
# index = [0,1,2,3]
# rand_index = np.random.choice(len(index),4,replace=False)
# # random_idx = random.sample(range(0,len(index)),len(index),replace = False)
# # print(random_idx)
# print(rand_index)
def batch_iter(x, y, batch_size = 2):
    data_len = len(x)
    num_batch = int((data_len - 1)/batch_size) + 1
    indices = np.random.permutation(np.arange(data_len))

    x_shuff = np.array(x)[indices]
    y_shuff = np.array(y)[indices]
    for i in range(num_batch):
        start_id = i * batch_size
        end_id = min((i+1) * batch_size, data_len)
        yield x_shuff[start_id:end_id], y_shuff[start_id:end_id]
x = [[1,2,3,4],[2,3,4,5],[32,2,2,2],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
y = [1,0,0,1,0,1]
# print(batch_iter(x,y))
# data = batch_iter(x,y)
# # for x,y in data:
# #     print(x)
# #     print(y)

x_tensor = torch.tensor(x)
y_tensor = torch.tensor(y)
def get_batch(batch,x,y):

    torch_dataset = Data.TensorDataset(x, y)
    loader = Data.DataLoader(dataset=torch_dataset,batch_size=batch,shuffle=True)
    return loader
data = get_batch(2,x_tensor,y_tensor)
for train_x,train_y in data:
    print(train_x)
    print(train_y)