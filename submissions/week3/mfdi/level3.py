# Install (run in terminal first):
# uv venv
# uv pip install transformers torch

import time
import os
from transformers import pipeline

# Models to compare
models = [
    'distilgpt2',      # Smallest, fastest
    'gpt2',            # Medium size
    'gpt2-medium',     # Larger
]

# Test prompts
test_prompts = [
    "The future of AI is",
    "In the year 2030",
    "The secret to happiness is",
    "Climate change will",
    "The best programming language is"
]

# Results storage
results = {}

print("=" * 80)
print("LEVEL 3: MODEL COMPARISON")
print("=" * 80)
print("\nThis will download models if not already cached. This may take a while...\n")

for model_name in models:
    print(f"\n{'='*80}")
    print(f"Testing model: {model_name}")
    print(f"{'='*80}\n")
    
    # Load model and measure loading time
    load_start = time.time()
    try:
        generator = pipeline('text-generation', model=model_name)
        load_time = time.time() - load_start
        print(f"Model loaded in {load_time:.2f} seconds")
    except Exception as e:
        print(f"Error loading {model_name}: {e}")
        continue
    
    # Get model size
    try:
        model_path = generator.model.config.name_or_path
        # Try to get actual file size from cache
        cache_dir = os.path.expanduser("~/.cache/huggingface/hub")
        model_size_mb = 0
        if os.path.exists(cache_dir):
            # This is approximate - actual size would require checking all files
            print("Note: Model size calculation is approximate")
    except:
        pass
    
    model_results = {
        'load_time': load_time,
        'generations': [],
        'total_gen_time': 0,
        'avg_gen_time': 0,
        'total_tokens': 0,
        'avg_tokens': 0
    }
    
    # Test generation on all prompts
    gen_start_total = time.time()
    for prompt in test_prompts:
        gen_start = time.time()
        try:
            output = generator(
                prompt,
                max_length=50,
                num_return_sequences=1,
                truncation=True,
                do_sample=True,
                temperature=1.0,
                top_k=50
            )
            gen_time = time.time() - gen_start
            
            generated_text = output[0]['generated_text']
            token_count = len(generator.tokenizer.encode(generated_text))
            
            model_results['generations'].append({
                'prompt': prompt,
                'output': generated_text,
                'time': gen_time,
                'tokens': token_count
            })
            
            model_results['total_gen_time'] += gen_time
            model_results['total_tokens'] += token_count
            
            print(f"  Prompt: {prompt}")
            print(f"  Generated: {generated_text[:80]}...")
            print(f"  Time: {gen_time:.3f}s | Tokens: {token_count}")
            print()
            
        except Exception as e:
            print(f"  Error generating for '{prompt}': {e}")
    
    model_results['total_gen_time'] = time.time() - gen_start_total
    model_results['avg_gen_time'] = model_results['total_gen_time'] / len(test_prompts)
    model_results['avg_tokens'] = model_results['total_tokens'] / len(test_prompts)
    
    results[model_name] = model_results
    
    # Clean up to save memory
    del generator
    import gc
    gc.collect()

# Print comparison table
print("\n" + "=" * 80)
print("COMPARISON TABLE")
print("=" * 80)
print(f"\n{'Model':<20} {'Load Time':<12} {'Avg Gen Time':<15} {'Avg Tokens':<12} {'Total Time':<12}")
print("-" * 80)

for model_name, data in results.items():
    print(f"{model_name:<20} {data['load_time']:<12.2f} {data['avg_gen_time']:<15.3f} {data['avg_tokens']:<12.1f} {data['total_gen_time']:<12.2f}")

# Model size information (approximate)
print("\n" + "=" * 80)
print("MODEL SIZE INFORMATION (Approximate)")
print("=" * 80)
print("distilgpt2: ~82M parameters (~350MB)")
print("gpt2:       ~124M parameters (~500MB)")
print("gpt2-medium: ~355M parameters (~1.4GB)")

# Save detailed results to file
with open('model_comparison_results.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 80 + "\n")
    f.write("MODEL COMPARISON RESULTS\n")
    f.write("=" * 80 + "\n\n")
    
    for model_name, data in results.items():
        f.write(f"\n{'='*80}\n")
        f.write(f"Model: {model_name}\n")
        f.write(f"{'='*80}\n")
        f.write(f"Load Time: {data['load_time']:.2f} seconds\n")
        f.write(f"Average Generation Time: {data['avg_gen_time']:.3f} seconds\n")
        f.write(f"Average Tokens: {data['avg_tokens']:.1f}\n")
        f.write(f"Total Generation Time: {data['total_gen_time']:.2f} seconds\n\n")
        
        f.write("Generated Outputs:\n")
        f.write("-" * 80 + "\n")
        for gen in data['generations']:
            f.write(f"\nPrompt: {gen['prompt']}\n")
            f.write(f"Output: {gen['output']}\n")
            f.write(f"Time: {gen['time']:.3f}s | Tokens: {gen['tokens']}\n")
            f.write("\n")
    
    f.write("\n" + "=" * 80 + "\n")
    f.write("RECOMMENDATIONS\n")
    f.write("=" * 80 + "\n\n")
    f.write("distilgpt2: Best for quick prototyping, testing, and when speed is critical.\n")
    f.write("            Use when: Fast iteration needed, limited resources, simple tasks.\n\n")
    f.write("gpt2:       Good balance between quality and speed.\n")
    f.write("            Use when: Need better quality than distilgpt2, moderate resources.\n\n")
    f.write("gpt2-medium: Best quality but slowest and largest.\n")
    f.write("            Use when: Quality is priority, have sufficient resources/time.\n")

print("\n" + "=" * 80)
print("RECOMMENDATIONS")
print("=" * 80)
print("\ndistilgpt2: Best for quick prototyping, testing, and when speed is critical.")
print("            Use when: Fast iteration needed, limited resources, simple tasks.")
print("\ngpt2:       Good balance between quality and speed.")
print("            Use when: Need better quality than distilgpt2, moderate resources.")
print("\ngpt2-medium: Best quality but slowest and largest.")
print("            Use when: Quality is priority, have sufficient resources/time.")

print("\nDetailed results saved to model_comparison_results.txt")

