#==================================================
#Importing libraries
#==================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#==================================================
#Load dataset
#==================================================
df=pd.read_csv("StudentsPerformance.csv")

# Data exploration and cleaning

print(df.head(5).to_string())
df.info()
print(df.columns)
dup=df.duplicated().sum()
print(dup)
print(df.isnull().sum())
print(df.describe())
print(df.nunique())
print((df["parental level of education"]=="high school").sum())

# Lunch vs Score Analysis

lunch_vs_score=df.groupby("lunch")[["math score","reading score","writing score"]].mean()
lunch_vs_score.plot(kind="bar",color=["blue","red","green"])
plt.xlabel("Lunch",fontsize=15)
plt.ylabel("Score",fontsize=15)
plt.title("Relationship Between Lunch Type and Student Performance",fontsize=20)
plt.grid(axis="y")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
plt.savefig("lunch_vs_score.png")

# Gender vs score Analysis

gender_vs_score= df.groupby("gender")[["math score","reading score","writing score"]].mean()
gender_vs_score.plot(kind="bar")
plt.xlabel("Gender",fontsize=15)
plt.ylabel("Average Score",fontsize=15)
plt.title("Average scores by Gender",fontsize=20)
plt.grid(axis="y")
plt.tight_layout()
plt.xticks(rotation=0)
plt.show()
plt.savefig("gender_vs_score.png")

avg_scores=["math score","reading score","writing score"]

# Test preparation vs score

print(df.head(10))
testprep_vs_course=df.groupby("test preparation course")[avg_scores].mean()
testprep_vs_course.plot(kind="bar",color=["green","cyan","orange"])
plt.xlabel("Test preparation course",fontsize=15)
plt.ylabel("Average Score",fontsize=15)
plt.title("Effect of test preparation on Student scores",fontsize=20)
plt.grid(axis="y")
plt.tight_layout()
plt.xticks(rotation=0)
plt.show()
plt.savefig("testprep_vs_score.png")
labels=[["Math","Reading","Writing"]]
plt.show()

# Average score by subject Analysis

(df[avg_scores].mean()).plot(kind="bar",color=["green","cyan","orange"])
plt.xlabel("Subject",fontsize=15)
plt.ylabel("Average Score",fontsize=15)
plt.title("Average score by subject",fontsize=20)
plt.grid(axis="y")
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig("subjectaveragescores.png")
plt.show()

# Parental education vs score Analysis

order=["some high school","high school","some college","associate's degree","bachelor's degree","master's degree"]

parent_education = df.groupby("parental level of education")[avg_scores].mean()
ax = parent_education.reindex(order).plot(kind="bar")
ax.legend(title="Subject",bbox_to_anchor=(1.05, 1),loc="upper left")
plt.xlabel("Parental education", fontsize=15)
plt.ylabel("Average Score", fontsize=15)
plt.title("Average scores by parental education level", fontsize=20)
plt.grid(axis="y")
plt.tight_layout()
plt.xticks(rotation=0)
plt.savefig("parental_education.png")
plt.show()

# Distribution of scores of different subjects Analysis

fig,axes=plt.subplots(1,3)
df["math score"].plot(kind="hist", ax=axes[0],color="green")
df["reading score"].plot(kind="hist", ax=axes[1],color="cyan")
df["writing score"].plot(kind="hist", ax=axes[2],color="orange")
axes[0].set_title("Distribution of math score",fontsize=20)
axes[0].set_xlabel("Score",fontsize=15)
axes[0].set_ylabel("Frequency",fontsize=15)
axes[1].set_title("Distribution of reading score",fontsize=20)
axes[1].set_xlabel("Score",fontsize=15)
axes[1].set_ylabel("Frequency",fontsize=15)
axes[2].set_title("Distribution of writing score",fontsize=20)
axes[2].set_xlabel("Score",fontsize=15)
axes[2].set_ylabel("Frequency",fontsize=15)
plt.savefig("easiestsub.png")
plt.show()

# Corelation between reading and writing score 

plt.scatter(df["reading score"],df["writing score"])
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Relationship Between Reading and Writing Scores")
plt.savefig("reading_writing_correlation.png")
plt.show()


