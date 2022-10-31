#!/usr/bin/python

import sys


commit_regex = r"^(build|feat|fix|refactor|test|chore|docs|ci){1}(:) ([\w ])+([\s\S])"


def prepare_commit_msg():
    print("\nCommit message example:")
    print("     feat(api)!: new endpoint to search")
    print("     refactor(api): renamed endpoint")
    print("     docs: updated documentation")
    print(f"Follow regex: {commit_regex}.\n")
    sys.exit(0)


if __name__ == "__main__":
    print("\n------PREPARE-COMMIT-MSG------")
    prepare_commit_msg()
