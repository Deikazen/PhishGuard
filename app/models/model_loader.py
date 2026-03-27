import onnxruntime as rt
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

XGB_MODEL_PATH = os.path.join(BASE_DIR, "model", "xgb.onnx")
TFIDF_MODEL_PATH = os.path.join(BASE_DIR, "model", "tfidf.onnx")
FEEDBACK_CSV_PATH = os.getenv("FEEDBACK_CSV_PATH")

model = rt.InferenceSession(XGB_MODEL_PATH)
tfidf = rt.InferenceSession(TFIDF_MODEL_PATH)

CSV_FILE = FEEDBACK_CSV_PATH