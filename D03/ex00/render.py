import sys
import settings

def main():
    argc = len(sys.argv)
    if argc == 2 and sys.argv[1].endswith(".template"):
        try:
            with open(sys.argv[1], "r") as file:
                body = file.read()
        except FileNotFoundError:
            print("The file does not exist.")
            return

        for attr in dir(settings):
            if not callable(getattr(settings, attr)):
                placeholder = "{" + attr + "}"
                value = getattr(settings, attr)
                body = body.replace(placeholder, str(value))
                content = settings.html_content.format(content=body)
        try:
            with open(sys.argv[1].replace(".template", ".html"), "w") as html_file:
                html_file.write(content)
        except Exception as e:
            print(f"An error occurred: {e}")

        

if __name__ == '__main__':
    main()