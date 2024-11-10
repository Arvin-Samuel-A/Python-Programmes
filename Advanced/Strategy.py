import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, LSTM, Input, concatenate
from tensorflow.keras.optimizers import Adam
from collections import deque
import random
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
import seaborn as sns

class AdvancedGameBot:
    def __init__(self, state_size=10, memory_size=2000):
        self.state_size = state_size
        self.action_size = 2  # Cooperate or Defect
        self.memory = deque(maxlen=memory_size)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0   # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.batch_size = 32
        
        # Create main models
        self.sequence_model = self._build_sequence_model()
        self.q_model = self._build_q_model()
        
        # Game statistics
        self.scores = []
        self.moves = []
        self.opponent_moves = []
        self.predictions = []
        
        # Initialize state scaler
        self.scaler = StandardScaler()
        
    def _build_sequence_model(self):
        """Build LSTM model for sequence prediction"""
        model = Sequential([
            LSTM(64, input_shape=(self.state_size, 1), return_sequences=True),
            LSTM(32),
            Dense(16, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model
    
    def _build_q_model(self):
        """Build Deep Q-Learning model"""
        # State input
        state_input = Input(shape=(self.state_size,))
        state_h1 = Dense(64, activation='relu')(state_input)
        state_h2 = Dense(32, activation='relu')(state_h1)
        
        # Prediction input
        pred_input = Input(shape=(1,))
        pred_h1 = Dense(8, activation='relu')(pred_input)
        
        # Combine state and prediction paths
        combined = concatenate([state_h2, pred_h1])
        combined_h1 = Dense(32, activation='relu')(combined)
        output = Dense(self.action_size, activation='linear')(combined_h1)
        
        model = Model(inputs=[state_input, pred_input], outputs=output)
        model.compile(optimizer=Adam(learning_rate=self.learning_rate), loss='mse')
        return model
    
    def preprocess_state(self, state):
        """Preprocess state for model input"""
        if len(state) < self.state_size:
            # Pad with zeros if not enough history
            state = [0] * (self.state_size - len(state)) + state
        return np.array(state[-self.state_size:])
    
    def predict_opponent_move(self, state):
        """Predict opponent's next move using LSTM"""
        state = np.array(state).reshape(1, self.state_size, 1)
        return self.sequence_model.predict(state, verbose=0)[0][0]
    
    def make_move(self, opponent_moves):
        """Make a move based on opponent's history"""
        state = self.preprocess_state(opponent_moves)
        
        # Predict opponent's next move
        opponent_prediction = self.predict_opponent_move(state)
        self.predictions.append(opponent_prediction)
        
        # Epsilon-greedy action selection
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
            
        scaled_state = self.scaler.fit_transform(state.reshape(-1, 1)).ravel()
        q_values = self.q_model.predict(
            [scaled_state.reshape(1, -1), 
             np.array([[opponent_prediction]])], verbose=0)
        return np.argmax(q_values[0])
    
    def remember(self, state, action, reward, next_state, opponent_pred):
        """Store experience in memory"""
        self.memory.append((state, action, reward, next_state, opponent_pred))
    
    def train_sequence_model(self, X, y, epochs=10):
        """Train LSTM sequence model"""
        X = np.array(X).reshape(-1, self.state_size, 1)
        return self.sequence_model.fit(X, y, epochs=epochs, verbose=0)
    
    def train_q_model(self):
        """Train Q-learning model on batch"""
        if len(self.memory) < self.batch_size:
            return
        
        minibatch = random.sample(self.memory, self.batch_size)
        
        for state, action, reward, next_state, opponent_pred in minibatch:
            scaled_state = self.scaler.fit_transform(state.reshape(-1, 1)).ravel()
            scaled_next_state = self.scaler.transform(next_state.reshape(-1, 1)).ravel()
            
            target = reward
            if reward is not None:
                next_q_values = self.q_model.predict(
                    [scaled_next_state.reshape(1, -1),
                     np.array([[opponent_pred]])], verbose=0)
                target = reward + self.gamma * np.amax(next_q_values[0])
            
            target_f = self.q_model.predict(
                [scaled_state.reshape(1, -1),
                 np.array([[opponent_pred]])], verbose=0)
            target_f[0][action] = target
            
            self.q_model.fit(
                [scaled_state.reshape(1, -1),
                 np.array([[opponent_pred]])],
                target_f, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
    
    def update_stats(self, my_move, opponent_move, score):
        """Update game statistics"""
        self.moves.append(my_move)
        self.opponent_moves.append(opponent_move)
        self.scores.append(score)

def run_advanced_simulation(num_rounds=1000, training_interval=50):
    """Run simulation with advanced bot"""
    bot = AdvancedGameBot()
    
    # Generate initial training data
    print("Generating initial training data...")
    X_train = []
    y_train = []
    for _ in range(1000):
        sequence = [random.choice([0, 1]) for _ in range(bot.state_size)]
        X_train.append(sequence)
        y_train.append(random.choice([0, 1]))
    
    # Initial sequence model training
    print("Training sequence model...")
    bot.train_sequence_model(X_train, y_train)
    
    # Main game loop
    print("Starting game simulation...")
    opponent_moves = []
    
    for round_num in tqdm(range(num_rounds)):
        # Get current state
        state = bot.preprocess_state(opponent_moves)
        
        # Make move
        bot_move = bot.make_move(opponent_moves)
        
        # Generate opponent move (random for simulation)
        opponent_move = random.choice([0, 1])
        opponent_moves.append(opponent_move)
        
        # Calculate reward
        score = calculate_score(bot_move, opponent_move)
        bot.update_stats(bot_move, opponent_move, score)
        
        # Get next state
        next_state = bot.preprocess_state(opponent_moves)
        
        # Store experience
        opponent_pred = bot.predictions[-1]
        bot.remember(state, bot_move, score, next_state, opponent_pred)
        
        # Periodic training
        if round_num % training_interval == 0 and round_num > 0:
            bot.train_q_model()
    
    return bot

def plot_advanced_metrics(bot):
    """Plot advanced performance metrics"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Score Distribution
    sns.histplot(bot.scores, kde=True, ax=ax1)
    ax1.set_title('Score Distribution')
    ax1.set_xlabel('Score')
    ax1.set_ylabel('Frequency')
    
    # Moving Average Score
    moving_avg = pd.Series(bot.scores).rolling(window=50).mean()
    ax2.plot(moving_avg, label='50-round Moving Average')
    ax2.set_title('Score Moving Average')
    ax2.set_xlabel('Round')
    ax2.set_ylabel('Average Score')
    ax2.legend()
    
    # Prediction Accuracy
    actual = bot.opponent_moves[1:]
    predictions = [1 if p > 0.5 else 0 for p in bot.predictions[:-1]]
    accuracy = [1 if a == p else 0 for a, p in zip(actual, predictions)]
    moving_acc = pd.Series(accuracy).rolling(window=50).mean()
    ax3.plot(moving_acc, label='Prediction Accuracy')
    ax3.set_title('Opponent Move Prediction Accuracy')
    ax3.set_xlabel('Round')
    ax3.set_ylabel('Accuracy')
    ax3.legend()
    
    # Strategy Evolution
    move_ratio = pd.Series(bot.moves).rolling(window=50).mean()
    ax4.plot(move_ratio, label='Cooperation Rate')
    ax4.set_title('Bot Strategy Evolution')
    ax4.set_xlabel('Round')
    ax4.set_ylabel('Cooperation Rate')
    ax4.legend()
    
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    from tqdm import tqdm
    
    print("Starting advanced game simulation...")
    bot = run_advanced_simulation(num_rounds=1000)
    
    print("\nGenerating performance visualizations...")
    plot_advanced_metrics(bot)
    
    print("\nFinal Statistics:")
    print(f"Average Score: {np.mean(bot.scores):.2f}")
    print(f"Final Prediction Accuracy: {np.mean(accuracy[-100:]):.2f}")
    print(f"Final Cooperation Rate: {np.mean(bot.moves[-100:]):.2f}")

