import re

def find_hidden_messages(file_path):
    pattern = re.compile(r'[a-zA-Z]{5,}!')
    found_messages = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                matches = pattern.findall(line)
                found_messages.extend(matches)
    except FileNotFoundError:
        print("File not found.")
        return None

    return found_messages

if __name__ == '__main__':
    file_path = '/Users/louyhaib/Desktop/Notebooks_content_week05_resources at main · PythonFreeCourse_Notebooks.html'
    hidden_messages = find_hidden_messages(file_path)
    if hidden_messages:
        print("Hidden messages found:")
        for msg in hidden_messages:
            print(msg)
    else:
        print("No hidden messages found.")

