# Fake News Detection

This project focuses on detecting fake news articles using machine learning and natural language processing (NLP). By analyzing textual features, we train a model to classify news as either **real** or **fake**, helping to combat misinformation online.

## Problem Statement

With the rise of online news and social media, the spread of misinformation and fake news has become a major issue. Automated detection of fake news can help in curbing its impact and increasing the reliability of information on the internet.

The goal is to develop a classification model that can distinguish between real and fake news articles based on their textual content.

## Task

Given a news article (typically the title and text), predict whether it is **fake** or **real**.

## Datasets

The project uses three datasets available on Kaggle or other public repositories.

- **Features used**:
  - `title`: The title of the news article.
  - `text`: The full text of the news article.
  - `label`: Target variable (FAKE or REAL).

Dataset sources: [FakeNewsCorpus](https://github.com/several27/FakeNewsCorpus)
[WELFake](https://www.kaggle.com/datasets/saurabhshahane/fake-news-classification)
[LIAR](https://www.kaggle.com/datasets/doanquanvietnamca/liar-dataset)

## Approach

This is a **binary classification** task using supervised learning. The pipeline includes:

### 1. **Preprocessing**
- Lowercasing
- Removal of punctuation, stopwords, special characters, html tags, contractions etc.
- Tokenization and lemmatization

### 2. **Feature Extraction**
- Bag-of-Words (BoW)
- TF-IDF (Term Frequency–Inverse Document Frequency)
- Word embeddings (e.g., Word2Vec, GloVe, BERT embeddings)

### 3. **Modeling**
- Decision Trees
- Naive Bayes
- Random Forest
- Support Vector Machines (SVM)
- Deep Learning (LSTM, BERT, etc.)

### 4. **Evaluation**
- Accuracy
- Precision, Recall, F1 Score
- Confusion Matrix
