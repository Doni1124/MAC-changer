# Python MAC Address Changer

A lightweight Python script that allows you to change or spoof the Media Access Control (MAC) address of any network interface on Linux systems using `ifconfig`.

## Overview

This tool automates the process of changing a network adapter's physical hardware address. It takes down the target network interface, assigns the specified MAC address, and brings the interface back up to establish connectivity with the new identity.

## Prerequisites

* **Operating System:** Linux / Unix-based system (requires the `net-tools` package for `ifconfig`).
* **Privileges:** Root / `sudo` administrative access (required to alter interface configurations).
* **Python Version:** Python 3.x

## Quick Start

1. sudo python3 MACchanger.py
