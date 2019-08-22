import lightgbm as lgb
import pandas as pd

df = pd.read_csv('test/support/iris.csv')

X = df.drop(columns=['Species'])
y = df['Species']
# y = y.replace(2, 1)
X['Sepal.Width'] = X['Sepal.Width'].replace(2.8, float('nan'))
X.loc[X['Sepal.Width'] < 3, 'Sepal.Width'] = 0
X.loc[X['Sepal.Width'] > 1, 'Sepal.Width'] = 1
# X.loc[X['Sepal.Width'] > 1, 'Sepal.Width'] = float('nan')
# print(X)

X_train = X[:100]
y_train = y[:100]
X_test = X[100:]
y_test = y[100:]

model = lgb.LGBMClassifier()
# model.fit(X_train, y_train)
model.fit(X_train, y_train, categorical_feature=[1]) #, eval_set=[(X_test, y_test)], early_stopping_rounds=5, verbose=True)
print(model.predict(X_test))
# print(model.predict_proba(X_test))
print(model.feature_importances_)
