#!/usr/bin/python3

# open(0) for stdin
cmds = [("LR".find(l[0])*2-1)*int(l[1:]) for l in open(0).read().splitlines()]
res, pos = 0, 50
for c in cmds:
  pos += c
  if pos >= 100:
    pos = pos % 100
  if pos < 0:
    #pos = 100 - (pos % 100)
    pos = pos - 100*(pos // 100)
  print(f"+ {c} -> {pos}")
  if pos == 0:
    res += 1
print(f"part 1: {res}")