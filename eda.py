import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed_tweets.csv")

#data manipulation 
df.drop("Unnamed: 0", axis=1, inplace=True)
df.drop("post_id", axis=1, inplace=True)
df.drop("user_id", axis=1, inplace=True)
df["frequency"] = df["post_text"].apply(lambda x: len(str(x).split(" "))) 

#datetime object
df.post_created=df.post_created.apply(pd.to_datetime)
df["month"]=df.post_created.dt.month
df["year"]=df.post_created.dt.year
df.drop("post_created", axis=1, inplace=True)

# frequency per month
sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.set(rc = {'figure.figsize':(11,5)})
sns.barplot(data=df, x="month", y="frequency").set(title="Frequency of tweets per month")
plt.savefig('figure/freq_month.png')
plt.clf()

# followers per month
sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.set(rc = {'figure.figsize':(11,5)})
sns.barplot(data=df, x="month", y="followers").set(title="Followers per month")
plt.savefig('figure/follower_month.png')
plt.clf()

# frequency per year
sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.set(rc = {'figure.figsize':(11,5)})
sns.barplot(data=df, x="year", y="frequency").set(title="Frequency of tweets per year")
plt.savefig('figure/freq_year.png')
plt.clf()

# followers per year
sns.set_style("whitegrid")
sns.despine(left=True, bottom=True)
sns.set_context("poster", font_scale = .5, rc={"grid.linewidth": 0.6})
sns.set(rc = {'figure.figsize':(11,5)})
sns.barplot(data=df, x="year", y="followers").set(title="Followers per year")
plt.savefig('figure/follower_year.png')
