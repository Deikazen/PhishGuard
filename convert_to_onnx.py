import joblib
import xgboost as xgb
import onnx
import onnxmltools
from skl2onnx import to_onnx
from skl2onnx.common.data_types import StringTensorType
from onnxmltools.convert.common.data_types import FloatTensorType
from scipy.sparse import hstack, csr_matrix
import warnings
warnings.filterwarnings('ignore')

print("Loading original models...")
tfidf = joblib.load('model/tfidf_vectorizer.pkl')
model = xgb.XGBClassifier()
model.load_model('model/xgb_v3.json')

print("Converting TF-IDF to ONNX...")
# Input TF-IDF adalah sebuah URL (string)
onnx_tfidf = to_onnx(tfidf, initial_types=[('document', StringTensorType([1, 1]))])
with open('model/tfidf.onnx', 'wb') as f:
    f.write(onnx_tfidf.SerializeToString())
print("TF-IDF converted and saved to model/tfidf.onnx")

print("Calculating XGBoost input features count...")
# Dummy data untuk mencari jumlah fitur
dummy_vector = tfidf.transform(["http://example.com"])
dummy_numeric = csr_matrix([[0.0] * 11])
dummy_final = hstack([dummy_numeric, dummy_vector])
n_features = dummy_final.shape[1]

print(f"XGBoost Input Features = {n_features}")
print("Converting XGBoost to ONNX...")
onnx_xgb = onnxmltools.convert_xgboost(model, initial_types=[('input', FloatTensorType([None, n_features]))])
with open('model/xgb.onnx', 'wb') as f:
    f.write(onnx_xgb.SerializeToString())
print("XGBoost converted and saved to model/xgb.onnx")
print("SUCCESS!")
