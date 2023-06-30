import pandas as pd

with open('kernel.txt','r') as file:
    data = file.read().split('\n')

# split the list in chunks of 7s
chunks = [data[x:x+7] for x in range(0, len(data), 7)]

# pass the chunks in pd.DataFrame and specify the columns names of the OP:
info = pd.DataFrame(chunks, columns=["Hostname", "OS Version", "System Date", "System Uptime", "Installed Kernel Date", "Installed Kernel", "Available Kernel"])
print(info)
info.to_csv('test.csv', index=False)