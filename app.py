import pandas as pd
import numpy as np

np.random.seed(42)

students = 100

data = {
    "Student_ID": range(1, students + 1),
    "Gender": np.random.choice(["Male", "Female"], students),
    "Class": np.random.choice(["A", "B", "C"], students),
    "Marks": np.random.randint(35, 100, students),
    "Attendance": np.random.randint(50, 100, students),
    "Assignments": np.random.randint(1, 11, students)
}

df = pd.DataFrame(data)

df.to_csv("student_data.csv", index=False)

print("Dataset Created Successfully")
df.head()
