"""
Reddit Data Collection for TikTok Slang Research
University of Warwick - CS310 Dissertation Project

This script collects posts from TikTok-related subreddits to identify
emerging slang terminology for linguistic analysis.
"""

import praw
import re
from datetime import datetime, timedelta

# Configuration
SUBREDDITS = [
    'TikTokCringe',
    'OutOfTheLoop',
    'GenZ',
    'NoStupidQuestions',
    'explainlikeimfive'
]

# Patterns to identify slang questions
SLANG_PATTERNS = [
    r"what does ['\"]?(\w+)['\"]? mean",
    r"what is ['\"]?(\w+)['\"]?",
    r"can someone explain ['\"]?(\w+)['\"]?",
    r"what's ['\"]?(\w+)['\"]?",
]


def initialize_reddit(client_id, client_secret, user_agent):
    """
    Initialize Reddit API connection
    
    Args:
        client_id: Reddit app client ID
        client_secret: Reddit app secret
        user_agent: User agent string
    
    Returns:
        praw.Reddit: Authenticated Reddit instance
    """
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )


def extract_potential_terms(text):
    """
    Extract potential slang terms from post text
    
    Args:
        text: Post title or body text
    
    Returns:
        list: Extracted terms that match slang question patterns
    """
    terms = []
    text_lower = text.lower()
    
    for pattern in SLANG_PATTERNS:
        matches = re.findall(pattern, text_lower, re.IGNORECASE)
        terms.extend(matches)
    
    return list(set(terms))  # Remove duplicates


def collect_posts_from_subreddit(reddit, subreddit_name, time_filter='week', limit=100):
    """
    Collect posts from a specific subreddit
    
    Args:
        reddit: Authenticated Reddit instance
        subreddit_name: Name of subreddit to collect from
        time_filter: Time period ('day', 'week', 'month')
        limit: Maximum number of posts to collect
    
    Returns:
        list: Collected posts with metadata
    """
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []
    
    # Collect from hot, top, and new
    for post in subreddit.hot(limit=limit // 3):
        terms = extract_potential_terms(post.title + " " + post.selftext)
        
        if terms:  # Only store posts with potential slang terms
            posts_data.append({
                'subreddit': subreddit_name,
                'title': post.title,
                'terms': terms,
                'created_utc': datetime.fromtimestamp(post.created_utc),
                'score': post.score,
                'url': post.url
            })
    
    return posts_data


def aggregate_term_frequencies(all_posts):
    """
    Aggregate frequency counts for discovered terms
    
    Args:
        all_posts: List of post data dictionaries
    
    Returns:
        dict: Term frequencies and metadata
    """
    term_freq = {}
    
    for post in all_posts:
        for term in post['terms']:
            if term not in term_freq:
                term_freq[term] = {
                    'count': 0,
                    'subreddits': set(),
                    'first_seen': post['created_utc']
                }
            
            term_freq[term]['count'] += 1
            term_freq[term]['subreddits'].add(post['subreddit'])
    
    return term_freq


def run_collection(client_id, client_secret, user_agent):
    """
    Main collection workflow
    
    Args:
        client_id: Reddit app client ID
        client_secret: Reddit app secret  
        user_agent: User agent string
    
    Returns:
        dict: Aggregated term frequencies and statistics
    """
    print("Initializing Reddit connection...")
    reddit = initialize_reddit(client_id, client_secret, user_agent)
    
    all_posts = []
    
    for subreddit_name in SUBREDDITS:
        print(f"Collecting from r/{subreddit_name}...")
        posts = collect_posts_from_subreddit(reddit, subreddit_name)
        all_posts.extend(posts)
        print(f"  Found {len(posts)} posts with potential slang terms")
    
    print(f"\nTotal posts collected: {len(all_posts)}")
    
    # Aggregate term frequencies
    term_frequencies = aggregate_term_frequencies(all_posts)
    
    # Sort by frequency
    sorted_terms = sorted(
        term_frequencies.items(),
        key=lambda x: x[1]['count'],
        reverse=True
    )
    
    print(f"\nDiscovered {len(sorted_terms)} unique potential terms")
    print("\nTop 10 terms:")
    for term, data in sorted_terms[:10]:
        print(f"  '{term}': {data['count']} mentions across {len(data['subreddits'])} subreddits")
    
    return {
        'terms': sorted_terms,
        'total_posts': len(all_posts),
        'collection_date': datetime.now()
    }


if __name__ == "__main__":
    # Example usage (credentials should be loaded from environment variables)
    import os
    
    CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
    CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
    USER_AGENT = os.getenv('REDDIT_USER_AGENT', 'TikTokDictionaryResearch/1.0')
    
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Error: Reddit API credentials not found in environment variables")
        print("Please set REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET")
    else:
        results = run_collection(CLIENT_ID, CLIENT_SECRET, USER_AGENT)
        
        # Results would be sent to Django backend for ML processing
        print("\nCollection complete. Results ready for ML classification.")
