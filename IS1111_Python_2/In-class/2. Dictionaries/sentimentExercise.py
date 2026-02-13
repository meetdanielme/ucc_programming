# ══════════════════════════════════════════════════════════════════
# OVERFLOW EXERCISE: REVIEW INSIGHTS
# Client: "ReviewRadar Analytics"
#
# Background:
# ReviewRadar is a small analytics firm that helps cafés and
# restaurants understand their customer feedback. They receive
# data as a single structured dictionary (like a JSON payload)
# containing the reviews and configuration settings.
#
# Your job: build functions that analyse this data using
# dictionary operations — counting, grouping, mapping, and
# extracting insights.
# ══════════════════════════════════════════════════════════════════

# All data arrives as one dictionary
data = {
    "cafe_name": "The Daily Grind",
    
    "reviews": [
        "The food was great and the service was fast",
        "The wait was slow and the coffee was cold",
        "Slow service and the food was cold and disappointing",
        "The music was loud and the wait was too slow",
        "Service was slow and food was average",
        "The coffee was cold and weak very disappointing",
        "Slow staff and the food was cold overall",
        "Excellent coffee and great food loved everything",
        "The wait was slow but the food was good",
        "Slow service and the atmosphere was poor",
    ],
    
    "config": {
        "common_words": [
            "the", "and", "was", "a", "but", "were", "would",
            "too", "come", "is", "it", "that", "this", "not",
            "at", "very", "overall"
        ],
        "positive_keywords": [
            "great", "loved", "fast", "friendly", "excellent",
            "good", "helpful", "amazing", "fantastic"
        ],
        "negative_keywords": [
            "slow", "cold", "weak", "loud", "bad", "rude",
            "average", "poor", "terrible", "disappointing"
        ]
    }
}


# ══════════════════════════════════════════════════════════════════
# TASK 1: count_all_words(data)
# ══════════════════════════════════════════════════════════════════
# Takes the data dictionary.
# Accesses the reviews list from data["reviews"].
# Counts how often each word appears (lowercase) using get().
# Returns a dictionary: word → count

def count_all_words(data):
    for review in data["reviews"]:
        words = review.lower().split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


# ══════════════════════════════════════════════════════════════════
# TASK 2: remove_common(word_counts, data)
# ══════════════════════════════════════════════════════════════════
# Takes a word counts dictionary and the data dictionary.
# Accesses common words from data["config"]["common_words"].
# Uses .copy() then loops through common words, using pop() to
# remove each one.
# Returns the cleaned dictionary.

def remove_common(word_counts, data):
    cleaned_counts = word_counts.copy()
    for common in data["config"]["common_words"]:
        cleaned_counts.pop(common, None)
    return cleaned_counts


# ══════════════════════════════════════════════════════════════════
# TASK 3: top_words(word_counts, n)
# ══════════════════════════════════════════════════════════════════
# Takes a word counts dictionary and a number n.
# Returns a list of the top n (word, count) tuples.
# Approach: work on a .copy(), repeatedly find the highest count
# using .items(), append to results, then pop it out.

def top_words(word_counts, n):
    word_counts_copy = word_counts.copy()
    top_n = []
    for _ in range(n):
        if not word_counts_copy:
            break
        top_word = max(word_counts_copy.values())
        for word, count in word_counts_copy.items():
            if count == top_word:
                top_n.append((word, count))
                word_counts_copy.pop(word)
                break
    return top_n


# ══════════════════════════════════════════════════════════════════
# TASK 4: extract_keywords(review_text, data)
# ══════════════════════════════════════════════════════════════════
# Takes a single review string and the data dictionary.
# Accesses keyword lists from data["config"].
# Returns a dictionary with the actual words found:
#   {"positive": [...], "negative": [...]}
#
# Example:
#   extract_keywords("Great food but slow service", data)
#   Returns: {"positive": ["great"], "negative": ["slow"]}

def extract_keywords(review_text, data):
    review_words = review_text.lower().split()
    positive_found = []
    negative_found = []
    
    for word in review_words:
        if word in data["config"]["positive_keywords"]:
            positive_found.append(word)
        elif word in data["config"]["negative_keywords"]:
            negative_found.append(word)
    
    return {"positive": positive_found, "negative": negative_found}


