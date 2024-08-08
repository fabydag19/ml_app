import spacy
import re
import numpy as np
from joblib import dump, load

def model_predictions(short_description, description, impact, urgency, priority):

    # Load italian language model
    nlp = spacy.load('it_core_news_sm')

    # Load the model and preprocessors
    model = load("/ml_app/models/svc_model.joblib")
    tfidf = load("/ml_app/models/tfidf_vectorizer.joblib")
    onehot = load ("/ml_app/models/onehot_encoder.joblib")
    label_encoder_f = load("/ml_app/models/label_encoder_f.joblib")
    label_encoder_t = load("/ml_app/models/label_encoder_t.joblib")


    def clean_free_text_columns(text):
        # Remove specified pattern
        text = re.sub(r"\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2} - .*? \(Work notes\)", "", text)
        # Transform text in lowercase
        text = text.lower()
        # Replace all non-alphabetic characters with spaces
        text = re.sub(r'[^a-z\s]', ' ', text)
        # Make sure there are single spaces by replacing multiple spaces with a single one
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    # Clean text with spacy: tokenization, lemmatization, stop word removal
    def spacy_clean_text(text):
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
        return " ".join(tokens)

    # Combine text data
    def combine_and_preprocess(short_description, description):
        combined_text = short_description + ' ' + description
        cleaned_text = clean_free_text_columns(combined_text)
        processed_text = spacy_clean_text(cleaned_text)
        return processed_text
    
    # Process data and make predictions
    def preprocess_and_predict(short_description, description, category, subcategory, process, subprocess, business_service, owner_group, customer_type, process_cause, resolution_entity, impact, urgency, priority):

        processed_text = combine_and_preprocess(short_description, description)
        
        X_text = tfidf.transform([processed_text])
        
        X_cat_1 = onehot.transform([[category, subcategory, process, subprocess, business_service, owner_group, customer_type, process_cause, resolution_entity]])
        X_cat_2 = label_encoder_f.transform([impact, urgency, priority]).reshape(1, -1)
        
        X = np.hstack((X_text.toarray(), X_cat_1.toarray(), X_cat_2))
        
        predictions = model.predict(X)
        predictions = label_encoder_t.inverse_transform(predictions)
        
        return predictions[0]

    # Input data
    short_description = short_description
    description = description
    category = ''
    subcategory = ''
    process = ''
    subprocess = ''
    business_service = ''
    owner_group = ''
    customer_type = ''
    process_cause = ''
    resolution_entity = ''
    impact = impact
    urgency = urgency
    priority = priority

    # Call function to predict
    predictions = preprocess_and_predict(short_description, description, category, subcategory, process, subprocess, business_service, owner_group, customer_type, process_cause, resolution_entity, impact, urgency, priority)
    
    return predictions