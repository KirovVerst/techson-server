import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from techson_server.settings import BASE_DIR

path = BASE_DIR + '/db/csv/train.csv'

train_data = pd.read_csv(path)

y_train = train_data['label']
x_train = train_data.drop('label', axis=1)

RFC = RandomForestClassifier(n_estimators=200, n_jobs=-1)

RFC.fit(x_train, y_train)

path = BASE_DIR + '/classifiers/random_forest_classifier.pkl'

with open(path, 'wb') as f:
    pickle.dump(RFC, f)
