"""
Module responsible for JSONifying Reddit submissions.
"""

from datetime import datetime
from typing import Any

from reddit.wrapper import Submission


def parse_submission(submission: Submission) -> dict[str, Any]:
    """Change Reddit submission to a JSON-like dict

    Only a selected values are present in resulting JSON:
     - id
     - url
     - title
     - author
     - nsfw
     - spoiler
     - selftext
     - score
     - created_utc - in human-readable format, not UNIX time
     - shortlink
     - subreddit
     - stickied
     - media_url - custom parameter storing URL for media submissions

    Args:
        submission (Submission): Reddit submission to JSONify

    Returns:
        dict[str, Any]: dict containing JSONified submission
    """
    return {
        "id": submission.get("id"),
        "url": submission.get("url"),
        "title": submission.get("title"),
        "author": submission.get("author"),
        "nsfw": submission.get("over_18", False),
        "spoiler": submission.get("spoiler", False),
        "selftext": submission.get("selftext"),
        "score": submission.get("score"),
        "created_utc": datetime.fromtimestamp(submission.get("created_utc", 0)),
        "permalink": submission.get("permalink"),
        "subreddit": submission.get("subreddit"),
        "stickied": submission.get("stickied"),
        "media_url": _parse_media_url(submission),
    }


def _parse_media_url(submission: Submission) -> str:
    if "i.redd.it" in submission.get("domain", "") or "image" in submission.get("post_hint", ""):
        return submission.get("url")
    elif "v.redd.it" in submission.get("domain", "") and submission.get("is_video"):
        return submission["media"]["reddit_video"]["fallback_url"].replace("?source=fallback", "")
    else:
        return None
