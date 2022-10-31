#!/usr/bin/python

import sys


__COMMIT_REGEX = r"^(build|feat|fix|refactor|test|chore|docs|ci){1}(:) ([\w\W\s\S]+)$"


def prepare_commit_msg():
    print("Commit message example:")
    print("     feat: add new model")
    print("     fix: update port number")
    print("     refactor: rewrite get endpoint")
    print("     test: add 5 unit tests")
    print("     chore: write README documentation")
    print(f"Follow regex: {__COMMIT_REGEX}.")
    sys.exit(0)


if __name__ == "__main__":
    print("\n------PREPARE-COMMIT-MSG------")
    prepare_commit_msg()
    print("------------------------------\n")
