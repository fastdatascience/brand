import re

with open("../README.md", "r", encoding="utf-8") as f:
    for l in f:
        l = l.strip()
        if len(l) == 6:
            colour = re.sub(r'[^0-9a-f]', '', l.lower())
            if len(colour) != 6:
                continue
            r = int(colour[:2], 16)
            g = int(colour[2:4], 16)
            b = int(colour[4:], 16)
            print (f"\n![{colour}](https://raw.githubusercontent.com/fastdatascience/brand/main/colours/{colour}.svg)\n```\n{colour}\n```\n```\nrgb({r}, {g}, {b})\n```\n")
            with open(colour + ".svg", "w", encoding="utf-8") as fo:
                fo.write(f'<svg viewBox="0 0 100 40" width="100" height="40" xmlns="http://www.w3.org/2000/svg"><rect x="0" y="0" width="100" height="40" style="fill:#{colour};stroke:#{colour}" /></svg>')
