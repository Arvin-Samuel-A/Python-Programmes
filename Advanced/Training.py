import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
from tqdm import tqdm

class TrainingAnalyzer:
    def __init__(self):
        self.training_times = []
        self.accuracies = []
        self.game_scores = []
        self.sample_sizes = []
        
    def analyze_training_performance(self, sample_sizes=[1000, 2000, 5000, 10000, 20000], 
                                   num_validation_rounds=100,
                                   num_trials=5):
        """Analyze training performance for different sample sizes"""
        results = []
        
        for size in tqdm(sample_sizes, desc="Analyzing sample sizes"):
            trial_metrics = []
            
            for trial in range(num_trials):
                # Create and train bot
                start_time = time.time()
                bot = GameBot()
                bot.generate_training_data(num_samples=size)
                training_time = time.time() - start_time
                
                # Validate performance
                validation_score = self.validate_bot(bot, num_validation_rounds)
                prediction_accuracy = self.test_prediction_accuracy(bot)
                
                trial_metrics.append({
                    'sample_size': size,
                    'training_time': training_time,
                    'validation_score': validation_score,
                    'prediction_accuracy': prediction_accuracy
                })
            
            results.extend(trial_metrics)
            
        return pd.DataFrame(results)
    
    def validate_bot(self, bot, num_rounds):
        """Run validation games and return average score"""
        total_score = 0
        opponent_moves = [random.choice([0, 1]) for _ in range(num_rounds)]
        
        for round_num in range(num_rounds):
            current_opponent_moves = opponent_moves[:round_num]
            bot_move = bot.make_move(current_opponent_moves)
            opponent_move = opponent_moves[round_num]
            score = calculate_score(bot_move, opponent_move)
            total_score += score
            
        return total_score / num_rounds
    
    def test_prediction_accuracy(self, bot):
        """Test bot's prediction accuracy on a test set"""
        X_test = [[random.choice([0, 1]) for _ in range(5)] for _ in range(100)]
        y_test = [random.choice([0, 1]) for _ in range(100)]
        
        predictions = bot.model.predict(X_test)
        return accuracy_score(y_test, predictions)
    
    def plot_training_analysis(self, results_df):
        """Plot comprehensive training analysis"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Training Time vs Sample Size
        sns.boxplot(data=results_df, x='sample_size', y='training_time', ax=ax1)
        ax1.set_title('Training Time vs Sample Size')
        ax1.set_xlabel('Number of Training Samples')
        ax1.set_ylabel('Training Time (seconds)')
        
        # Validation Score vs Sample Size
        sns.boxplot(data=results_df, x='sample_size', y='validation_score', ax=ax2)
        ax2.set_title('Game Performance vs Sample Size')
        ax2.set_xlabel('Number of Training Samples')
        ax2.set_ylabel('Average Score per Round')
        
        # Prediction Accuracy vs Sample Size
        sns.boxplot(data=results_df, x='sample_size', y='prediction_accuracy', ax=ax3)
        ax3.set_title('Prediction Accuracy vs Sample Size')
        ax3.set_xlabel('Number of Training Samples')
        ax3.set_ylabel('Prediction Accuracy')
        
        # Training Time vs Performance Scatter
        sns.scatterplot(data=results_df, x='training_time', y='validation_score', 
                       size='prediction_accuracy', sizes=(50, 400), ax=ax4)
        ax4.set_title('Training Time vs Performance')
        ax4.set_xlabel('Training Time (seconds)')
        ax4.set_ylabel('Average Score per Round')
        
        plt.tight_layout()
        plt.show()
        
        return results_df.groupby('sample_size').agg({
            'training_time': ['mean', 'std'],
            'validation_score': ['mean', 'std'],
            'prediction_accuracy': ['mean', 'std']
        })

def find_optimal_training_params():
    """Find optimal training parameters based on performance metrics"""
    analyzer = TrainingAnalyzer()
    
    # Analyze different sample sizes
    results = analyzer.analyze_training_performance()
    
    # Plot results
    summary_stats = analyzer.plot_training_analysis(results)
    
    # Find optimal sample size based on performance/time trade-off
    results['efficiency'] = results['validation_score'] / results['training_time']
    optimal_size = results.groupby('sample_size')['efficiency'].mean().idxmax()
    
    # Calculate recommended training time
    optimal_time = results[results['sample_size'] == optimal_size]['training_time'].mean()
    
    return {
        'optimal_sample_size': optimal_size,
        'recommended_training_time': optimal_time,
        'full_results': summary_stats
    }

# Example usage
if __name__ == "__main__":
    import seaborn as sns
    
    # Run analysis
    optimal_params = find_optimal_training_params()
    
    print("\nOptimal Training Parameters:")
    print(f"Optimal sample size: {optimal_params['optimal_sample_size']:,} samples")
    print(f"Recommended training time: {optimal_params['recommended_training_time']:.2f} seconds")
    print("\nDetailed Performance Metrics:")
    print(optimal_params['full_results'])