import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split

EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

class FERDataset(Dataset):
    def __init__(self, dataframe, transform=None):
        self.data = dataframe.reset_index(drop=True)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        pixels = np.array(row['pixels'].split(), dtype='float32').reshape(48, 48)
        image = torch.tensor(pixels, dtype=torch.float32).unsqueeze(0) / 255.0
        label = int(row['emotion'])
        if self.transform:
            image = self.transform(image)
        return image, label


def load_data(csv_path='/content/data/train.csv', val_size=0.15, test_size=0.15, random_state=42):
    df = pd.read_csv(csv_path)

    
    train_val, test = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=df['emotion']
    )

  
    val_ratio = val_size / (1 - test_size)
    train, val = train_test_split(
        train_val, test_size=val_ratio, random_state=random_state, stratify=train_val['emotion']
    )

    return train, val, test
