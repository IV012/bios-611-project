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

def encode_and_pad(tweet, length, word2index):
    sos = [word2index["<SOS>"]]
    eos = [word2index["<EOS>"]]
    pad = [word2index["<PAD>"]]

    if len(tweet) < length - 2: # -2 for SOS and EOS
        n_pads = length - 2 - len(tweet)
        encoded = [word2index[w] for w in tweet]
        return sos + encoded + eos + pad * n_pads 
    else: # tweet is longer than possible; truncating
        encoded = [word2index[w] for w in tweet]
        truncated = encoded[:length - 2]
        return sos + truncated + eos

def prepare_dataset(path="data/processed_tweets.csv", batch_size=64, seq_length=40):
    nltk.download('punkt')
    df = pd.read_csv(path, encoding='utf-8').astype({"post_text":str})
    X = df.post_text
    y = df.label
    data = [(word_tokenize(post_text)) for post_text in X]
    X_train, X_test, y_train, y_test = train_test_split(data, y, stratify = y, random_state = 611)

    index2word = ["<PAD>", "<SOS>", "<EOS>"]

    for ds in [X_train, X_test]:
        for tweet in ds:
            for token in tweet:
                if token not in index2word:
                    index2word.append(token)
    word2index = {token: idx for idx, token in enumerate(index2word)}

    train_encoded = [encode_and_pad(tweet, seq_length, word2index) for tweet in X_train]
    test_encoded = [encode_and_pad(tweet, seq_length, word2index) for tweet in X_test]

    train_ds = TensorDataset(torch.as_tensor(train_encoded), torch.as_tensor(list(y_train)))
    test_ds = TensorDataset(torch.as_tensor(test_encoded), torch.as_tensor(list(y_test)))

    train_dl = DataLoader(train_ds, shuffle=True, batch_size=batch_size, drop_last=True)
    test_dl = DataLoader(test_ds, shuffle=True, batch_size=batch_size, drop_last=True)

    return train_dl, test_dl, word2index