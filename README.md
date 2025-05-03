# Qi Layout

Optimize the arrangement of 30 characters—letters of the alphabet and punctuation symbols (, . - ;) - using the quantum computing cloud service from [Fixstars Amplify](https://amplify.fixstars.com).

## Getting Started

### Prerequisites

- python: 3.9 - 3.13
- Fixstars Amplify: 1.3.1

### Setting Up

Install required dependencies:

```bash
pip install numpy amplify
```

Prepare your training text data. It should only contain lowercase English letters and the following punctuation marks: comma (,), period (.), hyphen (-), and semicolon (;).

```text
abcdefghijklmnopqrstuvwxyz,.-;
```

### Running the Optimizatiojn

To generate a key layout:

```bash
python main.py
```

## Advanced Configuration

You can further customize the key layout optimization by modifying the files in the `model/` or `config/` directories.

If you create a custom model (e.g., `model/your_model.py`), you can specify it with the `--model_name` argument:

```bash
python main.py --model_name your_model
```
