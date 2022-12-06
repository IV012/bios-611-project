import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader

import nltk
from tqdm import tqdm
import pandas as pd
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from model import BiLSTM_SentimentAnalysis
from train_prepare import prepare_dataset

# process the data

train_dl, test_dl, word2index = prepare_dataset()

# train model

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = BiLSTM_SentimentAnalysis(len(word2index)).to(device)
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters(), lr = 3e-4)

epochs = 100
losses = []
model.train()

for e in tqdm(range(epochs)):

    h0, c0 =  model.init_hidden()

    h0 = h0.to(device)
    c0 = c0.to(device)

    for batch_idx, batch in enumerate(train_dl):

        input = batch[0].to(device)
        target = batch[1].to(device)

        optimizer.zero_grad()
        with torch.set_grad_enabled(True):
            out, hidden = model(input, (h0, c0))
            loss = criterion(out.type(torch.DoubleTensor), target.type(torch.DoubleTensor))
            loss.backward()
            optimizer.step()
        if batch_idx%10 == 0:
            print("\nepoch:", e+1 ,' num:', batch_idx, 'loss:', loss.item())
    losses.append(loss.item())

torch.save(model.state_dict(), "model/model_lstm.pt")

plt.plot(losses)
plt.savefig("figure/loss.png")