from helper_functions import get_jinja_environment, write_to_file
import json

ROOT = "/mnt/c/cmpe/jinja"
TEMPLATES_FOLDER = ROOT + "/templates"
TEMPLATE = "test.jinja"
GENERATED_FILE = ROOT + "/generated/test.txt"
SOURCE_FILE = ROOT + "/source/friends.json"



def main():
    # jinja_environment = get_jinja_environment(TEMPLATES_FOLDER)
    # template = jinja_environment.get_template(TEMPLATE)
    # render = template.render(test=friends)
    # write_to_file(render, GENERATED_FILE)
    with open(SOURCE_FILE, "r") as file:
        content = json.load(file)
        print(json.dumps(content, indent=4))


if __name__ == "__main__":
    main()