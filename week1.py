# Python course for beginners
# week 7

import pandas as pd

data = {
    "subject_number": np.arange(1,101,1),
    "age": np.random.randint(15,46,size=100),
    "gender": np.random.choice(['F','M'], size=100),
    "depression": np.random.binomial(n=1, p=0.15, size=100)
}

df = pd.DataFrame(data)
df.to_csv("subjects.csv", index=False)