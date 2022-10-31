#!/usr/bin/python

import sys
import re


commit_regex = r"^(build|feat|fix|refactor|test|chore|docs|ci){1}(:) ([\w\W\s\S]+)$"


def get_commit_message() -> str:
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, "r+") as file:
        commit_msg = file.read()
        return commit_msg


def commit_msg_hook():
    if re.search(commit_regex, get_commit_message()):
        print("[INFO] Good commit message!")
        sys.exit(0)
    else:
        print(f"[ERROR] Bad commit message! Follow regex: {commit_regex}")
        sys.exit(1)


if __name__ == "__main__":
    print("\n----------COMMIT-MSG----------")
    commit_msg_hook()
    print("------------------------------\n")
