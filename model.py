import pandas as pd
import numpy as np
from sklearn.neighbors import BallTree
from sklearn.base import BaseEstimator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
import joblib

good = pd.read_csv('good.tsv', encoding="windows-1251", sep='\t')

rep = good[good.context_0 == "как дела ?"].reply
if rep.shape[0] > 0:
    print(rep.sample(1).iloc[0])

vectorizer = TfidfVectorizer(encoding="windows-1251")
matrix_big = vectorizer.fit_transform((good.context_0).apply(lambda x: np.str_(x)))
print(matrix_big.shape)

svd = TruncatedSVD(n_components=300)
svd.fit(matrix_big)
matrix_small = svd.transform(matrix_big)
print(matrix_small.shape)
print(svd.explained_variance_ratio_.sum())


def softmax(x):
    proba = np.exp(-x)
    return proba / sum(proba)


class NighborSampler(BaseEstimator):
    def __init__(self, k=5, temperature=1.0):
        self.k = k
        self.temperature = temperature

    def fit(self, X, y):
        self.tree = BallTree(X)
        self.y = np.array(y)

    def predict(self, X, random_state=None):
        distances, indices = self.tree.query(X, return_distance=True, k=self.k)
        result = []
        for distance, index in zip(distances, indices):
            result.append(np.random.choice(index, p=softmax(distance * self.temperature)))
        return self.y[result]


ns = NighborSampler()
ns.fit(matrix_small, good.reply)
pipe = make_pipeline(vectorizer, svd, ns)

print(pipe.predict(['Отправил отчет с ошибкой на эл.почту, когда я получу ответ об исправлении ошибки ?']))
