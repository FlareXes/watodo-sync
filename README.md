# watodo-sync
A script to sync watodos with cloud via aws s3 service. So, not need of copying `watodo.json` in different systems. [Watodo](https://github.com/FlareXes/watodo) the original project is a minimal todo script with **No Garbage - Which Suckless**

### Why a different repository for sync?
Because, It's a bloat okay!, Yaa it's a bloat. Original project [watodo](https://github.com/FlareXes/watodo) suppose to be suckless. And, It will never change. And, One real reason, It requires little bit of hustle.

# Usage
Print help
```
watodo-sync help
```

Push current todos to cloud
```
watodo-sync push
```

Fetch todos from cloud and merge with existing todos
```
watodo-sync pull
```

# Prerequisite
1. [Aws Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

2. Access to any cloud service provider that has **s3 support**. [`Storj`](https://www.storj.io/) could a good option for free. Check out [How to setup storj?](https://flarexes.com/a-fast-secure-cloud-storage-sync-for-linux) for more info.

3. Create a bucket named `watodo-bucket` because thats where `watodo.json` will going to be stored.

> **Warning:** If you're using any other `s3` provider than aws, then you have to change `endpoint = "aws s3"` variable to `endpoint = "aws s3 --endpoint-url=<your s3 provider endpoint>"` because by default `aws` cli will point to `aws s3` endpoints.
> The `endpoint` variable exists in `watodo-sync.py` file at two places so you have to change both of them.
> Example: For storj, endpoint variable would be `endpoint = "aws s3 --endpoint-url=https://gateway.storjshare.io"`




# Installation
**Linux / MacOS**
```bash
git clone https://github.com/FlareXes/watodo-sync.git && cd watodo-sync

chmod +x setup

./setup
```

**Windows**

Download `watodo-sync.py`. Then use it manually `python watodo-sync.py`.

# Uninstall
**Linux / MacOS**
```bash
sudo rm -rf /opt/watodo-sync /usr/local/bin/watodo-sync
```

**Windows**

Just delete `watodo-sync.py`

# License
This work is shared by [FlareXes](https://github.com/FlareXes) under the terms of [MIT License](LICENSE).
