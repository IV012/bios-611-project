import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_tweets.csv")
df = df.astype({"post_text":str})

count_vector = CountVectorizer(stop_words="english")
tfidf_transformer = TfidfTransformer()
sparse_matrix = count_vector.fit_transform(df.post_text)
sparse_matrix = tfidf_transformer.fit_transform(sparse_matrix)

x = sparse_matrix
y = df["label"].values

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify = y, random_state = 611)

BNB = BernoulliNB()
clf = BNB.fit(x_train, y_train)
print("The Accuracy of Bernoulli Naive Bayes is {:2.2%}".format(clf.score(x_test, y_test)))
cm = confusion_matrix(y_test, clf.predict(x_test), labels=clf.classes_)
disp = ConfusionMatrixDisplay(cm, display_labels=clf.classes_)
disp.plot()
plt.title('The Confusion Matrix of Bernoulli Naive Bayes Classifier')
plt.savefig("result/cm_bnb.png")
