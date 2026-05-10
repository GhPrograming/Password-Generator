HI, i want to share this project with you. It is not the beste project but it was made for learning. 

IMPORTANT: those passwords are saved in plain text, so i sugest to be carefull. If you want, you can make your own custom password using my code

# PyPass-Gen

A cryptographically secure password generator written in Python. This tool generates high-entropy strings and logs them to a local file for later use.

## 📌 Overview

Standard random number generators (like Python's `random` module) are not suitable for security purposes. This script utilizes the `secrets` module, which is designed to generate numbers and characters that are unpredictable enough for passwords, account authentication, and security tokens.

## 🚀 Features

- **High Entropy:** Combines uppercase/lowercase letters, digits, and special characters.
- **Secure Randomization:** Powered by the `secrets` library (standard in Python 3.6+).
- **Auto-Logging:** Automatically appends generated passwords to `fisier.txt` for record-keeping.

## 🛠️ Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/pypass-gen.git](https://github.com/yourusername/pypass-gen.git)
   cd pypass-gen


  Run the script:

   python main.py

   ## 📝 Script Logic

- **Charset Definition:** Merges `ascii_letters`, `digits`, and `punctuation` into a single pool.
- **Generation Loop:** Iterates 10 times, picking a secure random character in each step.
- **File I/O:** Opens `fisier.txt` in **append mode** (`"a"`), ensuring previous passwords are not overwritten.

## ⚠️ Requirements

- **Python 3.6+**
- **No external dependencies** (uses standard library only).

---
*Developed for personal security and automation. Use with caution: ensure your password log file is kept in a secure, encrypted location.*
