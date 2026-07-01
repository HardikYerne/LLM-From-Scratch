
# Project 01 – Exercises

## Objective

These exercises are designed to test your understanding of text preprocessing before moving to tokenization.

---

# Exercise 1

Answer the following questions.

1. What is a corpus?
2. What is the difference between a corpus and a document?
3. What is a sentence?
4. What is a word?
5. What is a character?

---

# Exercise 2

Draw the hierarchy of text.

```
Corpus

↓

Document

↓

Paragraph

↓

Sentence

↓

Word

↓

Character
```

Explain each level in your own words.

---

# Exercise 3

Given the following text:

```
Python      IS

A Programming Language.
```

Write the cleaned version.

---

# Exercise 4

Normalize the following words:

```
Python

PYTHON

python

PyThOn
```

Expected result:

```
python
```

---

# Exercise 5

Explain the responsibilities of each class.

* DataLoader
* TextCleaner
* TextNormalizer
* CorpusAnalyzer
* CorpusWriter

Write one sentence describing the purpose of each class.

---

# Exercise 6

Complete the pipeline.

```
Raw Dataset

↓

_____________

↓

_____________

↓

_____________

↓

_____________

↓

Processed Dataset
```

---

# Exercise 7

Why should we never modify the files inside `datasets/raw/`?

Write your answer in your own words.

---

# Exercise 8

Explain why cleaning and normalization are different processes.

Provide one example of each.

---

# Exercise 9

Run the project and record the following statistics.

* Number of documents
* Number of sentences
* Number of words
* Number of characters
* Average words per document
* Longest document

---

# Exercise 10

Challenge

Add one new text file to the `datasets/raw/` folder.

Run the pipeline again.

Observe:

* Did the document count change?
* Did the total word count increase?
* Did the longest document change?
* Were the processed files updated automatically?

Record your observations.

---

# Completion Checklist

* □ Dataset loaded successfully
* □ Text cleaned successfully
* □ Text normalized successfully
* □ Corpus analyzed successfully
* □ Processed dataset generated
* □ Statistics saved
* □ All exercises completed

After completing these exercises, you are ready to begin **Project 02 – Tokenization**.
