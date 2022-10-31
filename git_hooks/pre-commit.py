#!/usr/bin/python

import sys
import re
import subprocess


branch_regex = r"^(feature|bugfix|hotfix){1}(\/)([a-z0-9-]+)$"


def get_current_branch() -> str:
    branch_name = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("ascii").strip()
    return branch_name


def pre_commit_hook():
    if re.search(branch_regex, get_current_branch()):
        print("[INFO] Branch name validated!")
        sys.exit(0)
    else:
        print(f"[ERROR] Invalid branch name. Follow regex: {branch_regex}.")
        print("Example branch name:")
        print("     feature/database-connection")
        print("     bugfix/docker-compose-port")
        print("     hotfix/user-model")
        sys.exit(1)


if __name__ == "__main__":
    print("\n----------PRE-COMMIT----------")
    pre_commit_hook()
    print("------------------------------\n")
