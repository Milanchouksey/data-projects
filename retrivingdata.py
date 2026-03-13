from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:96912427@localhost:3306/student_data")

df = pd.read_csv("student_marks_dataset.csv")

df.to_sql("students", engine, if_exists="replace", index=False)

print("Data inserted")
df.sort_values(by='Marks',ascending=False,inplace=True)
print(df)
'''display all the information of student'''
print(df.info())
"passing is 33 the student above the marks will we passed"
passing=df[df["Marks"]>33]
print(f"list of passing student\n",passing)
print(f"Total number of passing students: {len(passing)}")
'''list of top 10 student'''
print(f"top 10 student of class\n:{passing.head(10)}")
"""list of all the fail student"""
fail_student=df[df["Marks"]<=33]
print(f"list of the fail student\n:" ,fail_student)
print(f"total number of the fail student:{len(fail_student)}")
"""10 lest student"""
print(f"10 lest student\n:{df.tail(10)}")
"""list of student having same name and subject"""
same = df[(df["Name"] == "Milan") & (df["Subject"] == "Chemistry")]
print(f"list of student having same name and subject\n",same)
"""average marks of student in class"""
print(f"average marks of student:{df["Marks"].mean()}")
"""average of student in subject wise"""
print(f"average marks of student:{df.groupby("Subject")["Marks"].mean()}")
"""mass percentage """
pass_percentage = (len(passing) / len(df)) * 100
print("Pass Percentage:", pass_percentage)
"""grade of all the student"""
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 33:
        return "D"
    else:
        return "Fail"

df["Grade"] = df["Marks"].apply(grade)

print("Students with Grades:\n")
print(df[["Name","Subject","Marks","Grade"]])
df.to_sql("analysis_data", engine, if_exists="replace", index=False)