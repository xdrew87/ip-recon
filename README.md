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

**FOR AUTHORIZED USE ONLY**

This tool is intended exclusively for:

- Testing your own infrastructure
- Authorized penetration testing with written permission
- Educational and research purposes in controlled environments

Unauthorized use against systems you don't own is illegal and may result in criminal prosecution. The developers assume no responsibility for misuse of this software.

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
git clone https://github.com/xdrew87/zzzz.git
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

![example](https://raw.githubusercontent.com/xdrew87/suicixdalEXE/main/zzzz/example.png)

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
