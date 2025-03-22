# Nocturne v1 - Discord Webhook Spammer

## Overview
Nocturne v1 is a powerful and efficient Discord webhook spammer designed for testing and automation purposes. This tool allows users to send bulk messages to Discord webhooks effortlessly, making it useful for stress-testing webhooks, automated notifications, or other experimental applications.

**Disclaimer:** This tool is for educational and testing purposes only. Misuse of this tool to spam or disrupt services violates Discord's Terms of Service and may result in account suspension or legal consequences. Use responsibly and with permission.

---

## Features
- **Fast & Efficient** – Sends messages rapidly to Discord webhooks.
- **Customizable Message Content** – Allows users to configure the message text.
- **Multi-threading Support** – Enables high-speed message delivery with multiple threads.
- **Proxy Support** – Option to use proxies for anonymous requests.
- **Rate Limit Handling** – Includes basic mechanisms to manage Discord rate limits.
- **User-Friendly Interface** – Simple and easy-to-use command-line interface.

---

## Installation & Setup
### Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- `requests` module
- `threading` module (included in Python standard library)

### Step-by-Step Guide
#### 1. Download & Setup
1. Download the repository folder from GitHub.
2. Ensure Python is installed and added to the system PATH.

#### 2. Install Dependencies
1. Open the `install_requirements` file.
2. Wait until all dependencies are installed.
3. Once done, close the file.

#### 3. Run the Tool
1. Open `spammer.py` to start the script.

---

## Usage
### Running the Spammer
1. Open `spammer.py`.
2. You will see the UI; if you like it, consider making a pull request and providing feedback. We answer every issue submitted!
3. Enter your Discord webhook URL.
4. Enter a custom name for the webhook (optional). If the webhook name is currently "test," you can rename it to "Nocturne."
5. Enter the message you want to spam.
6. Enter the delay between messages (in seconds).
7. Enter the number of messages to be sent.
8. Choose whether to delete the webhook after completion. If you enter 'Y' (yes), the webhook will be automatically deleted once the specified number of messages has been sent.

### Additional Controls
- Soon, Nocturne will release plenty of multi-tools. Consider giving us ideas or suggestions for future features! 

## Legal & Ethical Use
Nocturne v1 is intended strictly for:
- Testing webhook functionality.
- Educational purposes related to API security and stress testing.
- Personal automation projects with webhooks.

Do **not** use this tool to spam, harass, or abuse services. Unauthorized use is a violation of Discord's policies and could lead to account bans or legal action.

---

## Support & Contributions
If you encounter issues or have suggestions for improvements, feel free to create an issue or submit a pull request.
Enjoy using Nocturne v1.
