# backend/emotion_text.py

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

def detect_text_emotion(text):
    """
    Takes user text as input.
    Returns detected emotion as a string.
    """

    if not text or text.strip() == "":
        return "neutral"

    # Get sentiment scores
    scores = analyzer.polarity_scores(text)

    # scores looks like:
    # {'neg': 0.0, 'neu': 0.3, 'pos': 0.7, 'compound': 0.85}

    compound = scores['compound']
    neg      = scores['neg']
    pos      = scores['pos']

    # Map scores to emotions
    if compound >= 0.5:
        return "happy"
    elif compound <= -0.5:
        if neg > 0.5:
            return "angry"
        else:
            return "sad"
    elif neg > 0.3:
        return "fear"
    else:
        return "neutral"


# -----------------------------------------------
# Quick test — run this file directly to check
# -----------------------------------------------
if __name__ == "__main__":
    test_sentences = [
        "I am so happy and excited today!",
        "I feel very sad and lonely",
        "I am furious and extremely angry!",
        "I am scared and frightened",
        "I went to the store today"
    ]

    print("\n🧪 Testing Emotion Detection:")
    print("-" * 40)
    for sentence in test_sentences:
        emotion = detect_text_emotion(sentence)
        print(f"Text    : {sentence}")
        print(f"Emotion : {emotion}")
        print("-" * 40)