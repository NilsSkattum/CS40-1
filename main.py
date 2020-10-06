import json
import matplotlib.pyplot as plt

#plot1
subjectDict = dict()
keyword = 'gender' #KeyError: bornCountry
filenames = [
    'nobel_laureate.json',
    'airline_delay.json'
]
#read
with open('nobel_laureate.json', 'r') as f1, open('airline_delay.json', 'r') as f2:
    lines = json.loads(f1.read())
    items = json.loads(f2.read())
    #analyze
    # print(lines.keys())
    # print(lines.values())
l = lines.values()
for line in l:
    for item in line:
        try:
            subjectDict[item[keyword]] += 1
        except Exception:
            subjectDict[item[keyword]] = 1
        else:
            pass
#visualize
fig, ax = plt.subplots()
ax = plt.subplot(1, 2, 1)
ax.set(ylabel="Number of Nobel Laureate", xlabel="Gender")
ax.bar(subjectDict.keys(), subjectDict.values())
fig.tight_layout()

#plot2
key_list = []
value_list = []
keyword_1 = 'Weather'
reason1_list = []
keyword_2 = 'Carrier'
reason2_list = []

#read
#analyze
for item in items:
    if item['Time']['Year'] not in key_list:
        key_list.append(item['Time']['Year'])
        value_list.append(item['Statistics']['# of Delays'])
    else:
        for key, value in item['Statistics']['# of Delays'].items():
            value_list[-1][key] += value 
for item in value_list:
    reason1_list.append(item[keyword_1])
    reason2_list.append(item[keyword_2])
# #visualize
plt.subplot(1,2,2)
plt.plot(key_list, reason1_list, label=keyword_1)
plt.plot(key_list, reason2_list, label=keyword_2)
plt.ylabel("Number of delays")
plt.xlabel("Year")
plt.legend()

#show all
plt.tight_layout(pad=2.3)
plt.show()




