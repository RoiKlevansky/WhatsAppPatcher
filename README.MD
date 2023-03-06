# WhatsApp Patcher

WhatsApp patcher is a program that patches WhatsApp apk.


## Features
|            Feature             | Availability |
|:------------------------------:|:------------:|
|   Signature Verifier Bypass    |      ✔       |
|      Enable all AB tests       |      ✔       |
| Keep revoked for all messages  |      ✔       |
|     Disable read receipts      |      ✔       |
| Option to save view once media |      ✔       |


## Requirements
1. Python3
2. Java 8 or higher


## Installation

Clone the repository:

```bash
> git clone https://github.com/Schwartzblat/WhatsAppPatcher.git
```

Requirements installation:

```bash
> pip install -r requirements.txt
```


## Usage

Run the program with the following command:

```bash
> python -m whatsapp_patcher.main [-p /path/to/input.apk] [-o /path/to/output.apk]
```

Where:
- `-p` is the input apk path, it may point to a whatsapp apk or `latest` to download the latest version automatically.
- `-o` is the output apk path.

## Example

```bash
> python -m whatsapp_patcher.main -p latest -o patched.apk
```


## Contributing

If you want to add patches you can open an issue and I will implement it, or you can add patches yourself and open pull request.