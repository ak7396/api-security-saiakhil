'''
NOTE: This question must be attempted in a Python environment — either Google Colab, VS Code, or any standard Python IDE. The use of AI-assisted coding tools such as GitHub Copilot, ChatGPT, Gemini, or any AI autocomplete feature is strictly prohibited during this examination. You may refer only to official Python documentation. After executing, paste the code directly into the submission box, not the links.

Write a Python program that does all of the following:

1. creates a list of movie dictionaries with the keys title, rating, and revenue;
2. converts that data into a Pandas DataFrame;
3. removes rows where rating is missing;
4. filters movies with rating >= 8;
5. sorts the remaining rows by revenue in descending order;
6. prints the top 3 titles with their ratings;
7. creates a bar chart for the top 3 movie revenues using Matplotlib.

Note : you can use any type of onlie or offline ide , but don't use ai tool , ensure that you are not submitting links of platform where you coded , rather you properly copy the entire code and paste it back and the test platform
'''


import pandas as pd
import matplotlib.pyplot as plt   

movies=[

        {"title1":'ABCD',"rating":8.5,"Revenue":5000000},
        {"title2":'Dhookudu',"rating":9.5,"Revenue":2000000},
        {"title3":'Singam',"rating":9.5,"Revenue":1000000},
        {"title4":'ABCD2',"rating":6.5,"Revenue":1500000},
        {"title5":'Bhahubali',"rating":9.8,"Revenue":20000000},
        {"title6":'Bhahubali2',"rating":9.5,"Revenue":25000000},
        {"title7":'Salar',"rating":8.5,"Revenue":8000000},
        {"title8":'KGF',"rating":9.8,"Revenue":35000000},
        {"title9":'KGF2',"rating":9.5,"Revenue":45000000},
        {"title10":'Radheshyam',"rating":3.5,"Revenue":555000000}
]

#Convert to DataFrame
df = pd.DataFrame(movies)
# droping the rating row if not mentioned in data
df = df.dropna(subset=["rating"])
#filtering the rating which is greater than  and equal to 8
df = df[df["rating"] >= 8]
#sorting the values by revenue in decending order
df = df.sort_values(by="Revenue", ascending=False)
#printing top 3 movies 
top3 = df.head(3)
print(top3[["title", "rating"]])

#gettin into bar plot 
plt.bar(top3["title"], top3["Revenue"])
plt.xlabel("Movie Title")#labeling X and y
plt.ylabel("Revenue in cr")
plt.title("Top 3 Movie Revenues") #giving titlt
plt.show() #displaying plot
