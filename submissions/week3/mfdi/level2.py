# Install (run in terminal first):
# uv venv
# uv pip install transformers torch

import time
from transformers import pipeline

# Load a small model
generator = pipeline('text-generation', model='distilgpt2')

# 5 different prompts (your choice of topics)
prompts = [
    "The future of AI is",
    "In the year 2030",
    "The secret to happiness is",
    "Climate change will",
    "The best programming language is"
]

# Experiment with different parameters
max_lengths = [20, 50, 100]
temperatures = [0.5, 1.0, 1.5]
top_ks = [10, 50, 100]

# Open file for writing results
with open('results.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("LEVEL 2: EXPERIMENT & DOCUMENT\n")
    f.write("=" * 80 + "\n\n")
    
    # Experiment 1: Different max_length values
    f.write("EXPERIMENT 1: Varying max_length\n")
    f.write("-" * 80 + "\n")
    for max_len in max_lengths:
        f.write(f"\nmax_length = {max_len}\n")
        f.write("-" * 40 + "\n")
        for prompt in prompts[:2]:  # Test with first 2 prompts
            start_time = time.time()
            output = generator(
                prompt, 
                max_length=max_len, 
                num_return_sequences=1,
                truncation=True
            )
            elapsed_time = time.time() - start_time
            
            generated_text = output[0]['generated_text']
            token_count = len(generator.tokenizer.encode(generated_text))
            
            f.write(f"\nPrompt: {prompt}\n")
            f.write(f"Generated: {generated_text}\n")
            f.write(f"Time: {elapsed_time:.3f} seconds\n")
            f.write(f"Token count: {token_count}\n")
            f.write("\n")
    
    # Experiment 2: Different temperature values
    f.write("\n\n" + "=" * 80 + "\n")
    f.write("EXPERIMENT 2: Varying temperature\n")
    f.write("-" * 80 + "\n")
    for temp in temperatures:
        f.write(f"\ntemperature = {temp}\n")
        f.write("-" * 40 + "\n")
        for prompt in prompts[:2]:  # Test with first 2 prompts
            start_time = time.time()
            output = generator(
                prompt, 
                max_length=50,
                temperature=temp,
                num_return_sequences=1,
                truncation=True
            )
            elapsed_time = time.time() - start_time
            
            generated_text = output[0]['generated_text']
            token_count = len(generator.tokenizer.encode(generated_text))
            
            f.write(f"\nPrompt: {prompt}\n")
            f.write(f"Generated: {generated_text}\n")
            f.write(f"Time: {elapsed_time:.3f} seconds\n")
            f.write(f"Token count: {token_count}\n")
            f.write("\n")
    
    # Experiment 3: Different top_k values
    f.write("\n\n" + "=" * 80 + "\n")
    f.write("EXPERIMENT 3: Varying top_k\n")
    f.write("-" * 80 + "\n")
    for top_k in top_ks:
        f.write(f"\ntop_k = {top_k}\n")
        f.write("-" * 40 + "\n")
        for prompt in prompts[:2]:  # Test with first 2 prompts
            start_time = time.time()
            output = generator(
                prompt, 
                max_length=50,
                top_k=top_k,
                num_return_sequences=1,
                truncation=True
            )
            elapsed_time = time.time() - start_time
            
            generated_text = output[0]['generated_text']
            token_count = len(generator.tokenizer.encode(generated_text))
            
            f.write(f"\nPrompt: {prompt}\n")
            f.write(f"Generated: {generated_text}\n")
            f.write(f"Time: {elapsed_time:.3f} seconds\n")
            f.write(f"Token count: {token_count}\n")
            f.write("\n")
    
    # Final: All 5 prompts with best settings
    f.write("\n\n" + "=" * 80 + "\n")
    f.write("FINAL: All 5 prompts with optimized settings\n")
    f.write("Settings: max_length=50, temperature=1.0, top_k=50\n")
    f.write("-" * 80 + "\n")
    
    total_start_time = time.time()
    for prompt in prompts:
        start_time = time.time()
        output = generator(
            prompt, 
            max_length=50,
            temperature=1.0,
            top_k=50,
            num_return_sequences=1,
            truncation=True
        )
        elapsed_time = time.time() - start_time
        
        generated_text = output[0]['generated_text']
        token_count = len(generator.tokenizer.encode(generated_text))
        
        f.write(f"\nPrompt: {prompt}\n")
        f.write(f"Generated: {generated_text}\n")
        f.write(f"Time: {elapsed_time:.3f} seconds\n")
        f.write(f"Token count: {token_count}\n")
        f.write("\n")
    
    total_time = time.time() - total_start_time
    f.write(f"\nTotal generation time: {total_time:.3f} seconds\n")
    f.write("=" * 80 + "\n")

print("Results saved to results.txt")
print("\nSummary:")
print("- Experimented with max_length: 20, 50, 100")
print("- Experimented with temperature: 0.5, 1.0, 1.5")
print("- Experimented with top_k: 10, 50, 100")
print("- Tested 5 different prompts")
print("- Timed all generations")
print("- Counted tokens in all outputs")

