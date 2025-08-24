import pickle

cv = pickle.load(open("models/cv.pkl", "rb"))
clf = pickle.load(open("models/clf.pkl", "rb"))

def make_prediction(email):
    tokenized_email = cv.transform([email])
    predictions = clf.predict(tokenized_email)
    predictions = 1 if predictions == 1 else -1
    return predictions