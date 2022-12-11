import os
import sys 
import json

modified = []


def frequency(todos):
    freq = {}
    for item in todos:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    return freq


def merge_todos(cloud_todo_freq, local_todo_freq):
    for c_todo in cloud_todo_freq:
        if c_todo in local_todo_freq:
            local_todo_freq[c_todo] = abs(local_todo_freq[c_todo] - cloud_todo_freq[c_todo])
            modified.append(c_todo)
        else:
            local_todo_freq[c_todo] = 1

    return local_todo_freq


def remove_unmodified_todos(original_b_count, b_count):
    for item in original_b_count:
        if item in modified:
            continue

        original_b_item_value = original_b_count[item]

        if b_count[item] == original_b_item_value:
            b_count[item] -= original_b_item_value

    return b_count


def process(a, b):
    global modified
    modified = []
    
    cloud_todo_freq = frequency(a)
    local_todo_freq = frequency(b)
    c = frequency(b)

    merged_todos_freq = merge_todos(cloud_todo_freq, local_todo_freq)
    filtered_todos = remove_unmodified_todos(c, merged_todos_freq)

    return filtered_todos


def load_local_todos():
    user_path = os.path.expanduser("~")
    database = os.path.join(user_path, ".local", "share", "watodo", "watodo.json")
    
    with open(database, "r") as f:
        return json.load(f)


def load_cloud_todos():
    endpoint = "aws s3"
    operation = "cp s3://watodo-bucket/watodo.json /tmp/tmp-watodo.json"
    cmd = endpoint + " " + operation

    print("Fetching watodo.json from cloud...")
    exit_code  = os.system(cmd)

    if exit_code == 0:
        with open("/tmp/tmp-watodo.json", "r") as f:
            return json.load(f)

    print(f"\nError Occured: unable to pull todos from cloud, exit code: {exit_code}")
    sys.exit(exit_code)
    

def push_to_cloud():
    user_path = os.path.expanduser("~")
    database = os.path.join(user_path, ".local", "share", "watodo", "watodo.json")

    endpoint = "aws s3"
    operation = f"cp {database} s3://watodo-bucket/watodo.json"
    cmd = endpoint + " " + operation

    print("Pushing watodo.json to cloud...")
    exit_code  = os.system(cmd)

    if exit_code != 0:
        print(f"Error Occured: unable to push todos to cloud, exit code: {exit_code}")
        sys.exit(exit_code)


def dump_synced_todos(synced_todos):
    user_path = os.path.expanduser("~")
    database = os.path.join(user_path, ".local", "share", "watodo", "watodo.json")
    
    with open(database, "w") as watodo_json:
        json.dump(synced_todos, watodo_json, indent=4)


def sync_watodo():
    cloud_todos = load_cloud_todos()
    local_todos = load_local_todos()

    inprogress = [cloud_todos["in-progress"], local_todos["in-progress"]]
    completed = [cloud_todos["completed"], local_todos["completed"]]

    inprogress = process(inprogress[0], inprogress[1])
    completed = process(completed[0], completed[1])
    
    for todo, count in inprogress.items():
        for i in range(count):
            local_todos["in-progress"].append(todo)

    for todo, count in completed.items():
        for i in range(count):
            local_todos["completed"].append(todo)

    dump_synced_todos(local_todos)


def help_prompt():
    print("""
Supported Argument: push, pull, help
For example:

# To upload existing local todos to cloud
python watodo-sync.py push

# To fetch todos from cloud and merge with existing todos
python watodo-sync.py sync

# To show this message
python watodo-sync.py help
""")


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) != 2:
        help_prompt()
        sys.exit(2)

    if argv[1] == "sync":
        sync_watodo()
        print("\n>>> 💻 Local 💻 : Synced! Successfully <<<")
    
    elif argv[1] == "push":
        push_to_cloud()
        print("\n>>> ⛅ Cloud ⛅ : Pushed! Successfully <<<")

    elif argv[1] == "help":
        help_prompt()
    
    else:
        help_prompt()
        print(">>>  Invalid Argument!  <<<")
        sys.exit(2)

    sys.exit(0)

