import subprocess
import sys

def run_sqlmap(target_url, data=None):
    # Build the sqlmap command with safe defaults (batch mode, random user-agent)
    cmd = ['sqlmap', '-u', target_url, '--batch', '--random-agent', '--risk', '1', '--level', '1']
    
    # If POST parameters are provided, append them
    if data:
        cmd.extend(['--data', data])
        
    print(f"[*] Starting automated sqlmap scan against: {target_url}")
    
    try:
        # Execute sqlmap and stream output in real-time
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()
            
        process.wait()
        print(f"\n[+] Scan finished with return code: {process.returncode}")
        
    except KeyboardInterrupt:
        print("\n[!] Scan aborted by user.")
        process.terminate()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_sqlmap.py '<target_url>' '<post_data_if_any>'")
        print("Example: python3 run_sqlmap.py 'http://127.0.0.1/vulnerable.php?id=1'")
        sys.exit(1)
        
    url = sys.argv[1]
    post_params = sys.argv[2] if len(sys.argv) > 2 else None
    
    run_sqlmap(url, post_params)
