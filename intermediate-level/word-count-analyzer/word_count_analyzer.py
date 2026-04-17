# Word Count Analyzer
# Analyzes text and reports character count, word count, sentence count,
# most common words, and average word length.

def analyze_text(text):
    """Analyze a block of text and return statistics."""
    words = text.lower().split()
    sentences = text.count(".") + text.count("!") + text.count("?")

    # Clean punctuation from words for accurate counting
    clean_words = [word.strip(".,!?;:\"'()[]") for word in words]
    clean_words = [w for w in clean_words if w]

    # Count word frequency using a dictionary
    word_freq = {}
    for word in clean_words:
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sort by frequency (most common first)
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    avg_word_length = sum(len(w) for w in clean_words) / len(clean_words) if clean_words else 0

    return {
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "words": len(clean_words),
        "sentences": max(sentences, 1),
        "unique_words": len(word_freq),
        "avg_word_length": avg_word_length,
        "top_words": sorted_words[:5],
    }


def display_results(stats):
    """Display the analysis results."""
    print("\n===== Text Analysis =====")
    print(f"Characters (with spaces):    {stats['characters']}")
    print(f"Characters (without spaces): {stats['characters_no_spaces']}")
    print(f"Words:                       {stats['words']}")
    print(f"Sentences:                   {stats['sentences']}")
    print(f"Unique words:                {stats['unique_words']}")
    print(f"Average word length:         {stats['avg_word_length']:.1f} characters")
    print(f"\nTop 5 most common words:")
    for word, count in stats["top_words"]:
        print(f"  '{word}' — {count} time(s)")


print("Word Count Analyzer")
print("-" * 30)
print("Enter your text (press Enter twice to finish):\n")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

if text.strip():
    stats = analyze_text(text)
    display_results(stats)
else:
    print("No text entered.")
