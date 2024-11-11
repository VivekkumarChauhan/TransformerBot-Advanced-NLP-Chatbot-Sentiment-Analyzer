from transformers import RobertaTokenizer, RobertaForSequenceClassification
import torch

# Load pre-trained RoBERTa model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)

def predict_sentiment(text):
    """
    Predict sentiment from input text using RoBERTa model.
    
    Parameters:
    text (str): Input text for sentiment analysis.
    
    Returns:
    dict: Sentiment label ('positive' or 'negative') and confidence score.
    """
    # Tokenize input text
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    
    # Perform inference using the model
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get prediction probabilities
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    
    # Get predicted label (0 for negative, 1 for positive)
    predicted_class = torch.argmax(probs, dim=1).item()
    
    # Map predicted class to sentiment label
    sentiment_label = 'positive' if predicted_class == 1 else 'negative'
    
    # Get confidence score
    confidence = probs[0][predicted_class].item()
    
    return {'label': sentiment_label, 'confidence': confidence}

# Example usage:
if __name__ == "__main__":
    sample_text = "I really love this movie!"
    result = predict_sentiment(sample_text)
    print(f"Sentiment: {result['label']}, Confidence: {result['confidence']:.2f}")
