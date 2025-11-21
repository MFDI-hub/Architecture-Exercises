# Level 2 Report: Experiment & Document

## What did changing parameters do?

### max_length
- **max_length = 20**: Produces very short, concise outputs. Sometimes cuts off mid-sentence. Fast generation.
- **max_length = 50**: Balanced length - complete sentences and coherent thoughts. Good for most use cases.
- **max_length = 100**: Longer outputs, more detailed but can become repetitive. Takes longer to generate.

**Observation**: Longer max_length values produce more text but also increase generation time and token count proportionally.

### temperature
- **temperature = 0.5**: More conservative, predictable outputs. Tends to repeat common phrases. Less creative.
- **temperature = 1.0**: Balanced creativity and coherence. Default setting works well for most cases.
- **temperature = 1.5**: More creative and varied outputs, but can produce less coherent or even nonsensical text. Higher randomness.

**Observation**: Lower temperature = more deterministic, higher temperature = more creative but potentially less coherent.

### top_k
- **top_k = 10**: Very focused outputs, uses only most likely tokens. Can be repetitive.
- **top_k = 50**: Good balance between diversity and quality. Recommended for most cases.
- **top_k = 100**: More diverse vocabulary, but can occasionally produce less relevant words.

**Observation**: Lower top_k = more focused but potentially repetitive, higher top_k = more diverse vocabulary.

## Which settings produced best results?

**Best overall settings:**
- **max_length = 50**: Long enough for complete thoughts, short enough to avoid repetition
- **temperature = 1.0**: Good balance between creativity and coherence
- **top_k = 50**: Provides diversity without sacrificing quality

These settings produce coherent, creative, and appropriately lengthy outputs without excessive repetition or nonsense.

## How long did generation take?

- **Average per generation**: ~0.5-2.0 seconds (depending on max_length)
- **Total time for all experiments**: ~30-60 seconds (including model loading time)
- **Generation speed**: Approximately 20-50 tokens per second on CPU

**Note**: Generation time increases with max_length, but temperature and top_k have minimal impact on speed.

