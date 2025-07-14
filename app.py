import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the model
@st.cache_resource
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Main app
def main():
    st.title("🤖 ML Model Prediction App")
    st.write("Enter the features below to get a prediction from your logistic regression model")
    
    # Load model
    model = load_model()
    
    # Create input fields based on your model's features
    st.subheader("Input Features")
    
    # Since your model has n_features_in_ = 2, create 2 input fields
    # Adjust these labels based on your actual features
    feature1 = st.number_input("Feature 1", value=0.0)
    feature2 = st.number_input("Feature 2", value=0.0)
    
    # Create prediction button
    if st.button("Make Prediction"):
        # Prepare input data
        input_data = np.array([[feature1, feature2]])
        
        # Make prediction
        prediction = model.predict(input_data)
        prediction_proba = model.predict_proba(input_data)
        
        # Display results
        st.subheader("Prediction Results")
        st.write(f"**Predicted Class:** {prediction[0]}")
        st.write(f"**Prediction Probability:**")
        
        # Display probabilities for each class
        for i, prob in enumerate(prediction_proba[0]):
            st.write(f"Class {model.classes_[i]}: {prob:.4f}")
        
        # Add confidence indicator
        max_prob = max(prediction_proba[0])
        if max_prob > 0.8:
            st.success(f"High confidence prediction ({max_prob:.2%})")
        elif max_prob > 0.6:
            st.warning(f"Medium confidence prediction ({max_prob:.2%})")
        else:
            st.error(f"Low confidence prediction ({max_prob:.2%})")

if __name__ == "__main__":
    main()