import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    #try:

    pattern = r'<iframe[^>]*src=(["\'])(?:https?:)?//(?:www\.)?youtube\.com/embed/([^\'"?]+)'
    match = re.search(pattern, s)

    if match:
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"
    else:
        return None










if __name__ == "__main__":
    main()
