import json
import sys
import os


def merge_dict_watodos(file1, file2):
    with open(file1, "r") as f:
        cf = json.load(f)

    with open(file2, "r") as f:
        lf = json.load(f)

    merge = {}
    merge["in-progress"] = list(set(cf["in-progress"] + lf["in-progress"]))
    merge["completed"] = cf["completed"] + lf["completed"]

    return merge


def get_cfile():
    endpoint = "aws s3"
    operation = "cp s3://heha/watodo.json /tmp/tmp-watodo.json"
    cmd = endpoint + " " + operation

    print("Fetching watodo.json from cloud...")
    exit_code = os.system(cmd)

    if exit_code == 0:
        file = "/tmp/tmp-watodo.json"
        return file

    print(f"\nError Occured: exit code: {exit_code}")
    sys.exit(1)


def get_lfile():
    file = os.path.join(os.path.expanduser("~"), ".local", "share", "watodo", "watodo.json")
    return file


def set_cfile():
    endpoint = "aws s3"
    operation = f"cp {get_lfile()} s3://heha/watodo.json"
    cmd = endpoint + " " + operation

    print("Pushing watodo.json to cloud...")
    exit_code = os.system(cmd)

    if exit_code != 0:
        print(f"\nMay Error Occured: exit code: {exit_code}")
        sys.exit(1)


def dump_json(todos):
    file = get_lfile()

    with open(file, "w") as f:
        json.dump(todos, f, indent=4)


def help_prompt():
    print("""
Supported Argument: push, pull, help

For example:
# To upload todos to cloud provider
python watodo-sync.py push

# To sync todos from cloud provider and merge with existing todos
python watodo-sync.py pull
    """)


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 2:
        help_prompt()
        sys.exit(1)

    if argv[1] == "pull":
        f1 = get_lfile()
        f2 = get_cfile()
        f3 = merge_dict_watodos(f1, f2)
        dump_json(f3)
        print("\n>>> 💻 Local 💻 : Synced! Successfully <<<")
    elif argv[1] == "push":
        set_cfile()
        print("\n>>> ⛅ Cloud ⛅ : Synced! Successfully <<<")
    elif argv[1] == "help":
        help_prompt()
    else:
        print("Invalid Argument!")
        sys.exit(2)

    sys.exit(0)

