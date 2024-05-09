#!/usr/bin/env python
# coding: utf-8

# ### 1. Import required libraries and read the provided dataset (youtube_dislike_dataset.csv) and retrieve top 5 and bottom 5 records.

# In[183]:


import pandas as pd
import numpy as np
import matplotlib. pyplot as plot
df = pd.read_csv(r"C:\Users\satya\Downloads\youtube_dislike_dataset (1).csv")


# In[139]:


df.head(5)


# In[140]:


df.tail(5)


# ### 2. Check the info of the dataframe and write your inferences on data types and shape of the dataset.

# In[141]:


df.info()


# In[181]:


type(df)


# In[143]:


df.shape


# In the above  output a summary of the dataframe's information, including the data types and non-null counts
# for each column. From this information, we can make inferences about the dataset's structure.
# The following dataframe consists of 37422 rows, 12 columns .Each rows represented the data about the video published .

# ### 3. Check for the Percentage of the missing values and drop or impute them.
# 

# In[144]:


missing_values = df.isnull().sum()


# In[145]:


missing_values


# In[146]:


df.isnull().sum()/(len(df)*100)


# In[147]:


df.drop(columns="comments",inplace = True)


# In[148]:


df.isnull().sum()


# ### 4. Check the statistical summary of both numerical and categorical columns and write your inferences

# In[149]:


numerical_summary = df.describe()


# In[150]:


categorical_summary = {}
for column in df.select_dtypes(include=['object']):
    categorical_summary[column] = df[column].value_counts()


# In[151]:


print("Statistical Summary for Numerical Columns:")
display(numerical_summary)


# The Numerical columns consist of view_counts, likes,dislikes,comment-counts. the statical summary for the numerical  datatypes provided with us  the discriptive details abouts our dataset.

# ### 5. Convert datatype of column published_at from object to pandas datetime.

# In[153]:


df['published_at'] = pd.to_datetime(df['published_at'])


# In[154]:


df.dtypes


# ### 6. Create a new column as 'published_month' using the column published_at (display the months only)

# In[155]:


df["published_month"]=df["published_at"].dt.month


# In[156]:


df


# ### 7. Replace the numbers in the column published_month as names of the months i,e., 1 as 'Jan', 2 as 'Feb' and so on....

# In[157]:


month_name = { 1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',
              7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}


# In[158]:


df['published_month']= df['published_month'].map(month_name)


# In[159]:


df


# ### 8. Find the number of videos published each month and arrange the months in a decreasing order base
# 

# In[160]:


videos_count = df.groupby('published_month')['video_id'].count().sort_values(ascending=False)

print(videos_count)


# ### 9. Find the count of unique video_id, channel_id and channel_title
# 

# In[161]:


unique_video_id_count = df['video_id'].nunique()
unique_channel_id_count = df['channel_id'].nunique()
# Count of unique channel_title
unique_channel_title_count = df['channel_title'].nunique()
# Display the counts
print("Count of unique video_id:", unique_video_id_count)
print("Count of unique channel_id:", unique_channel_id_count)
print("Count of unique channel_title:", unique_channel_title_count)


# ### 10. Find the top10 channel names having the highest number of videos in the dataset and the bottom10 having lowest number of videos.

# In[162]:


channel_video_counts = df.groupby('channel_title')['video_id'].count().reset_index()


# In[163]:


channel_video_counts = channel_video_counts.sort_values(by='video_id', ascending=False)


# In[164]:


top_10_channels = channel_video_counts.head(10)


# In[165]:


bottom_10_channels = channel_video_counts.tail(10)


# In[166]:


print("Top 10 channels with the highest number of videos:")
print(top_10_channels)


# In[167]:


print("\nBottom 10 channels with the lowest number of videos:")
print(bottom_10_channels)


# ### 11. Find the title of the video which has the maximum number of likes and the title of the video having minimum likes and write your inferences

# In[168]:


max_likes_video = df[df['likes'] == df['likes'].max()]['title'].values[0]
min_likes_video = df[df['likes'] == df['likes'].min()]['title'].values[0]
print("Video with maximum likes:", max_likes_video)
print("Video with minimum likes:", min_likes_video)


# The maximum liked videos are "BTS () 'Dynamite' Official MV" & the minimum liked videos are "Kim Kardashian's Must-See Moments on "Saturday Night Live" | E! News".
# 

# ### 12. Find the title of the video which has the maximum number of dislikes and the title of the video having  minimum dislikes and write your inferences

# In[169]:


max_dislikes_video = df.loc[df['dislikes'].idxmax()]

min_dislikes_video = df.loc[df['dislikes'].idxmin()]


# In[170]:


print("Video with maximum dislikes:")
print(max_dislikes_video['title'])
print("Number of dislikes:", max_dislikes_video['dislikes'])


# In[171]:


print("\nVideo with minimum dislikes:")
print(min_dislikes_video['title'])
print("Number of dislikes:", min_dislikes_video['dislikes'])


# The maximum disliked videos are "Cuties | Official Trailer | Netflix" & the minimum disliked videos are "Kim Kardashian's Must-See Moments on "Saturday Night Live" | E! News".

# ### 13. Does the number of views have any effect on how many people disliked the video? Support your answer with a metric and a plot                                   
# 

# In[172]:


corr = df ["view_count"].corr(df["dislikes"])


# In[173]:


corr


# In[182]:


plot.scatter(df["view_count"],df["dislikes"])
plot.xlabel("Views")
plot.ylabel("Dislikes")
plot.title("Correlation between Views and Dislikes")
plot.grid(True)
plot.show()


# The correlation between views and dislikes is 0.684.It means it's is having derived the relation and increased in one leads to 
# incresing another.

# ### 14. Display all the information about the videos that were published in January, and mention the count of videos that were published in January

# In[176]:


january_videos = df[df['published_month']=='Jan']


# In[177]:


january_videos.describe()


# In[178]:


january_videos.count= len(january_videos)


# In[179]:


january_videos.count

