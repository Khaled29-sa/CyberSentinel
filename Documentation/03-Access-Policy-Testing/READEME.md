# 03 – Access Policy Testing

## Objective

Verify that department-based web access policies are enforced correctly through the Squid Proxy by testing permitted and blocked websites for IT, HR, and Finance employees.

## Implementation

### 1. IT Department – Ahmed

The IT employee was configured to use the dedicated proxy port `3129`.

![IT Proxy Configuration](images/IT/Ahmed_01_Proxy_Configuration.png)

**Access Policy Tests:**

- GitHub: Allowed.
- TradingView: Blocked.

The browser tests confirmed the expected access behavior.

![GitHub Allowed](images/IT/Ahmed_03_Allowed_GitHub.png)

![TradingView Blocked](images/IT/Ahmed_04_Blocked_TradingView.png)

Splunk logs confirmed the results through `TCP_TUNNEL/200` for GitHub and `TCP_DENIED/403` for TradingView.

![IT Splunk Verification](images/IT/Ahmed_05_Splunk_Allowed_vs_Blocked.png)

### 2. HR Department – Sara

The HR employee was configured to use the dedicated proxy port `3130`.

![HR Proxy Configuration](images/HR/Sara_03_Proxy_Configuration.png)

**Access Policy Tests:**

- LinkedIn: Allowed.
- GitHub: Blocked.

The browser tests confirmed the expected access behavior.

![LinkedIn Allowed](images/HR/Sara_01_Allowed_LinkedIn.png)

![GitHub Blocked](images/HR/Sara_02_Blocked_GitHub.png)

Splunk logs confirmed the results through `TCP_TUNNEL/200` for LinkedIn and `TCP_DENIED/403` for GitHub.

![HR Splunk Verification](images/HR/Sara_04_Splunk_Allowed_vs_Blocked.png)

### 3. Finance Department – Faisal

The Finance employee was configured to use the dedicated proxy port `3131`.

![Finance Proxy Configuration](images/Finance/Faisal_01_Proxy_Configuration.png)

**Access Policy Tests:**

- TradingView: Allowed.
- GitHub: Blocked.

The browser tests confirmed the expected access behavior.

![TradingView Allowed](images/Finance/Faisal_03_Allowed_TradingView.png)

![GitHub Blocked](images/Finance/Faisal_04_Blocked_GitHub.png)

Splunk logs confirmed the results through `TCP_TUNNEL/200` for TradingView and `TCP_DENIED/403` for GitHub.

![Finance Splunk Verification](images/Finance/Faisal_05_Splunk_Allowed_vs_Blocked.png)

## Outcome

All six access policy tests produced the expected results across the three departments.

The browser tests and Splunk access logs verified that permitted connections were established and restricted requests were denied according to the configured department policies.
