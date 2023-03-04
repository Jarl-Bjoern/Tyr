<h1 align="center">💀 TYR 💀</h1>
<p align="center"></p>
<div align="center">
  <a href="https://www.kali.org/">
    <img alt="linux" src="https://img.shields.io/badge/%20-Linux-1f425f.svg?logo=linux&logoColor=cyan" />
  </a>
  <a href="https://www.microsoft.com/">
    <img alt="windows" src="https://img.shields.io/badge/%20-Windows-1f425f.svg?logo=windows&logoColor=cyan" />
  </a>
  <a href="https://www.python.org/downloads/release/python-3100/">
    <img alt="python" src="https://img.shields.io/badge/python-3.10-blue.svg?logo=python&logoColor=cyan" />
  </a>
  <a href="https://visitor-badge.glitch.me/badge?page_id=jarl-bjoern/tyr&left_color=grey&right_color=blue">
    <img alt="visitors" src="https://visitor-badge.glitch.me/badge?page_id=jarl-bjoern/tyr&left_color=grey&right_color=blue" />
  </a>
</div>
<div align="center">
  <a href="https://GitHub.com/jarl-bjoern/tyr/releases/">
    <img alt="repo size" src="https://img.shields.io/github/repo-size/jarl-bjoern/tyr?logo=github&logoColor=cyan" />
  </a>
  <a href="https://GitHub.com/jarl-bjoern/tyr/releases/">
    <img alt="releases" src="https://img.shields.io/github/downloads/jarl-bjoern/tyr/total?color=blue&logo=github&logoColor=cyan" />
  </a>
  <a href="https://github.com/jarl-bjoern">
      <img title="Follower" src="https://img.shields.io/github/followers/jarl-bjoern?color=blue&label=follow&logo=github&logoColor=cyan&style=flat-square">
  </a>
</div>
<div align="center">
  <a href="https://www.python.org/">
    <img alt="python" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg" />
  </a>
</div><br/>

TYR offers the possibility to load URLs into your standard browser in a relatively fast way, so that you can check them manually. This is very suitable for example if you get 1000 endpoints by fuzzing and cannot copy them manually due to lack of time.

It is best suited if you unite your browser with the BURP proxy, so you can track the called pages directly.<br />

# 📖 Table of Contents
- [How to download and install the tool](#download_install)
  - [Download and start the tool](#start_install)
  - [Using the help section to see which parameters do we have](#help_install)
      
<a name="download_install"></a>
# ⚔ How to download and install the tool
<a name="start_install"></a>
## ⚔ Download and start the tool
```bash
sudo git clone https://github.com/Jarl-Bjoern/Tyr/
cd Tyr
sudo python3 TYR.py
```

<a name="help_install"></a>
## ⚔ Using the help section to see which parameter do we have
```python
-------------------------------------------------------------------------------------
|  Created by Rainer Christian Bjoern Herold                                        |
|  Copyright 2022-2023. All rights reserved.                                        |
|                                                                                   |
|  Please do not use the program for illegal activities.                            |
|                                                                                   |
|  If you got any problems don't hesitate to contact me so I can try to fix them.   |
-------------------------------------------------------------------------------------

required arguments:
  -iL IMPORT_LIST, --import-list IMPORT_LIST
                        This parameter specify your targetlist
 
                        Your list must look like in this example:
                          - http://192.168.2.1
                          - https://192.168.2.2:8443
                          - http://tomcat-test:8080
                          - http://tomcat-test:8080/manager

                        -----------------------------------------------------------

optional arguments:
  -t TIME, --time TIME  This parameter specify the seconds between the next tab
 
                        Default: 0.65 Seconds
 
                        -----------------------------------------------------------
  -mt MAX_TABS, --max-tabs MAX_TABS
                        This parameter specify the max open tabs
 
                        Default: 100
 
                        -----------------------------------------------------------
  -h, --help            Show this help message and exit.
 
                        -----------------------------------------------------------
```

<a name="live_demo">
## ⚔ TYR
<p align=center>
    <img src="https://github.com/Jarl-Bjoern/Jarl-Bjoern/blob/main/Screencasts/tyr_start.gif" width=700 height=500>
</p>

# ⚠️ Remark
It should be said that the scripts are still under development, but already allow an easier start to perform as a penetration tester or digital forensics, certain pre-settings.

