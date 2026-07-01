
# Project 01 – Text Processing Theory

## Objective

The objective of this project is to understand how raw text is prepared before training a Large Language Model (LLM).

Large Language Models cannot directly understand raw text. Before text reaches a neural network, it must pass through several preprocessing stages. This project implements those stages from scratch.

---

# Learning Objectives

After completing this project, you should understand:

* What is a Corpus?
* What is a Document?
* What is a Sentence?
* What is a Word?
* What is a Character?
* Why text preprocessing is necessary
* Text Cleaning
* Text Normalization
* Corpus Analysis
* Saving processed datasets

---

# Text Hierarchy

```
Corpus
│
├── Document
│     ├── Paragraph
│     │      ├── Sentence
│     │      │      ├── Word
│     │      │      │      └── Character
```

Example:

```
Corpus
│
├── programming.txt
├── science.txt
├── history.txt
├── mathematics.txt
├── machine_learning.txt
└── daily_life.txt
```

---

# Corpus

A corpus is a collection of text documents used for Natural Language Processing (NLP) or training a language model.

Example:

```
datasets/raw/

programming.txt

science.txt

history.txt
```

Together these files form one corpus.

---

# Document

A document is a single text file inside the corpus.

Example:

```
programming.txt
```

---

# Sentence

A sentence is a meaningful sequence of words.

Example:

```
Python is a programming language.
```

---

# Word

Words are created by splitting a sentence.

Example:

```
Python

is

a

programming

language
```

---

# Character

Characters are the smallest text units.

Example:

```
Python

↓

P
y
t
h
o
n
```

---

# Why Text Preprocessing?

Raw text usually contains:

* Extra spaces
* Tabs
* Empty lines
* Mixed letter cases
* Inconsistent formatting

Preprocessing makes the dataset consistent and easier for later stages.

---

# Text Cleaning

Cleaning removes unnecessary noise.

Example:

Before:

```
Python      is

great.
```

After:

```
Python is great.
```

---

# Text Normalization

Normalization converts text into a standard format.

Example:

Before:

```
Python
PYTHON
python
```

After:

```
python
```

---

# Corpus Analysis

Corpus analysis helps us understand the dataset before training.

Metrics include:

* Number of documents
* Number of sentences
* Number of words
* Number of characters
* Average words per document
* Longest document

---

# Pipeline

```
Raw Dataset
      │
      ▼
Data Loader
      │
      ▼
Text Cleaner
      │
      ▼
Text Normalizer
      │
      ▼
Corpus Analyzer
      │
      ▼
Corpus Writer
      │
      ▼
Processed Dataset
```

---

# Classes Implemented

* DataLoader
* TextCleaner
* TextNormalizer
* CorpusAnalyzer
* CorpusWriter

Each class follows the Single Responsibility Principle, meaning each class performs only one specific task.

---

# Output

This project produces:

```
datasets/processed/
```

which contains cleaned and normalized text files ready for tokenization.

---

# Conclusion

Project 01 establishes the preprocessing pipeline required before tokenization. The processed corpus generated here becomes the input for Project 02, where we will implement tokenization from scratch.
