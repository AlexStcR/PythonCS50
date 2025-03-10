import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s+([aApP][mM])\s+[tT][oO]\s+(\d{1,2})(?::(\d{2}))?\s+([aApP][mM])$'
    match = re.search(pattern, s.strip())
    if not match:
        raise ValueError("Invalid input format")

    hour_1 = int(match.group(1))
    minutes_1 = match.group(2)
    period_start = match.group(3).lower()
    hour_2 = int(match.group(4))
    minutes_2 = match.group(5)
    period_end = match.group(6).lower()

    if not (1 <= hour_1 <= 12) or not (1 <= hour_2 <= 12):
        raise ValueError("Hour out of range")

    if minutes_1 is None:
        minutes_1 = '00'
    else:
        if not (0 <= int(minutes_1) < 60):
            raise ValueError("Invalid minutes")
    if minutes_2 is None:
        minutes_2 = '00'
    else:
        if not (0 <= int(minutes_2) < 60):
            raise ValueError("Invalid minutes")

    # Convert start hour
    if period_start == 'pm':
        if hour_1 != 12:
            hour_1 += 12
    else:
        if hour_1 == 12:
            hour_1 = 0

    # Convert end hour
    if period_end == 'pm':
        if hour_2 != 12:
            hour_2 += 12
    else:
        if hour_2 == 12:
            hour_2 = 0

    return f"{hour_1:02}:{minutes_1} to {hour_2:02}:{minutes_2}"


if __name__ == "__main__":
    main()
