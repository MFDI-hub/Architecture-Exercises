"""
Writing Assistant - A simple tool for text completion and suggestions using transformers
Uses distilgpt2 for text generation and BART for summarization
"""

from transformers import pipeline
import sys

class WritingAssistant:
    def __init__(self):
        print("Loading models... This may take a moment.")
        # Text generation model
        self.generator = pipeline('text-generation', model='distilgpt2')
        # Summarization model
        self.summarizer = pipeline('summarization', model='facebook/bart-large-cnn')
        print("Models loaded successfully!\n")
    
    def complete_text(self, prompt, max_length=50):
        """Complete the given text prompt"""
        result = self.generator(
            prompt,
            max_length=max_length,
            num_return_sequences=1,
            temperature=0.7,
            truncation=True,
            pad_token_id=self.generator.tokenizer.eos_token_id
        )
        return result[0]['generated_text']
    
    def generate_suggestions(self, prompt, num_suggestions=3):
        """Generate multiple completion suggestions"""
        results = self.generator(
            prompt,
            max_length=len(prompt.split()) + 30,
            num_return_sequences=num_suggestions,
            temperature=0.8,
            truncation=True,
            pad_token_id=self.generator.tokenizer.eos_token_id
        )
        suggestions = [result['generated_text'] for result in results]
        return suggestions
    
    def summarize_text(self, text):
        """Summarize the given text"""
        if len(text.split()) < 20:
            return "Text is too short to summarize meaningfully."
        
        try:
            result = self.summarizer(
                text,
                max_length=50,
                min_length=10,
                do_sample=False
            )
            return result[0]['summary_text']
        except Exception as e:
            return f"Error summarizing: {str(e)}"
    
    def interactive_mode(self):
        """Run in interactive mode"""
        print("=" * 60)
        print("Writing Assistant - Interactive Mode")
        print("=" * 60)
        print("\nCommands:")
        print("  complete <text>    - Complete the text")
        print("  suggest <text>    - Get multiple suggestions")
        print("  summarize <text>  - Summarize the text")
        print("  quit              - Exit\n")
        
        while True:
            try:
                user_input = input("> ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() == 'quit':
                    print("Goodbye!")
                    break
                
                if user_input.lower().startswith('complete '):
                    text = user_input[9:].strip()
                    if text:
                        print("\nCompleting text...")
                        completed = self.complete_text(text)
                        print(f"Completed: {completed}\n")
                    else:
                        print("Please provide text to complete.")
                
                elif user_input.lower().startswith('suggest '):
                    text = user_input[8:].strip()
                    if text:
                        print("\nGenerating suggestions...")
                        suggestions = self.generate_suggestions(text)
                        for i, sug in enumerate(suggestions, 1):
                            print(f"Suggestion {i}: {sug}")
                        print()
                    else:
                        print("Please provide text for suggestions.")
                
                elif user_input.lower().startswith('summarize '):
                    text = user_input[10:].strip()
                    if text:
                        print("\nSummarizing...")
                        summary = self.summarize_text(text)
                        print(f"Summary: {summary}\n")
                    else:
                        print("Please provide text to summarize.")
                
                else:
                    print("Unknown command. Use 'complete', 'suggest', 'summarize', or 'quit'.")
            
            except KeyboardInterrupt:
                print("\n\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}\n")

def demo():
    """Run a quick demo"""
    print("=" * 60)
    print("Writing Assistant - Demo Mode")
    print("=" * 60)
    
    assistant = WritingAssistant()
    
    # Demo 1: Complete text
    print("\n1. TEXT COMPLETION")
    print("-" * 60)
    prompt1 = "The future of artificial intelligence"
    print(f"Prompt: {prompt1}")
    completed = assistant.complete_text(prompt1, max_length=40)
    print(f"Completed: {completed}\n")
    
    # Demo 2: Generate suggestions
    print("2. MULTIPLE SUGGESTIONS")
    print("-" * 60)
    prompt2 = "In the next decade, technology will"
    print(f"Prompt: {prompt2}")
    suggestions = assistant.generate_suggestions(prompt2, num_suggestions=2)
    for i, sug in enumerate(suggestions, 1):
        print(f"Suggestion {i}: {sug}")
    print()
    
    # Demo 3: Summarize
    print("3. TEXT SUMMARIZATION")
    print("-" * 60)
    long_text = """
    Machine learning is a subset of artificial intelligence that enables 
    computers to learn from data without being explicitly programmed. 
    It uses algorithms to identify patterns in data and make predictions 
    or decisions. There are three main types: supervised learning, where 
    the model learns from labeled examples; unsupervised learning, where 
    it finds patterns in unlabeled data; and reinforcement learning, where 
    an agent learns through trial and error by receiving rewards or penalties. 
    Machine learning is used in many applications including image recognition, 
    natural language processing, recommendation systems, and autonomous vehicles.
    """
    print(f"Original text ({len(long_text.split())} words):")
    print(long_text.strip()[:150] + "...")
    summary = assistant.summarize_text(long_text)
    print(f"\nSummary: {summary}\n")
    
    print("=" * 60)
    print("Demo complete! Run with --interactive for interactive mode.")
    print("=" * 60)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        assistant = WritingAssistant()
        assistant.interactive_mode()
    else:
        demo()
