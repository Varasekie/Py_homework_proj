import math
import numpy
s="语文:80,数学:82,英语:90, 物理: 85,化学:88,美术:80"
l1 = s.split(',')
# sub = []
score = []
for i in l1:
    # su
    score.append(int(i.split(':')[1]))

print(math.fsum(score))
print(numpy.mean(score))