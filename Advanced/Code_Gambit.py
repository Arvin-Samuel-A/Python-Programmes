def Still_We_Rise(opponent_moves):
    """
    Function to submit for the competition.
    Input: List of opponent's previous moves (0 for defect, 1 for cooperate)
    Output: Your move (0 for defect, 1 for cooperate)
    """
    import numpy as np
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, LSTM
    # Access persistent variables
    if not hasattr(Still_We_Rise, 'model'):
        # Initialize on first call
        
        
        # Create and compile model
        Still_We_Rise.model = Sequential([
            LSTM(32, input_shape=(5, 1), return_sequences=True),
            LSTM(16),
            Dense(8, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        Still_We_Rise.model.compile(optimizer='adam', loss='binary_crossentropy')
        
        # Initialize other persistent variables
        Still_We_Rise.history = []
        Still_We_Rise.state_size = 5
        Still_We_Rise.training_counter = 0
        
        # Initial training with random data
        X_train = np.random.choice([0, 1], size=(1000, 5, 1))
        y_train = np.random.choice([0, 1], size=(1000, 1))
        Still_We_Rise.model.fit(X_train, y_train, epochs=5, verbose=0)
    
    # Update history
    if len(opponent_moves) > 0:
        Still_We_Rise.history.append(opponent_moves[-1])
    
    # If not enough history, use cooperative move
    if len(opponent_moves) < 2:
        return 1
    
    # Prepare state for prediction
    state = opponent_moves[-5:] if len(opponent_moves) >= 5 else \
            [0] * (5 - len(opponent_moves)) + opponent_moves
    state = np.array(state).reshape(1, 5, 1)
    
    # Predict opponent's next move
    opponent_prediction = Still_We_Rise.model.predict(state, verbose=0)[0][0]
    
    # Periodic retraining
    Still_We_Rise.training_counter += 1
    if Still_We_Rise.training_counter % 50 == 0 and len(opponent_moves) >= 5:
        # Create training data from recent history
        X = []
        y = []
        for i in range(len(opponent_moves) - 5):
            X.append(opponent_moves[i:i+5])
            y.append(opponent_moves[i+5])
        if X:
            X = np.array(X).reshape(-1, 5, 1)
            y = np.array(y)
            Still_We_Rise.model.fit(X, y, epochs=1, verbose=0)
    
    # Strategic decision based on prediction
    if opponent_prediction > 0.6:  # If opponent likely to cooperate
        return 1  # Cooperate
    elif opponent_prediction < 0.4:  # If opponent likely to defect
        return 0  # Defect
    else:
        # In uncertain cases, use tit-for-tat strategy
        return opponent_moves[-1]

    return decision