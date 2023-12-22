import requests
import argparse
from datetime import datetime

TEMPLATE = """\
On this day, the {date}..

{events}
"""


def get_ordinal_suffix(day):
    if 10 <= day % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    return suffix


def on_this_day(month: int, day: int):
    """Get a list of events that occurred on a given month / day.

    Arguments:
        month (int): Target month (1-12).
        day (int): Target day (1-31).
    """

    api_url = f"https://byabbe.se/on-this-day/{month}/{day}/events.json"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        events = ""

        for e in data["events"]:
            events += f"{e['year']}: \t{e['description']}\n"

        date = datetime(year=2023, month=month, day=day).strftime(
            f"%d{get_ordinal_suffix(day)} of %B"
        )
        print(TEMPLATE.format(date=date, events=events))

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error checking {api_url}: {e}")


def main():
    parser = argparse.ArgumentParser(
        description='Get the Wikipedia "On this day.." events.'
    )
    parser.add_argument("month", type=int, help="The target month (1-12)")
    parser.add_argument("day", type=int, help="The target day (1-31)")

    args = parser.parse_args()
    on_this_day(args.month, args.day)


if __name__ == "__main__":
    main()
