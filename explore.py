import pandas as pd 
import numpy as np 

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

def count_percent(df):
    labels = pd.concat([df.language.value_counts(), df.language.value_counts(normalize=True)], axis=1)
    labels.columns = ['n', 'percent']
    return labels

def readme_length(df):
    df["length"]= df.readme.str.split().str.len()
    return df.groupby("language").length.agg(["min","mean","max"])

def words_dict(df):
    words={}
    for lang in df.language.unique():
        words["{}_words".format(lang.lower())] = ' '.join(df[df.language == lang].prepared)
    words["all_words"] = ' '.join(df.prepared) 
    return words

def word_count_by_lang(words):
    all_freq = pd.Series(words["all_words"].split()).value_counts()
    javas_freq = pd.Series(words["javascript_words"].split()).value_counts()
    python_freq = pd.Series(words["python_words"].split()).value_counts()
    java_freq = pd.Series(words["java_words"].split()).value_counts()
    none_freq = pd.Series(words["none_words"].split()).value_counts()

    word_counts = (pd.concat([all_freq, javas_freq, python_freq, java_freq, none_freq], axis=1, sort=True)
                    .set_axis(['all', 'javascript', 'python', 'java', 'none'], axis=1, inplace=False)
                    .fillna(0)
                    .apply(lambda s: s.astype(int)))
    return word_counts

def one_word_one_cloud(words, title):
    plt.figure(figsize=(10, 6))
    cloud = WordCloud(background_color='white', width=1200, height=800).generate(words)

    plt.imshow(cloud)
    plt.title(title)
    plt.axis("off")
    plt.show()

def one_word_two_cloud(words1, words2, title1, title2):
    cloud1 = WordCloud(background_color='white', height=1600, width=1200).generate(words1)
    cloud2 = WordCloud(background_color='white', height=1600, width=1200).generate(words2)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.6, 0, .5, 1])]

    axs[0].imshow(cloud1)
    axs[1].imshow(cloud2)

    axs[0].set_title(title1)
    axs[1].set_title(title2)

    for ax in axs: ax.axis('off')

def two_word_two_cloud(words1, words2, title1, title2):
    data = {k[0] + ' ' + k[1]: v for k, v in words1.to_dict().items()}
    cloud1 = WordCloud(background_color='white', width=800, height=800).generate_from_frequencies(data)

    data = {k[0] + ' ' + k[1]: v for k, v in words2.to_dict().items()}
    cloud2 = WordCloud(background_color='white', width=800, height=800).generate_from_frequencies(data)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.6, 0, .5, 1])]

    axs[0].imshow(cloud1)
    axs[1].imshow(cloud2)

    axs[0].set_title(title1)
    axs[1].set_title(title2)

    for ax in axs: ax.axis('off')

def three_word_two_cloud(words1, words2, title1, title2):
    data = {k[0] + ' ' + k[1] + ' ' + k[2]: v for k, v in words1.to_dict().items()}
    cloud1 = WordCloud(background_color='white', width=1000, height=800).generate_from_frequencies(data)

    data = {k[0] + ' ' + k[1] + ' ' + k[2]: v for k, v in words2.to_dict().items()}
    cloud2 = WordCloud(background_color='white', width=1000, height=800).generate_from_frequencies(data)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.6, 0, .5, 1])]

    axs[0].imshow(cloud1)
    axs[1].imshow(cloud2)

    axs[0].set_title(title1)
    axs[1].set_title(title2)

    for ax in axs: ax.axis('off')
