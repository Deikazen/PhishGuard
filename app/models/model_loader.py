import joblib
import xgboost as xgb
import os
from dotenv import load_dotenv

load_dotenv()

XGB_MODEL_PATH = os.getenv("XGB_MODEL_PATH")
TFIDF_MODEL_PATH = os.getenv("TFIDF_MODEL_PATH")
FEEDBACK_CSV_PATH = os.getenv("FEEDBACK_CSV_PATH")

model = xgb.XGBClassifier()


model.load_model(XGB_MODEL_PATH)
tfidf = joblib.load(TFIDF_MODEL_PATH)

CSV_FILE = FEEDBACK_CSV_PATH