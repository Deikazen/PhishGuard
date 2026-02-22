from scipy.sparse import csr_matrix, hstack
import pandas as pd
from app.models.model_loader import model, tfidf
from app.services.number_feature import get_features

def predict_url(url):
    vector = tfidf.transform([url])
    numeric_features = get_features(url)
    numeric_features_df = pd.DataFrame([numeric_features])
    final_features = hstack([numeric_features_df, vector])

    print(final_features)
    prediction = model.predict(final_features)[0]
    probability = model.predict_proba(final_features)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }

