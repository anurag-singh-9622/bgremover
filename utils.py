def fetch_readme():
    try:
        with open('README.md', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "README.md file not found."
    except Exception as e:
        return f"An error occurred: {e}"