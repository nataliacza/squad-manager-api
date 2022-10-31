#!/usr/bin/python

import sys
import re
import subprocess


branch_regex = r"^(build|feat|fix|refactor|test|chore|docs|ci){1}(:) ([\w ])+([\s\S])"


def get_current_branch() -> str:
    branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("ascii").strip()
    return branch_name


def pre_commit_hook():
    if re.search(branch_regex, get_current_branch()):
        print("\n[INFO] Branch name validated!\n")
        sys.exit(0)
    else:
        print(f"\n[ERROR] Invalid branch name. Follow regex: {branch_regex}.\n")
        sys.exit(1)


if __name__ == "__main__":
    print("\n----------PRE-COMMIT----------")
    pre_commit_hook()
