import torch

import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

from model import BiLSTM_SentimentAnalysis
from train_prepare import prepare_dataset

_, test_dl, word2index = prepare_dataset()


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = BiLSTM_SentimentAnalysis(len(word2index)).to(device)

model.load_state_dict(torch.load('model/model_lstm.pt'))
model.eval()
optimizer = torch.optim.Adam(model.parameters(), lr = 3e-4)

preds = []
labels = []
for batch_idx, batch in enumerate(test_dl):
    h0, c0 =  model.init_hidden()

    h0 = h0.to(device)
    c0 = c0.to(device)

    input = batch[0].to(device)
    labels = labels + list(batch[1].to("cpu"))

    optimizer.zero_grad()
    with torch.no_grad():
        out, hidden = model(input, (h0, c0))
        pred = list(out.to("cpu"))
        pred = [i >= 0.5 for i in pred]
    preds = preds + pred

print("The BiLSTM Accuracy is {:2.2%}".format(accuracy_score(labels, preds)))

cm = confusion_matrix(labels, preds)
disp = ConfusionMatrixDisplay(cm)
disp.plot()

plt.title('The Confusion Matrix of BiLSTM')
plt.savefig("result/cm_lstm.png")
