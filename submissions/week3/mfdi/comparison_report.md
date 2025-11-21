# Level 3 Report: Model Comparison

## Comparison Table

| Model | Load Time | Avg Gen Time | Avg Tokens | Total Time | Model Size |
|-------|-----------|--------------|------------|------------|------------|
| distilgpt2 | ~2-5s | ~0.5-1.0s | ~50 | ~5-10s | ~82M params (~350MB) |
| gpt2 | ~3-8s | ~1.0-2.0s | ~50 | ~10-15s | ~124M params (~500MB) |
| gpt2-medium | ~5-15s | ~2.0-4.0s | ~50 | ~15-25s | ~355M params (~1.4GB) |

*Note: Actual times vary based on hardware and whether models are cached*

## Same Prompts Tested on All Models

All models were tested with these prompts:
1. "The future of AI is"
2. "In the year 2030"
3. "The secret to happiness is"
4. "Climate change will"
5. "The best programming language is"

## Generation Speed Analysis

- **distilgpt2**: Fastest generation (~0.5-1.0s per prompt)
- **gpt2**: Moderate speed (~1.0-2.0s per prompt)
- **gpt2-medium**: Slowest (~2.0-4.0s per prompt)

Speed scales roughly with model size - larger models take longer to generate.

## Output Quality (Subjective Analysis)

### distilgpt2
- **Pros**: Fast, lightweight, good for simple tasks
- **Cons**: Sometimes repetitive, less creative, can produce shorter outputs
- **Best for**: Quick prototypes, testing, simple text completion

### gpt2
- **Pros**: Better coherence than distilgpt2, more creative outputs
- **Cons**: Slower than distilgpt2
- **Best for**: Production use when you need balance between quality and speed

### gpt2-medium
- **Pros**: Most coherent and creative outputs, better context understanding
- **Cons**: Slowest, largest memory footprint
- **Best for**: High-quality text generation when speed isn't critical

## Model Size Comparison

- **distilgpt2**: Smallest (~350MB) - easiest to deploy
- **gpt2**: Medium (~500MB) - reasonable for most systems
- **gpt2-medium**: Largest (~1.4GB) - requires more resources

## Recommendations: Which Model for Which Use Case?

### Use distilgpt2 when:
- ✅ Fast iteration and testing needed
- ✅ Limited computational resources
- ✅ Simple text completion tasks
- ✅ Prototyping or development
- ✅ Real-time applications where speed matters

### Use gpt2 when:
- ✅ Need better quality than distilgpt2
- ✅ Have moderate computational resources
- ✅ Production applications requiring balance
- ✅ General-purpose text generation
- ✅ When quality matters but speed is still important

### Use gpt2-medium when:
- ✅ Quality is the top priority
- ✅ Have sufficient computational resources
- ✅ Non-real-time applications
- ✅ Complex text generation tasks
- ✅ When you can afford longer generation times

## Conclusion

The choice of model depends on your specific needs:
- **Speed priority**: distilgpt2
- **Balance**: gpt2
- **Quality priority**: gpt2-medium

For most practical applications, **gpt2** offers the best balance between quality and speed. Use **distilgpt2** for development and testing, and **gpt2-medium** when you need the highest quality outputs and can wait for generation.

