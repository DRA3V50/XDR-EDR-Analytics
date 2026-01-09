# PowerShell Encoded Command Detection

### Threat Overview
Attackers often use encoded PowerShell commands for stealth execution
and malware delivery.

### Detection Logic
- Detect `powershell.exe` processes with `-enc` in command line.
- Focus on unusual parent processes (e.g., Office apps, explorer.exe)

### False Positives
- Admin scripts
- Automation tools

### Mitigation/Tuning
- Whitelist known admin hosts
- Alert only if executed by non-privileged users
- Include parent process validation
