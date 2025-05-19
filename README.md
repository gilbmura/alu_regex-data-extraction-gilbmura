# alu_regex-data-extraction-gilbmura
# 🔍 Regex Data Extraction Tool

This project is a Python-based command-line application built to **extract and validate structured data** such as email addresses, URLs, phone numbers, currency amounts, and HTML tags using **Regular Expressions (Regex)**.

It was developed as part of the Regex Onboarding Hackathon challenge during the Full Stack Developer track.

---

## 🚀 Project Overview

You’ve landed a gig to build a Web Application for a private organization. Your API pulls in massive amounts of string data from the web — now you need a tool to scan and validate specific types of data.

This CLI tool scans input text files and validates each line against specific patterns using regex.

---

## ✅ Features

* 📁 Reads from input `.txt` files
* 🧪 Validates common data types using regex
* 🧼 Clean and modular code
* 🔄 Handles multiple formats and edge cases
* 🖥️ CLI-based menu interface

---

## 🧠 Data Types Extracted

| Data Type        | Regex Pattern Used                                                                |
| ---------------- | --------------------------------------------------------------------------------- |
| **Currency**     | `^\$\d{1,3}(,\d{3})*(\.\d{2})?$` or `^\$\d+(\.\d{2})?$`                           |
| **Phone Number** | `^(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$`                        |
| **HTML Tag**     | `^<\/?[a-zA-Z][a-zA-Z0-9]*(\s+[a-zA-Z_:][a-zA-Z0-9_\-:.]*="[^"]*")*\s*\/?>(\n)?$` |
| **Email**        | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`                                |
| **URL**          | `^https?://([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(/[\S]*)?(\?[\S]*)?$`             |

> You can add additional patterns (e.g., hashtags, time, credit card numbers) by following the current structure.

---

## 📂 File Structure

```bash
alu_regex-data-extraction-{yourusername}/
├── main.py
├── emails.txt
├── phones.txt
├── currency.txt
├── htmltags.txt
├── urls.txt
└── README.md
```

---

## 🧪 How to Use

1. **Clone the repository**

```bash
git clone https://github.com/{yourusername}/alu_regex-data-extraction-gilbmura.git
cd alu_regex-data-extraction-gilbmura
```

2. **Run the script**

```bash
python main.py
```

3. **Choose from the menu** to validate:

* Currency
* Phone numbers
* HTML tags
* Emails
* URLs

---

## 📘 Example Input/Output

Example from `phones.txt`:

```
123-456-7890
(123) 456-7890
1234567890
```

Expected Output:

```
Line 1: '123-456-7890' ---- Valid
Line 2: '(123) 456-7890' ---- Valid
Line 3: '1234567890' ---- Invalid
```

---

## 🧹 Future Improvements

* Add support for hashtags, credit card numbers, and time formats
* Export valid entries to separate output files
* Add GUI interface

---

## 👨‍💻 Author

Built with ❤️ by **Gilbert** during the ALU Regex Hackathon 2025.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy Hacking! 💻
