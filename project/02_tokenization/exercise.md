
# Project 02 – Exercises

## Objective

These exercises will help you understand tokenization before building vocabularies and embeddings.

---

# Exercise 1

Answer the following questions.

1. What is tokenization?
2. Why do LLMs need tokenization?
3. What is a token?
4. Why can't neural networks process raw text directly?

---

# Exercise 2

Tokenize the following sentence into words.

```text
Python is a programming language.
```

---

# Exercise 3

Perform character tokenization.

```text
hello
```

Expected format:

```text
['h', 'e', 'l', 'l', 'o']
```

---

# Exercise 4

Perform word tokenization.

```text
Machine learning is amazing.
```

Write the resulting list of tokens.

---

# Exercise 5

Explain the difference between:

* Character Tokenization
* Word Tokenization
* Regex Tokenization

Write one advantage of each.

---

# Exercise 6

Explain the purpose of the following special tokens.

```text
<BOS>

<EOS>

<PAD>

<UNK>
```

---

# Exercise 7

Complete the pipeline.

```text
Processed Dataset

↓

_____________

↓

_____________

↓

_____________

↓

Tokenized Dataset
```

---

# Exercise 8

Explain the responsibility of each class.

* DataLoader
* WordTokenizer
* TokenAnalyzer
* CorpusWriter

---

# Exercise 9

Run the tokenizer and record the following statistics.

* Number of documents
* Total tokens
* Average tokens per document
* Longest token sequence
* Number of unique tokens

---

# Exercise 10

Challenge

Add a new processed document into:

```text
datasets/processed/
```

Run the tokenizer again and answer:

* Did the token count increase?
* Did the number of documents change?
* Did the longest token sequence change?
* Was the new tokenized file generated automatically?

Record your observations.

---

# Completion Checklist

* □ Data loaded successfully
* □ Documents tokenized successfully
* □ Token analysis completed
* □ Tokenized dataset saved
* □ Statistics generated
* □ All exercises completed

After completing these exercises, you will be ready to begin **Project 03 – Vocabulary**, where tokens are converted into a vocabulary and integer IDs.
