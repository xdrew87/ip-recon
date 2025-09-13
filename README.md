# 🟣 IP RECON

Cyberstyle IP Intelligence Tool  
by [xdrew87](https://github.com/xdrew87)

```
               _._
           __.{,_.}.__
        .-"           "-.
      .'  __.........__  '.
     /.-'`___.......___`'-.\ 
    /_.-'` /   \ /   \ `'-._\
    |     |   '/ \'   |     |
    |      '-'     '-'      |
    ;                       ;
    _\         ___         /_
   /  '.'-.__  ___  __.-'.'  \
 _/_    `'-..._____...-'`    _\_
/   \           .           /   \
\____)         .           (____/
    \___________.___________/
      \___________________/
     (_____________________)
         IP RECON
```

---

## 🚨 LEGAL DISCLAIMER

FOR AUTHORIZED USE ONLY

This IP Recon tool is intended strictly for:
	•	Testing your own IPs or networks
	•	Educational purposes, OSINT research, and learning cybersecurity
	•	Demonstrations in safe, public environments (e.g., public DNS like 8.8.8.8)

Do not use this tool against systems you do not own or have explicit permission to test. Misuse may be illegal and could lead to criminal prosecution. The developers are not responsible for unauthorized use.
---

## ✨ Features

- **IP Lookup:** Enter any IP address (`-i <ip>`)
- **Fetches:** Country, Region, City, ISP, Org, ASN
- **IP Type Detection:**  
  - **Static (Server):** Hosting/cloud providers (AWS, Azure, Google, OVH, DigitalOcean, Linode, Hetzner, Contabo, Vultr, Oracle, Alibaba, Rackspace, Dreamhost, GCP, Microsoft, etc.)
  - **Likely Dynamic:** Residential ISP
- **Visuals:** Colorful, modern table output with [Rich](https://github.com/Textualize/rich)
- **Banner:** ASCII art cyber banner at startup
- **Logging:** Optional `--log` flag saves results to `results.log`
- **No API Key Needed:** Works out of the box

---

## ⚡️ Quick Start

### Prerequisites

- Python 3.6 or higher

### Installation

Copy and paste these commands in your terminal:

```bash
git clone https://github.com/xdrew87/ip-recon.git
cd zzzz
pip install rich requests
```

---

## 🛠️ Usage

```bash
python3 ip_recon.py -i 1.1.1.1
python3 ip_recon.py -i 8.8.8.8 --log
```

- Use `-i <ip>` to specify the IP address.
- Add `--log` to save results to `results.log`.

---

## 📋 Example Output

![example] <img width="1897" height="879" alt="Screenshot 2025-09-13 174738" src="https://github.com/user-attachments/assets/47a28f4b-293d-4c88-98c8-186f4a2f4df3" />

---

## 💡 Why Use IP RECON?

- Instantly see where an IP is located and who owns it.
- Know if it's a server or a regular ISP.
- Share colorful results in screenshots.
- No API key needed, works out of the box.

---

## 🤝 Contributing

Contributions are welcome!  
Fork the repository, create a feature branch, commit your changes, and open a Pull Request.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.  
See the LICENSE file for details.

---

> "I'm not fat, I'm festively plump!"  
> — IP RECON Cyber Banner

---

**Made with ❤️ by [xdrew87](https://github.com/xdrew87)**
**Made with ❤️ by [xdrew87](https://github.com/xdrew87)**

