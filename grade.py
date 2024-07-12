
c1='''83
79
78
81
89
78
93
91
77
90
90
61
88
72
91
90
86
88
86
81
88
78
83
81
59
54
54
88
83
83
85
82
78
84
75
75
70'''
c2='''81
79
88
87
78
75
91
85
69
86
80
80
66
66
65
68
70
66
92
86
86
70
92
58
72
82
60
69
70
92
82
84
92
90'''
grade='''83
79
78
81
89
78
93
91
77
90
90
61
88
72
91
90
86
88
86
81
88
78
83
81
59
54
54
88
83
83
85
82
78
84
75
75
70
81
79
88
87
78
75
91
85
69
86
80
80
66
66
65
68
70
66
92
86
86
70
92
58
72
82
60
69
70
92
82
84
92
90'''
def stat(data):
    gs = data.split('\n')
    gs = [float(g) for g in gs]

    level = [int(l/10) for l in gs]
    count = {4:0,5:0, 6:0, 7:0,8:0,9:0,10:0}
    for x in level:
        c = count[x]
        count[x] = c + 1
    for k in count.keys():
        c = count[k]
        v = 100* c/len(gs)
        count[k] = (c, v)
    return count
import pandas as pd
x = [stat(c1),stat(c2), stat(grade)]
pdf0 = pd.DataFrame(x[0])
pdf1 = pd.DataFrame(x[1])
pdf2 = pd.DataFrame(x[2])
print(pdf0)
print(pdf1)
print(pdf2)