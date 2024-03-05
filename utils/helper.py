import os
from datetime import datetime, timedelta

import numpy as np
from groq import Groq


client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def ask_mixtral(messages: list):
    stream = client.chat.completions.create(
        messages=messages,
        model="mixtral-8x7b-32768",
        stream=True,
    )

    response = ""
    print()
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            response += content
            print(content, end="")
    print()

    return response


def convert_to_unix_epoch(input_str):
    """Converts raw datetime string into unix-epoch timestamp."""

    try:
        date_str, time_str = input_str.split(" ")

        dt = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(hours=5, minutes=30)
        tm = datetime.strptime(time_str, "%H:%M:%S%z")

        # Combine the date and time into a single datetime object
        combined_dt = dt.replace(hour=tm.hour, minute=tm.minute, second=tm.second)

        # Calculate the Unix epoch timestamp
        unix_epoch = (
            combined_dt - datetime(1970, 1, 1, tzinfo=combined_dt.tzinfo)
        ).total_seconds()

        return int(unix_epoch)
    except ValueError:
        return np.nan  # Return None for invalid input
