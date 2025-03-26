import pandas as pd
url = "http://192.168.0.168:5000/get_attendance"
df = pd.read_csv(url)
print(df)
