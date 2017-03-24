import argparse
import os
import sys
from github import Github


def get_token():
    home = os.path.expanduser("~")
    token_path = os.path.join(home, '.githubtoken')
    with open(token_path) as token_fd:
        return token_fd.read().strip()


def listprs(options):
    token = get_token()
    g = Github(token)
    repo = g.get_repo(options.repo)
    for pr in repo.get_pulls('open'):
        print pr.number

    return 0


def main():
    parser = argparse.ArgumentParser(description='GitHub tools')
    subparsers = parser.add_subparsers()

    listprs_parser = subparsers.add_parser('listprs', help='List PRs')
    listprs_parser.add_argument('repo')
    listprs_parser.set_defaults(func=listprs)

    options = parser.parse_args()

    sys.exit(options.func(options))
