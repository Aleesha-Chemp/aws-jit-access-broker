# AWS Just-In-Time (JIT) Access Broker

A Python-based Just-In-Time (JIT) credential broker that implements the Principle of Least Privilege by issuing short-lived, temporary AWS STS credentials for specific engineer tasks.

---

## 📌 Project Overview
Static, long-lived AWS IAM access keys stored on local machines create significant security risks. This broker removes permanent elevated standing privileges by dynamically assuming an IAM role via AWS Security Token Service (STS) and issuing short-lived session tokens.

- **Target Role:** `Target-S3Reader-Role`
- **Session Duration:** 15 minutes (900 seconds)
- **Session Identity Tag:** `JIT-{engineer_name}` (auditable in AWS CloudTrail)

---

## 🛠️ Architecture & Tech Stack
- **Language:** Python 3
- **AWS SDK:** Boto3 (`sts` client)
- **Shell Environment:** Windows PowerShell
- **Security Standard:** Principle of Least Privilege (PoLP) & Ephemeral Access

---

## 🚀 How It Works & Usage

### 1. Run the Broker Script
Request temporary scoped access from PowerShell:
```powershell
python jit_broker.py
