import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import TensorDataset, DataLoader

class BiLSTM_SentimentAnalysis(torch.nn.Module) :
    def __init__(self, vocab_size, embedding_dim=64, hidden_dim=32, dropout=0.5, batch_size=64) :
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim, padding_idx=0)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=2, batch_first=True, bidirectional=True)
        self.fc = nn.Sequential(
            nn.Linear(2*hidden_dim, 2*hidden_dim),
            nn.Dropout(dropout),
            nn.ReLU()
        )
        self.dropout = nn.Dropout(dropout)
        self.dense = nn.Sequential(
            nn.Linear(2*hidden_dim, 1),
            nn.Sigmoid()
        )
        self.batch_size = batch_size

    def forward(self, x, hidden):
        """
        The forward method takes in the input and the previous hidden state 
        """
        embs = self.embedding(x)
        out, hidden = self.lstm(embs, hidden)
        out = self.dropout(out)
        # out = self.fc(out)
        out = self.dense(out)
        out = out.squeeze()
        out = out[:, -1]
        return out, hidden
    
    def init_hidden(self):
        return (torch.zeros(4, self.batch_size, 32), torch.zeros(4, self.batch_size, 32))