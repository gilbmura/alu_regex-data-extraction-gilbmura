import re

def check_currency(text):
    pattern = re.compile(r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$|^\$\d+(\.\d{2})?$')
    return bool(pattern.fullmatch(text.strip()))

def check_phone(text):
    pattern = re.compile(
        r'^(\+?\d{1,2}\s?)?(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}$'
    )
    return bool(pattern.fullmatch(text.strip()))

def check_html_tag(text):
    pattern = re.compile(
        r'^<\/?[a-zA-Z][a-zA-Z0-9]*(\s+[a-zA-Z_:][a-zA-Z0-9_\-:.]*="[^"]*")*\s*\/?>$'
    )
    return bool(pattern.fullmatch(text.strip()))

def check_url(text):
    pattern = re.compile(
        r'^https?://([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(:\d+)?(/[^\s]*)?(\?[^\s]*)?$'
    )
    return bool(pattern.fullmatch(text.strip()))

def check_email(text):
    pattern = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    return bool(pattern.fullmatch(text.strip()))

def process_file(file_path, validator, label):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                is_valid = validator(line)
                print(f"Line {line_num}: '{line}' ---- {'Valid' if is_valid else 'Invalid'}")
    except FileNotFoundError:
        print("File not found. Please check the path.\n")

def main():
    print("\t" * 2, "Welcome To The Regex Pattern Finder & Checker!\n")

    menu = [
        "check Currency Amount From currency.txt",
        "check Phone Number From phones.txt",
        "check HTML Tag From htmltags.txt",
        "check Email Address From emails.txt",
        "check URL Address From urls.txt",
        "Close The Program"
    ]

    validators = [
        ("currency amount", check_currency),
        ("phone number", check_phone),
        ("HTML tag", check_html_tag),
        ("email address", check_email),
        ("URL address", check_url),
    ]

    # Define your file paths here
    file_paths = {
        "currency amount": "currency.txt",
        "phone number": "phones.txt",
        "HTML tag": "tags.txt",
        "email address": "emails.txt",
        "URL address": "search.txt",
    }

    while True:
        for idx, item in enumerate(menu, 1):
            print(f"{idx}. {item}")
        print()
        try:
            choice = int(input("Please select an option from the above menu(1-6): "))
        except ValueError:
            print("\nInvalid input! Please enter a number between 1 and 6.\n")
            continue

        if 1 <= choice <= 5:
            label, validator = validators[choice - 1]
            file_path = file_paths[label]
            process_file(file_path, validator, label)
        elif choice == 6:
            print("Thank you for Trusting our Team...")
            break
        else:
            print("\nInvalid choice! Please select a number between 1 and 6.\n")

if __name__ == '__main__':
    main()