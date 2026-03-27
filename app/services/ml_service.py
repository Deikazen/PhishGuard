import numpy as np
from app.models.model_loader import model, tfidf
from app.services.number_feature import get_features

def predict_url(url):
    input_text = np.array([[url]], dtype=object)
    tfidf_out = tfidf.run(None, {'document': input_text})[0]
    
    numeric_features = get_features(url)
    numeric_np = np.array([numeric_features], dtype=np.float32)
    
    if hasattr(tfidf_out, "todense"):
        tfidf_out = tfidf_out.todense()
        
    final_features = np.hstack([numeric_np, tfidf_out]).astype(np.float32)
    
    print("Features shape:", final_features.shape)
    
    xgb_out = model.run(None, {'input': final_features})
    prediction = xgb_out[0][0]
    probabilities = xgb_out[1][0]
    
    if isinstance(probabilities, dict):
        prob_1 = probabilities.get(1, 0.0)
    else:
        prob_1 = probabilities[1]
        
    return {
        "prediction": int(prediction),
        "probability": float(prob_1)
    }
