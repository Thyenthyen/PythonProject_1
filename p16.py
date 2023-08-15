# Program name: p16
# Your Name: Ngoc Dan Thuyen Nguyen
# Python Version: 3.10.4
# Date Started - Date Finished: 6/3/2022
# Description:
'''
Write a program which uses a loop to display a conversion table,
with kilograms on the left and pounds on the right. Pounds are rounded
to 1 decimal digit.
1 kg = 2.2 lb
Include every other (odd) values of kilograms, from 1 to 199.
'''

print('Kilogram    Pounds')
for kg in range(1, 200, 2):
    lbs = 2.2 * kg
    print('%-8i'%kg,'   %.1f '%lbs)
           # %8i means insert the kg value but reserve 8 spaces for it.(lean to the right)
           # % -8i lean to the left.
'''
========== RESTART: C:\Users\Thyen\OneDrive\Máy tính\python hw\p16.py ==========
Kilogram    Pounds
1           2.2 
3           6.6 
5           11.0 
7           15.4 
9           19.8 
11          24.2 
13          28.6 
15          33.0 
17          37.4 
19          41.8 
21          46.2 
23          50.6 
25          55.0 
27          59.4 
29          63.8 
31          68.2 
33          72.6 
35          77.0 
37          81.4 
39          85.8 
41          90.2 
43          94.6 
45          99.0 
47          103.4 
49          107.8 
51          112.2 
53          116.6 
55          121.0 
57          125.4 
59          129.8 
61          134.2 
63          138.6 
65          143.0 
67          147.4 
69          151.8 
71          156.2 
73          160.6 
75          165.0 
77          169.4 
79          173.8 
81          178.2 
83          182.6 
85          187.0 
87          191.4 
89          195.8 
91          200.2 
93          204.6 
95          209.0 
97          213.4 
99          217.8 
101         222.2 
103         226.6 
105         231.0 
107         235.4 
109         239.8 
111         244.2 
113         248.6 
115         253.0 
117         257.4 
119         261.8 
121         266.2 
123         270.6 
125         275.0 
127         279.4 
129         283.8 
131         288.2 
133         292.6 
135         297.0 
137         301.4 
139         305.8 
141         310.2 
143         314.6 
145         319.0 
147         323.4 
149         327.8 
151         332.2 
153         336.6 
155         341.0 
157         345.4 
159         349.8 
161         354.2 
163         358.6 
165         363.0 
167         367.4 
169         371.8 
171         376.2 
173         380.6 
175         385.0 
177         389.4 
179         393.8 
181         398.2 
183         402.6 
185         407.0 
187         411.4 
189         415.8 
191         420.2 
193         424.6 
195         429.0 
197         433.4 
199         437.8 
'''
