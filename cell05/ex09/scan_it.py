import sys

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = text.count(keyword)
    print(count if count > 0 else "none")
else:
    print("none") 