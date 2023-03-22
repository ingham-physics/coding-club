"""Some examples of Context Managers in Python
"""


class MyFileContextManager:
    def __init__(self, file_path):
        self.file_path = file_path

        self.file_handle = None

    def __enter__(self):
        print("Entering the context...")

        self.file_handle = open(self.file_path, "w", encoding="utf8")
        return self.file_handle

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print("Closing the file")
        self.file_handle.close()


def write_to_file():

    print("Writing to hello.txt")

    file = open("hello.txt", "w", encoding="utf8")

    try:
        for i in range(10, -1, -1):
            file.write(f"Hello, World! {1/i}\n")
    except Exception as exception:
        print(exception)
    finally:
        file.close()
        print("File Closed")

    # with MyFileContextManager("hello.txt") as my_file:
    #     for i in range(10, 0, -1):
    #         my_file.write(f"Hello, World! {1/i}\n")

    with open("hello.txt", "w", encoding="utf8") as file:
        for i in range(10, -1, -1):
            file.write(f"Hello, World! {1/i}\n")


if __name__ == "__main__":

    write_to_file()


def insert_attribute_to_dataset(dataset, attributes={}):

    for k, v in attributes.items():

        try:
            dataset[k] = v
            # ...
        except AttributeError:
            print("Attribute not in DICOM dataset")
        except ValueError:
            print("handle")
        except Exception:  # pylint: disable=broad-exception-caught
            print("everything")
