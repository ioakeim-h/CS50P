from datetime import date
import re
import sys
from inflect import engine


def main():
    dob = input("Date of Birth: ").strip()
    year, month, day = validate(dob)
    minutes = convert_to_minutes(year, month, day)
    print(engine().number_to_words(minutes, andword='').capitalize(), "minutes")


def validate(dob):
  matches = re.search(r"^(\d{4})-(\d\d)-(\d\d)$", dob)

  if not matches:
    sys.exit("Invalid date")
  return matches.groups()


def convert_to_minutes(y, m, d):
  time_difference = date.today() - date(int(y),int(m),int(d))
  difference_in_days = str(time_difference)[:4]
  difference_in_minutes = int(difference_in_days) * 24 * 60
  return difference_in_minutes


if __name__ == "__main__":
    main()


