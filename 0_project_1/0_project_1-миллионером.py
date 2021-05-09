#!/usr/bin/env python
# coding: utf-8

# Вопрос 1. У какого фильма из списка самый большой бюджет?

# In[3]:


import pandas as pd
data = pd.read_csv('/Users/tatiana/Downloads/movie_bd_v5.csv')
data_1 = data.groupby(['original_title'])['budget'].max().sort_values(ascending=False)
data_1.head(1)


# Вопрос 2. Какой из фильмов самый длительный (в минутах)?

# In[4]:


data_2 = data.groupby(['original_title'])['runtime'].max().sort_values(ascending=False)
data_2.head(1)


# Вопрос 3. Какой из фильмов самый короткий (в минутах)?

# In[14]:


data_3 = data.groupby(['original_title'])['runtime'].max().sort_values(ascending=False)
data_3.tail(1)


# Вопрос 4. Какова средняя длительность фильмов?

# In[18]:


data_4 = data.runtime.mean()
round(data_4)


# Вопрос 5. Каково медианное значение длительности фильмов?

# In[19]:


data_5 = data.runtime.median()
round(data_5)


# Вопрос 6. Какой фильм самый прибыльный?

# In[24]:


data['profit'] = data['revenue'] - data['budget']
data[data.profit==data.profit.max()].original_title


# Вопрос 7. Какой фильм самый убыточный?

# In[25]:


data['profit'] = data['revenue'] - data['budget']
data[data.profit==data.profit.min()].original_title


# Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[27]:


data['profit'] = data['revenue'] > data['budget']
data['profit'].value_counts()


# Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?

# In[28]:


data['profit'] = data['revenue'] - data['budget']
film_2008 = data[data.release_year==2008]
film_2008[(film_2008.profit==film_2008.profit.max())].original_title


# Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?

# In[29]:


data['profit'] = data['revenue'] - data['budget']
films_2012_2014 = data[data.release_year.between(2012,2014)]
films_2012_2014[(films_2012_2014.profit==films_2012_2014.profit.min())].original_title


# Вопрос 11. Какого жанра фильмов больше всего?

# In[31]:


data_11=data.copy()
data_11['genres'] = data_11['genres'].apply(lambda x: x.split('|'))
data_11 = data_11.explode('genres')
data_11['genres'].value_counts()


# Вопрос 12. Фильмы какого жанра чаще всего становятся прибыльными?

# In[32]:


data['profit'] = data['revenue']-data['budget']
profit_film = data[data.profit > 0].copy() 
profit_film.genres = profit_film.genres.str.split('|')
profit_genres = profit_film.explode('genres').genres 


# Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?

# In[35]:


data_by_director = data.copy()
data_by_director.director = data_by_director    .director.apply(lambda s: str(s).split("|"))
data_by_director = data_by_director.explode("director")
data_by_director = data_by_director    .groupby("director").revenue.sum()    .sort_values(ascending=False)    .index[0]
data_by_director


# Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?

# In[36]:


data_14 = data.copy()
data_14['director'] = data_14['director'].str.split('|')
data_14 = data_14.explode('director')
data_14['genres'] = data_14['genres'].str.split('|')
data_14 = data_14.explode('genres')
data_14[data_14['genres'] == 'Action'].director.value_counts().sort_values(ascending=False)


# Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?

# In[37]:


data_15 = data[data['release_year'] == 2012]
data_15.explode('cast').groupby(by='cast').sum().sort_values(by='revenue', ascending=False)


# Вопрос 16. Какой актер снялся в большем количестве высокобюджетных фильмов? Примечание: в фильмах, где бюджет выше среднего по данной выборке.

# In[54]:


data_16 = pd.read_csv('/Users/tatiana/Downloads/movie_bd_v5.csv')
data_16['cast']=data_16.cast.map(lambda x: x.split('|'))
data_16=data_16.explode('cast')
data_16[data_16['budget']>data_16['budget'].mean()].groupby('cast')[['original_title']].count(
).sort_values(by='original_title', ascending=False)


# Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?

# In[59]:


data_17 = data.copy()
data_17[data_17.cast.str.contains('Nicolas Cage', na=False)]


# Вопрос 18. Самый убыточный фильм от Paramount Pictures?

# In[63]:


data_18 = data.copy()
data_18['profit'] = data['revenue'] - data['budget']
data_18= data[data['production_companies'].str.contains('Paramount Pictures')]
data_18.groupby('original_title').profit.sum().sort_values(ascending=False)


# Вопрос 19. Какой год стал самым успешным по суммарным кассовым сборам?

# In[66]:


data_19 = pd.read_csv('/Users/tatiana/Downloads/movie_bd_v5.csv')
data_19 = data_19.groupby(['release_year']).revenue.sum().sort_values(ascending=False).index[0]
data_19


# Вопрос 20. Какой самый прибыльный год для студии Warner Bros?

# In[69]:


data['profit'] = data['revenue'] - data['budget']
data_20 = data[data['production_companies'].str.contains('Warner Bros')]
data_20.groupby('release_year').profit.sum().sort_values(ascending=False)


# Вопрос 21. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[71]:


data = pd.read_csv('/Users/tatiana/Downloads/movie_bd_v5.csv')
data.release_date = pd.to_datetime(data.release_date)
data[data.release_date.dt.month.isin([9])].shape[0]


# Вопрос 22. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?

# In[73]:


data.release_date = pd.to_datetime(data.release_date)
data[data.release_date.dt.month.isin([6,7,8])].shape[0]


# Вопрос 23. Для какого режиссера зима — самое продуктивное время года?

# In[77]:


data = pd.read_csv('/Users/tatiana/Downloads/movie_bd_v5.csv')
data['director'] = data['director'].apply(lambda x:x.split('|'))
data.release_date = data.release_date.apply(lambda x:x.split('/'))
data['month'] = data['release_date'].apply(lambda x:x[0])
pivot = data.loc[data['month'].isin([12, 1, 2])]
pivot['director'].value_counts().head(1)


# Вопрос 24. Какая студия даёт самые длинные названия своим фильмам по количеству символов?

# In[78]:


data['char_title_count'] = data['original_title'].apply(lambda x: len(x.replace(" ", " ")))
data.groupby('production_companies').char_title_count.mean().idxmax()


# Вопрос 25. Описания фильмов какой студии в среднем самые длинные по количеству слов?

# In[80]:


data_25 = data.copy()
data_25['overview_words_length'] = data_25.overview.map(lambda x: len(x.split(' ')))
data_25['production_companies'] = data_25['production_companies'].str.split('|')
data_25 = data_25.explode('production_companies')
data_25.groupby('production_companies')['overview_words_length'].mean(
).sort_values(ascending=False).index[0]


# Вопрос 26. Какие фильмы входят в один процент лучших по рейтингу?

# In[81]:


data.original_title[data.vote_average.quantile(.99) < data.vote_average]


# Вопрос 27. Какие актеры чаще всего снимаются в одном фильме вместе?

# In[86]:


import itertools as it
import pandas as pd
data = pd.read_csv('/Users/tatiana/Downloads/movie_bd_v5.csv')
data['cast_comb'] = data.cast.str.split('|').apply(lambda x: tuple(it.combinations(sorted(x),2)))
print('размерность data до explode',data.shape,'\n')
data = data.explode('cast_comb')
print('размерность data после explode',data.shape,'\n')
data.cast_comb.value_counts()


# In[ ]:




