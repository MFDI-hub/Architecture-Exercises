# Level 4 Submission: Writing Assistant

## What I Built

A **Writing Assistant** tool that uses transformer models to help with text completion, generation, and summarization. The tool provides three main features:

1. **Text Completion** - Completes partial sentences or prompts using distilgpt2
2. **Multiple Suggestions** - Generates several alternative completions for a given prompt
3. **Text Summarization** - Summarizes longer texts using BART (facebook/bart-large-cnn)

## Why I Chose This

- **Practical**: Useful for writing assistance, brainstorming, and quick summaries
- **Demonstrates multiple transformer use cases**: Text generation and summarization
- **Simple but functional**: Not overly complex, but shows real-world application
- **Interactive**: Can be used in both demo and interactive modes

## Code Structure

- `writing_assistant.py` - Main implementation with WritingAssistant class
- Supports both demo mode (default) and interactive mode (`--interactive` flag)
- Uses two transformer models:
  - `distilgpt2` for text generation (lightweight, fast)
  - `facebook/bart-large-cnn` for summarization (high quality summaries)

## How to Run

```bash
# Demo mode (default)
python writing_assistant.py

# Interactive mode
python writing_assistant.py --interactive
```

## Demo Output

The tool successfully:
- Completes text prompts with relevant continuations
- Generates multiple variations/suggestions
- Summarizes longer texts effectively

Example outputs:
- Completion: "The future of artificial intelligence" → generates relevant continuation
- Suggestions: Multiple alternative ways to complete a prompt
- Summary: Condenses longer texts into key points

## What I Learned

1. **Model Selection**: Different models excel at different tasks (generation vs summarization)
2. **Prompt Engineering**: How you structure prompts affects output quality
3. **Pipeline API**: Using Hugging Face pipelines simplifies model usage
4. **Temperature Control**: Adjusting temperature affects creativity vs consistency
5. **Error Handling**: Need to handle edge cases (short texts, model errors)

## What I'd Improve Next

1. **Better Prompts**: Fine-tune prompts for more coherent completions
2. **Model Fine-tuning**: Fine-tune on specific domains (code, formal writing, etc.)
3. **UI**: Add a web interface or GUI for easier use
4. **More Features**: Add grammar checking, style transfer, or sentiment analysis
5. **Performance**: Cache models, add batch processing, optimize for speed
6. **Better Models**: Try larger models like GPT-2 or T5 for better quality

## Technical Details

- **Models Used**: 
  - distilgpt2 (text generation)
  - facebook/bart-large-cnn (summarization)
- **Dependencies**: transformers, torch
- **Python Version**: 3.8+
- **Features**: Text completion, suggestions, summarization, interactive mode

