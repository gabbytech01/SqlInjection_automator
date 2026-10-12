# SqlInjection_automator
Get sqlinjection the faster way

How to Use the Script

    Make sure sqlmap is installed and updated:
    Bash

    sudo apt update && sudo apt install sqlmap

    Run against a GET-based vulnerable parameter:
    Bash

    python3 run_sqlmap.py "http://127.0.0.1/vulnerable.php?id=1"

    Run against a POST-based form parameter:
    Bash

    python3 run_sqlmap.py "http://127.0.0.1/login.php" "username=test&password=test"

Key Flags Explained

    --batch: Prevents sqlmap from pausing to ask default questions, automatically choosing safe options.

    --random-agent: Uses a randomized HTTP User-Agent header to mimic standard browser traffic.

    --risk 1 / --level 1: Keeps tests conservative and fast, avoiding heavy or potentially disruptive payloads against your local test app.
