# netpyma
Network Management and Automation with Python 🚀

This package converts YAML configuration file of a network to a cisco device ios command file.

## ⚡ Quick Start

1. Cloning the project

```sh
git clone https://github.com/bmict/netpyma.git
```

1. Install .venv in the project folder

```sh
python -m venv .venv
```

2. Install requirements

```sh
pip install -r requirements.txt
```

3. To test converting a YAML file to ios config file for test01 exam file, only run below command.

```sh
py main.py tests/test01
```

## 🖥️ Documentation

### Command

`py main.py` **`<test-folder>`** *`[options]`*

#### Options

1. **-V** verbose, print config json
2. **-a** apply, send config commands to devices

The output files are saved in dist folder inside the sample test folder.

<br />

---
Mojtaba Soltani
