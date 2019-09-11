import pandas as pd
import numpy as np
from collections import Counter
from SentimentNN import SentimentNN
import torch.optim as optim
import torch.nn as nn
import torch

from torch.utils.data import DataLoader, TensorDataset

from torch.utils.data import Dataset, DataLoader

dataset_path = 'Sentiment.csv'

if __name__ == '__main__':

    df = pd.read_csv(dataset_path, usecols=['sentiment', 'text'])

    # Labels
    sentiments = df['sentiment']
    labels = np.array([0 if sentiment == 'Negative' else 1 for sentiment in sentiments])

    # Sample
    texts = df['text'].str.lower()

    vocab = set(' '.join(texts).split())

    idx_to_word = {i+1: word for i, word in enumerate(vocab)}
    word_to_idx = {w: i for i, w in idx_to_word.items()}

    # Init params to NN
    vocab_size = len(vocab)
    input_size = max([len(text.split()) for text in texts])
    n_labels = len(set(labels))
    lr = 0.01
    max_epochs = 5
    batch_size = 50

    inputs = np.zeros((len(texts), 200), dtype=int)

    for i, text in enumerate(texts):
        for j, word in enumerate(text.split()):
            inputs[i][j] = word_to_idx[word]

    train_data = TensorDataset(torch.from_numpy(
        inputs), torch.from_numpy(labels))
    train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)

    # Neural Network
    model = SentimentNN(vocab_size, n_labels, 400, 256, 2)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.BCELoss()

    model.train()
    clip = 5
    step =0

    for epoch in range(max_epochs):
        h = model.init_hidden(batch_size)
        
        for data_train, labels in train_loader:
            print(labels[0])
            step += 1
            data_train, labels = data_train.to('cpu'), labels.to('cpu')
            
            # making requires_grad = False for the latest set of h
            h = tuple([each.data for each in h])   
            
            model.zero_grad()
            output, h = model(data_train)

            print(output.shape, labels.shape)

            loss = criterion(output.squeeze(), labels.float())
            loss.backward()
            nn.utils.clip_grad_norm(model.parameters(), clip)
            optimizer.step()