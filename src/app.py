def predict_wine_quality(input_values):
    
    # - Variables Predictoras:
    
    feature_names = [
        'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
        'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'
    ]
    
    # - Creación Del DataFrame Simulador De Y_Test:
    
    new_sample = pd.DataFrame([input_values], columns=feature_names)
    
    # - Escalado:
    
    new_sample_scaled = scaler.transform(new_sample)
    
    # - Predicción:
    
    prediction = model.predict(new_sample_scaled)[0]

    # - Interpretación:
    
    if prediction <= 4:
        return f"Este vino probablemente sea de calidad baja (calidad {prediction})"
    elif prediction <= 6:
        return f"Este vino probablemente sea de calidad media (calidad {prediction})"
    else:
        return f"Este vino probablemente sea de calidad alta (calidad {prediction})"