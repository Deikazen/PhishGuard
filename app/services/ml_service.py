from scipy.sparse import csr_matrix, hstack
from app.models.model_loader import model, tfidf
from app.services.number_feature import get_features

def predict_url(url):
    vector = tfidf.transform([url])
    numeric_features = get_features(url)
    numeric_array = np.array([numeric_features]) # Pakai numpy saja
    final_features = hstack([numeric_array, vector])

    print(final_features)
    prediction = model.predict(final_features)[0]
    probability = model.predict_proba(final_features)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }

