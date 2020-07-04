from helper_functions import get_jinja_environment, write_to_file, read_json_file
import json
import os

ROOT = "/mnt/c/cmpe/learning_for_fun/jinja"
TEMPLATES_FOLDER = ROOT + "/templates"
TEMPLATE = "test.jinja"
GENERATED_FILE = ROOT + "/generated/test.txt"
SOURCE_FILE = ROOT + "/source/friends.json"

def main():
    jinja_environment = get_jinja_environment(TEMPLATES_FOLDER)
    template = jinja_environment.get_template(TEMPLATE)
    content = read_json_file(SOURCE_FILE)
    print(content)
    render = template.render(test=content)
    write_to_file(render, GENERATED_FILE)
    


if __name__ == "__main__":
    main()