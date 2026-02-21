import joblib
import xgboost as xgb

model = xgb.XGBClassifier()

# model = joblib.load("model/xgb_v3.json")
model.load_model("model/xgb_v3.json")
tfidf = joblib.load("model/tfidf_vectorizer.pkl")

CSV_FILE = "model/feedback.csv"