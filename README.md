# watodo-sync
A script to sync watodos with cloud via aws s3 service. So, not need of copying `watodo.json` in different systems. [Watodo](https://github.com/FlareXes/watodo) the original project is a minimal todo script with **No Garbage - Which Suckless**

> **Note:** This Project Is Still Under Development. So, Use Your Coder Mind To Make It Work.

### Why a different repository for sync?
Because, It's a bloat okay!, Yaa it's a bloat. Original project [watodo](https://github.com/FlareXes/watodo) suppose to be suckless. And, It will never change. And, One real reason, It's not the best way to do that. But, I'll think about this in future.

# Usage
Print help
```bash
watodo-sync help
```

Push current todos to cloud
```bash
watodo-sync push
```

Fetch todos from cloud and merge with existing todos
```bash
watodo-sync pull
```

# Installation
```bash
git clone https://github.com/FlareXes/watodo-sync.git && cd watodo-sync

chmod +x setup

./setup
```

# Uninstall
```bash
sudo rm -rf /opt/watodo-sync /usr/local/bin/watodo-sync
```

# License
This work is shared by [FlareXes](https://github.com/FlareXes) under the terms of [MIT License](LICENSE).
