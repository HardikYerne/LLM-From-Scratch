
# Project 02 – Tokenization

## Overview

Tokenization is the process of converting text into smaller units called **tokens**. Before a Large Language Model (LLM) can understand text, it must first break the text into tokens that can later be converted into numerical representations.

In this project, we build a tokenizer **completely from scratch** without using external NLP libraries such as Hugging Face Tokenizers, SentencePiece, spaCy, or NLTK.

The output of **Project 01 – Text Processing** becomes the input for this project.

---

# Learning Objectives

After completing this project, you will understand:

* Why tokenization is required
* How tokenizers work internally
* Character Tokenization
* Word Tokenization
* Regex Tokenization
* Special Tokens
* Token Analysis
* Saving tokenized datasets

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
Corpus Writer
        │
        ▼
Tokenized Dataset
```

---

# Project Structure

```text
02_tokenization/

├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── tokenizer.py
│   ├── analyzer.py
│   └── writer.py
│
├── output/
│
├── tests/
│
├── README.md
├── theory.md
├── exercise.md
└── requirements.txt
```

---

# Components

## 1. DataLoader

Responsibilities:

* Load processed text files
* Read all documents from `datasets/processed/`
* Store them in memory

---

## 2. WordTokenizer

Responsibilities:

* Split text into tokens
* Preserve token order
* Process every document

Example:

Input:

```text
python is amazing
```

Output:

```python
["python", "is", "amazing"]
```

---

## 3. TokenAnalyzer

Responsibilities:

* Count total documents
* Count total tokens
* Count unique tokens
* Calculate average tokens per document
* Find the longest tokenized document

---

## 4. CorpusWriter

Responsibilities:

* Save tokenized documents
* Save token statistics
* Generate output files

---

# Input

This project reads data from:

```text
datasets/processed/
```

Example:

```text
datasets/
└── processed/
    ├── programming.txt
    ├── science.txt
    ├── history.txt
    ├── mathematics.txt
    ├── machine_learning.txt
    └── daily_life.txt
```

---

# Output

The tokenizer generates:

```text
datasets/
└── tokenized/
    ├── programming.txt
    ├── science.txt
    ├── history.txt
    ├── mathematics.txt
    ├── machine_learning.txt
    ├── daily_life.txt
    └── statistics.json
```

---

# Current Features

* Load processed corpus
* Tokenize every document
* Analyze token statistics
* Save tokenized documents
* Save analysis report

---

# Technologies Used

* Python 3
* pathlib
* json
* Regular Expressions (Regex)

---

# Skills Learned

* NLP preprocessing pipeline
* Tokenization concepts
* Data loading
* Token analysis
* File handling
* Clean project architecture
* Single Responsibility Principle (SRP)

---

# Project Workflow

```text
Project 01
Raw Dataset
      │
      ▼
Processed Dataset
      │
      ▼
Project 02
Data Loader
      │
      ▼
Tokenizer
      │
      ▼
Token Analyzer
      │
      ▼
Corpus Writer
      │
      ▼
Tokenized Dataset
```

---

# Future Improvements

The tokenizer will be expanded in later stages to support:

* Character Tokenization
* Regex Tokenization
* Special Tokens (`<BOS>`, `<EOS>`, `<PAD>`, `<UNK>`)
* Byte Pair Encoding (BPE)
* GPT-style Tokenization

---

# Next Project

The output of this project becomes the input for:

**Project 03 – Vocabulary**

In the next project, every unique token will receive a unique integer ID, preparing the data for embedding layers and transformer models.
