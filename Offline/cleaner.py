with open("leetcode.md", "r+") as f:
    lines = f.readlines()

    f.seek(0)

    for l in lines:
        f.write(l.strip() + "\n")
