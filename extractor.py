import re
import os

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

def ensure_output_folder():
    os.makedirs("output", exist_ok=True)

def process_file(file_path, validator, label):
    ensure_output_folder()
    
    valid_output = f"output/extracted_{label.replace(' ', '_')}.txt"
    invalid_output = f"output/invalid_{label.replace(' ', '_')}.txt"

    valid_count = 0
    invalid_count = 0

    try:
        with open(file_path, 'r', encoding='utf-8') as infile, \
             open(valid_output, 'w', encoding='utf-8') as valid_file, \
             open(invalid_output, 'w', encoding='utf-8') as invalid_file:

            for line_num, line in enumerate(infile, 1):
                line = line.strip()
                if not line:
                    continue
                if validator(line):
                    valid_file.write(line + '\n')
                    print(f"Line {line_num}: ✅ '{line}'")
                    valid_count += 1
                else:
                    invalid_file.write(line + '\n')
                    print(f"Line {line_num}: ❌ '{line}'")
                    invalid_count += 1

        print(f"\n✅ Valid entries saved to: {valid_output} ({valid_count} entries)")
        print(f"❌ Invalid entries saved to: {invalid_output} ({invalid_count} entries)\n")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.\n")

def main():
    print("\t" * 2, "Welcome To The Regex Pattern Finder & Checker!\n")

    menu = [
        "Check Currency Amount From currency.txt",
        "Check Phone Number From phones.txt",
        "Check HTML Tag From htmltags.txt",
        "Check Email Address From emails.txt",
        "Check URL Address From urls.txt",
        "Close The Program"
    ]

    validators = [
        ("currency amount", check_currency),
        ("phone number", check_phone),
        ("HTML tag", check_html_tag),
        ("email address", check_email),
        ("URL address", check_url),
    ]

    file_paths = {
        "currency amount": "currency.txt",
        "phone number": "phones.txt",
        "HTML tag": "htmltags.txt",
        "email address": "emails.txt",
        "URL address": "urls.txt",
    }

    while True:
        for idx, item in enumerate(menu, 1):
            print(f"{idx}. {item}")
        print()

        try:
            choice = int(input("Please select an option from the menu (1-6): "))
        except ValueError:
            print("\n❌ Invalid input! Please enter a number between 1 and 6.\n")
            continue

        if 1 <= choice <= 5:
            label, validator = validators[choice - 1]
            file_path = file_paths[label]
            process_file(file_path, validator, label)
        elif choice == 6:
            print("Thank you for using the Regex Pattern Finder & Checker and Trusting Our Team.")
            break
        else:
            print("\n❌ Invalid choice! Please select a number between 1 and 6.\n")

if __name__ == '__main__':
    main()
