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
* 📂 Automatically creates an `output/` folder upon running
* 📄 Saves valid and invalid entries to separate files by data type
* 🧼 Clean and modular code
* 🔄 Handles multiple formats and edge cases
* 🖥️ CLI-based menu interface

---

## 🧠 Data Types Extracted

| Data Type        | Regex Pattern Used                                                            |
| ---------------- | ----------------------------------------------------------------------------- |
| **Currency**     | `^\$\d{1,3}(,\d{3})*(\.\d{2})?$` or `^\$\d+(\.\d{2})?$`                       |
| **Phone Number** | `^(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$`                    |
| **HTML Tag**     | `^<\/?[a-zA-Z][a-zA-Z0-9]*(\s+[a-zA-Z_:][a-zA-Z0-9_\-:.]*="[^"]*")*\s*\/? >$` |
| **Email**        | `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`                            |
| **URL**          | `^https?://([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(/[^\s]*)?(\?[^\s]*)?$`       |

> You can add additional patterns (e.g., hashtags, time, credit card numbers) by following the current structure.

---

## 📂 File Structure

```
alu_regex-data-extraction-{yourusername}/
├── README.md
├── RegexEplanation.txt
├── currency.txt
├── emails.txt
├── extractor.py
├── htmltags.txt
├── urls.txt
├── phones.txt
└── output/
    ├── extracted_email_address.txt
    ├── invalid_email_address.txt
    └── ... (similar for other types)
```

---

## ⚙️ How It Works

When you run the program (`extractor.py`), the following happens:

1. An `output/` directory is automatically created (if it doesn't already exist).
2. For each data type (e.g., email, phone, URL), it reads entries from the corresponding `.txt` file (like `emails.txt`).
3. It validates each entry using the appropriate regex.
4. **Valid entries** are saved to a file like `output/extracted_email_address.txt`.
5. **Invalid entries** are saved to a file like `output/invalid_email_address.txt`.

👉 All saved files will be inside the `output/` folder, clearly named by data type and validity.

---

## ✏️ Adding or Modifying Data

You can freely **edit, add, or remove** entries in the `.txt` input files (`emails.txt`, `phones.txt`, etc.) before running the program. The tool will read the current contents of each file and process them — there's no embedded or hardcoded data.

> 📌 Make sure your new entries are each on a separate line.

This gives you flexibility to test different types of input or reuse the tool for new data.

---

## 🙌 Final Notes

This tool is designed to be extendable, clear, and useful for validating large sets of structured data with regular expressions. Great for quick testing or integrating into larger text-processing workflows.

Feel free to fork and improve it! 

---

## 👤 Author

Created by **Gilbert**.

## 📚 License

This project is licensed under the **MIT License**.