# ══════════════════════════════════════════════════════════════════
# TASK 5: map_reviews_to_keywords(data)
# ══════════════════════════════════════════════════════════════════
# Takes the data dictionary.
# Builds a dictionary mapping each review to its extracted keywords.
# Returns: {review_text: {"positive": [...], "negative": [...]}, ...}

def map_reviews_to_keywords(data):
    review_keyword_map = {}
    for review in data["reviews"]:
        review_keyword_map[review] = extract_keywords(review, data)
    return review_keyword_map


# ══════════════════════════════════════════════════════════════════
# TASK 6: group_by_sentiment(data)
# ══════════════════════════════════════════════════════════════════
# Takes the data dictionary.
# Groups reviews by sentiment score (positive count - negative count):
#   score > 0 → "positive"
#   score < 0 → "negative"
#   score == 0 → "neutral"
#
# Returns:
#   {"positive": [...], "negative": [...], "neutral": [...]}

def group_by_sentiment(data):
    grouped = {"positive": [], "negative": [], "neutral": []}
    for review in data["reviews"]:
        keywords = extract_keywords(review, data)
        score = len(keywords["positive"]) - len(keywords["negative"])
        if score > 0:
            grouped["positive"].append(review)
        elif score < 0:
            grouped["negative"].append(review)
        else:
            grouped["neutral"].append(review)
    return grouped


# ══════════════════════════════════════════════════════════════════
# TASK 7: count_negative_keywords(grouped, data)
# ══════════════════════════════════════════════════════════════════
# Takes the grouped reviews dict (from Task 6) and the data dict.
# Counts how often each negative keyword appears across the
# reviews in grouped["negative"].
# Returns: {negative_word: count, ...}
#
# This tells the owner which specific complaints come up most.

def count_negative_keywords(grouped, data):
    negative_counts = {}
    for review in grouped["negative"]:
        keywords = extract_keywords(review, data)
        for neg in keywords["negative"]:
            negative_counts[neg] = negative_counts.get(neg, 0) + 1
    return negative_counts


# ══════════════════════════════════════════════════════════════════
# TASK 8: print_dashboard(data)
# ══════════════════════════════════════════════════════════════════
# Brings everything together into a formatted dashboard.
# Accesses data["cafe_name"] for the header.
# Calls the functions above and prints:
#   - Overview stats
#   - Top 5 keywords with bar chart
#   - Sentiment breakdown
#   - Reviews grouped by category with their keywords shown
#   - Most common complaints ranked
#
# Bar chart hint: "█" * count
# Truncate long reviews: review[:38] + "..." if len > 38

def print_dashboard(data):
    cafe_name = data["cafe_name"]
    print(f"Review Dashboard for {cafe_name}")
    print("=" * 40)
    
    # Overview stats
    total_reviews = len(data["reviews"])
    print(f"Total reviews: {total_reviews}")
    
    # Top keywords
    word_counts = count_all_words(data)
    cleaned_counts = remove_common(word_counts, data)
    top_keywords = top_words(cleaned_counts, 5)
    
    print("\nTop Keywords:")
    for word, count in top_keywords:
        print(f"{word}: {'█' * count} ({count})")
    
    # Sentiment breakdown
    grouped = group_by_sentiment(data)
    print("\nSentiment Breakdown:")
    for sentiment, reviews in grouped.items():
        print(f"{sentiment.capitalize()}: {len(reviews)} reviews")
    
    # Reviews with keywords
    review_keyword_map = map_reviews_to_keywords(data)
    print("\nReviews with Extracted Keywords:")
    for review, keywords in review_keyword_map.items():
        truncated_review = review[:38] + "..." if len(review) > 38 else review
        print(f"{truncated_review} | Positive: {keywords['positive']} | Negative: {keywords['negative']}")
    
    # Common complaints
    negative_counts = count_negative_keywords(grouped, data)
    sorted_negatives = sorted(negative_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMost Common Complaints:")
    for neg, count in sorted_negatives:
        print(f"{neg}: {'█' * count} ({count})")


# ══════════════════════════════════════════════════════════════════
# Run the dashboard
# ══════════════════════════════════════════════════════════════════
print_dashboard(data)