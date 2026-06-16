import re

DUR = 118.116
PAD = 0.07
# cortes manuales (tiempo original): tartamudeos + relleno/arranques fallidos
MANUAL_CUTS = [
    [4.30, 5.78],     # "y sea lo de casina de hace" (arranque fallido)
    [11.34, 15.52],   # relleno garbled
    [70.54, 72.08],   # tartamudeo freidora 1
    [72.74, 75.60],   # tartamudeo freidora 2
    [90.50, 98.00],   # "mas o menos para que te des una idea" + pausa
    [107.26, 109.24], # "no se que te quiero decir con esto"
]

# parsear silencios reales (silencedetect)
nums = []
for line in open("silences.txt"):
    p = line.split()
    if len(p) == 2:
        nums.append((p[0], float(p[1])))
sil = []
i = 0
while i < len(nums) - 1:
    if nums[i][0] == "start" and nums[i + 1][0] == "end":
        sil.append([nums[i][1], nums[i + 1][1]]); i += 2
    else:
        i += 1

cuts = list(MANUAL_CUTS)
for s, e in sil:
    if s <= 0.05:
        cuts.append([0, max(0, e - 0.08)])           # lead-in
    elif e >= DUR - 0.1:
        cuts.append([s + 0.08, DUR])                 # cola
    elif e - s > 2 * PAD:
        cuts.append([s + PAD, e - PAD])              # pausa interna

cuts = [c for c in cuts if c[1] > c[0]]
cuts.sort()
merged = []
for c in cuts:
    if merged and c[0] <= merged[-1][1] + 0.001:
        merged[-1][1] = max(merged[-1][1], c[1])
    else:
        merged.append(list(c))

keeps = []
cur = 0.0
for cs, ce in merged:
    if cs > cur:
        keeps.append([cur, cs])
    cur = max(cur, ce)
if cur < DUR:
    keeps.append([cur, DUR])
keeps = [k for k in keeps if k[1] - k[0] > 0.05]

fg = ""
for i, (a, b) in enumerate(keeps):
    fg += f"[0:v]trim=start={a:.3f}:end={b:.3f},setpts=PTS-STARTPTS[v{i}];\n"
    fg += f"[0:a]atrim=start={a:.3f}:end={b:.3f},asetpts=PTS-STARTPTS[a{i}];\n"
fg += "".join(f"[v{i}][a{i}]" for i in range(len(keeps)))
fg += f"concat=n={len(keeps)}:v=1:a=1[v][a]"
open("filter.txt", "w").write(fg)

total = sum(b - a for a, b in keeps)
print(f"keeps={len(keeps)} | dur final={total:.2f}s (de {DUR}s, -{DUR-total:.2f}s)")
