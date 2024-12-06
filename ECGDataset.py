import torch
from torch.utils.data import Dataset
from torchvision import transforms
from torchvision.transforms import ToTensor
import numpy as np
import cv2

class ECGDataset(Dataset):
    def __init__(self, img_path_data, csv_data, transform=transforms.ToTensor()):
        self.img_data = []
        self.label_data = []
        self.len = 0
        print('init start')
        for path in img_path_data:
            self.len += 1
            #self.img_data.append(transform(cv2.imread(path))) # read in color
            self.img_data.append(transform(cv2.imread(path,0))) # read in grayscale
            self.label_data.append(torch.Tensor(csv_data.iloc[int(path.split('\\')[-1].split('.')[0].split('_')[1])].values))
            if self.len % 50 == 0 : print(f'init ongoing... {self.len} img done')
        print(f'init done with {self.len} img')

    def __len__(self):
        return self.len

    def __getitem__(self, idx):
        return self.img_data[idx], self.label_data[idx]