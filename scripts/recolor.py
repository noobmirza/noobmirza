import re, sys
p = "profile-3d-contrib/profile-night-view.svg"
s = open(p, encoding="utf-8").read()
s = re.sub(r'<svg style="[^"]*" ', '<svg ', s)
def blue(m):
    r, g, b = map(int, m.groups())
    return "rgb(%d, %d, %d)" % (min(255, int(b * .66)), int(g * .55), b)
s = re.sub(r'rgb\((\d+), (\d+), (\d+)\)', blue, s)
for a, b in (("rgb(255,200,55)", "#a78bfa"), ("#b07219", "#8b5cf6"), ("#3572A5", "#c4b5fd")):
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
