import subprocess

def get_wifi_passwords():
    # Run the command to get all Wi-Fi profiles
    command = ['netsh', 'wlan', 'show', 'profiles']
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Extract Wi-Fi profile names
    profiles = []
    for line in result.stdout.splitlines():
        if "All User Profile" in line:
            # Get the Wi-Fi profile name
            profile = line.split(":")[1].strip()
            profiles.append(profile)
    
    # Extract passwords for each profile
    wifi_details = []
    for profile in profiles:
        # Run the command to get details of each profile
        command = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
        result = subprocess.run(command, capture_output=True, text=True)
        
        password = None
        for line in result.stdout.splitlines():
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break
        
        wifi_details.append({'SSID': profile, 'Password': password or 'No password saved'})
    
    return wifi_details

if __name__ == "__main__":
    wifi_data = get_wifi_passwords()
    for wifi in wifi_data:
        print(f"SSID: {wifi['SSID']}, Password: {wifi['Password']}")
