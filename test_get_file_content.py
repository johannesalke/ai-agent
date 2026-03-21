from functions.get_file_content import get_file_content



def test():
    result = get_file_content("calculator", "main.py")
    print("def main():")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("def _apply_operator(self, operators, values)")

    result = get_file_content("calculator", "/bin/cat")
    print("Error:")


if __name__ == "__main__":
    test()