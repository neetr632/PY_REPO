combined_numbers = """
85596
90467
73607
72087
96940
95636
78333
82340
89208
101462
77941
84818
90467
95636
110135
93108
80676
106590
86295
109960
85215
74499
75556
77804
82820
105354
76950
89790
80950
73298
72359
73048
80880
91677
83335
106590
79042
93812
76023
87138
98114
79658
110446
90001
108369
85596
95636
98114
95636
72448
90001
93927
86295
85215
110156
111633
98326
84370
"""

# Split the numbers into a list and convert them to integers
combined_numbers_list = [int(num) for num in combined_numbers.split()]

# Find the unique numbers
unique_combined_numbers = set(combined_numbers_list)

# Count the unique numbers
total_unique_combined_numbers = len(unique_combined_numbers)

total_unique_combined_numbers
print(total_unique_combined_numbers)