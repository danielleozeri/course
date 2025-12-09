# Python course for beginners
# week 1

import pandas as pd

data = {
  "subject_number": [1, 2, 3, 4, 5, 6],
  "gender": ["F", "M", "F", "M", "M", "F"],
  "age": [27, 24, 30, 26, 40, 35],
  "depression": [0, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)
df.to_csv("subjects.csv", index=False)