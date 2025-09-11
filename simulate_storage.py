class InMemoryFileStorage:
    def __init__(self):
        self.storage = {}  # Dictionary to hold {file_path: content}

    def upload_file(self, path, content):
        self.storage[path] = content
        return f"File '{path}' uploaded successfully."

    def read_file(self, path):
        if path in self.storage:
            return self.storage[path]
        return f"Error: File '{path}' not found."

    def delete_file(self, path):
        if path in self.storage:
            del self.storage[path]
            return f"File '{path}' deleted successfully."
        return f"Error: File '{path}' not found."

    def list_files(self):
        return list(self.storage.keys())


if __name__ == "__main__":
    storage = InMemoryFileStorage()

    # Upload
    print(storage.upload_file("images/logo.png", "BinaryDataOfLogo..."))
    print(storage.upload_file("docs/readme.txt", "This is the README file."))

    # List files
    print("Files in storage:", storage.list_files())

    # Read
    print("Reading docs/readme.txt:", storage.read_file("docs/readme.txt"))

    # Delete
    print(storage.delete_file("images/logo.png"))
    print("Files after delete:", storage.list_files())

    # Try to read deleted file
    print(storage.read_file("images/logo.png"))
