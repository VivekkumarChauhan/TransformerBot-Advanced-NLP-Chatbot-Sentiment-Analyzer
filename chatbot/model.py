from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

def generate_response(user_input):
    # Encode input
    inputs = tokenizer.encode(user_input, return_tensors='pt')
    
    # Generate output
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    
    # Decode output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response
