# CV Ranking And Filtering Tool

This tool allows you to rank and filter CVs using a domain-specific language (DSL) for command parsing.

## Installation

- Python 3.13.3: [Download here](https://www.python.org/downloads/)
- ANTLR: [Download here](https://repo1.maven.org/maven2/org/antlr/antlr4/4.9.2/)

## Runing the repository

1. Clone this repository:

   ```bash
   git clone https://github.com/quynhanhhoang572004/CV-Ranking.git
   ```

2. Download

```bash
 pip install antlr4-python3-runtime
```

3. Try Out The Features
   a. Generate CVs

```bash
 cd generator
 python CVGenerator.py
```

b. Compile and test the grammar:
Suppose the ANTLR jar is saved in YOUR_ANTLR_JAR_PATH in your local computer.

```bash
 cd grammars
 java -jar YOUR_ANTLR_JAR_PATH -Dlanguage=Python3 -o ../CompiledFiles JDMatcher.g4
 cd ..
 python runMatcher.py test
```

c. Generate the Visitor classes

```bash
java -jar YOUR_ANTLR_JAR_PATH -Dlanguage=Python3 -o ../parse  -visitor JD.g4
```

d. Run the visitor

```bash
  python -m tests.test_validator
```

## List of available commands

```bash
  list all CVs for job backend developer
```

```bash
  show CV with gpa: >= 3.5
```

```bash
  show top 5 best CV for ai engineer
```

```bash
 jd input (read JD.txt)
```
