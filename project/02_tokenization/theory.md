
# Project 02 – Tokenization Theory

## Objective

The objective of this project is to understand how raw text is converted into **tokens** before it is processed by a Large Language Model (LLM).

Tokenization is one of the most important stages in the NLP pipeline because neural networks cannot directly understand text. They require structured tokens that can later be converted into numerical representations.

---

# Learning Objectives

After completing this project, you should understand:

* What is Tokenization?
* Why Tokenization is necessary
* Different types of tokenization
* Character Tokenization
* Word Tokenization
* Regex Tokenization
* Special Tokens
* Token Analysis
* Saving tokenized data

---

# Where Tokenization Fits

```text
Raw Dataset
      │
      ▼
Text Processing
      │
      ▼
Processed Dataset
      │
      ▼
Tokenization
      │
      ▼
Vocabulary
      │
      ▼
Token IDs
      │
      ▼
Embeddings
      │
      ▼
Transformer
```

---

# What is a Token?

A token is the smallest unit that a language model processes.

Example:

Sentence:

```text
python is a programming language.
```

Tokens:

```text
python
is
a
programming
language
.
```

---

# Why Tokenization?

Neural networks cannot process strings directly.

Instead of:

```text
python is amazing
```

The model receives:

```text
["python", "is", "amazing"]
```

Later these tokens are converted into integer IDs and embeddings.

---

# Types of Tokenization

## 1. Character Tokenization

Input:

```text
cat
```

Output:

```text
['c', 'a', 't']
```

---

## 2. Word Tokenization

Input:

```text
python is powerful
```

Output:

```text
["python", "is", "powerful"]
```

---

## 3. Regex Tokenization

Regex tokenizers separate punctuation from words.

Example:

```text
Hello, World!
```

Output:

```text
["Hello", ",", "World", "!"]
```

---

# Special Tokens

Modern LLMs use special tokens.

Examples:

```text
<BOS>   Beginning of Sentence

<EOS>   End of Sentence

<PAD>   Padding Token

<UNK>   Unknown Token
```

These tokens help the model understand sentence boundaries and handle unknown words.

---

# Token Analysis

In this project we will calculate:

* Total Documents
* Total Tokens
* Average Tokens per Document
* Longest Token Sequence
* Unique Tokens

---

# Project Pipeline

```text
Processed Dataset
        │
        ▼
Data Loader
        │
        ▼
Tokenizer
        │
        ▼
Token Analyzer
        │
        ▼
Writer
        │
        ▼
Tokenized Dataset
```

---

# Classes Implemented

* DataLoader
* WordTokenizer
* TokenAnalyzer
* CorpusWriter

Each class has a single responsibility.

---

# Output

This project generates:

```text
datasets/tokenized/
```

which contains tokenized documents ready for vocabulary creation.

---

# Conclusion

Tokenization converts processed text into structured tokens. These tokens become the foundation for vocabulary creation, token IDs, embeddings, and eventually transformer-based language models.
