import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("fileInput", nargs="?", default="./data.json")
parser.add_argument("fileOutput", nargs="?", default="./output.txt")
args = parser.parse_args()

with open((args.fileInput), encoding="utf-8") as file:
    # Adds extracted URLs to url_list
    def tabs_from_window(json_window):
        for tab_counter in range(0, len(json_window["tabs"])):
            # ["entries"][0] due to json structure
            url_list.append(json_window["tabs"][tab_counter]["entries"][0]["url"])

    def append_text_to_file(file_path, _url_list):
        try:
            with open(file_path, "a") as file:
                for url in _url_list:
                    file.write(url + "\n")
            print(f"Text appended to {file_path} successfully.")
        except Exception as e:
            print(f"Error: {e}")

    # Loads json object
    decoded_json_object = json.load(file)

    # Preps an list to add urls to
    url_list = []

    # Loops each indiviual window to extract tab URLs
    for window_counter in range(0, len(decoded_json_object["windows"])):
        tabs_from_window(decoded_json_object["windows"][window_counter])

    append_text_to_file((args.fileOutput), url_list)
