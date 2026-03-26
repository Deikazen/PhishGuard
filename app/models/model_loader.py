import onnxruntime as rt
import os
from dotenv import load_dotenv

load_dotenv()

XGB_MODEL_PATH = "model/xgb.onnx"
TFIDF_MODEL_PATH = "model/tfidf.onnx"
FEEDBACK_CSV_PATH = os.getenv("FEEDBACK_CSV_PATH")

model = rt.InferenceSession(XGB_MODEL_PATH)
tfidf = rt.InferenceSession(TFIDF_MODEL_PATH)

CSV_FILE = FEEDBACK_CSV_PATH