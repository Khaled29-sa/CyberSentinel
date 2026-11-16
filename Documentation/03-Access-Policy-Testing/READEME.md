# 03 – Access Policy Testing

## Objective

Verify that department-based web access policies are enforced correctly through the Squid Proxy by testing permitted and blocked websites for IT, HR, and Finance employees.

## Implementation

### 1. Department Website Policies

Department-specific website access lists were configured to define which websites are allowed and blocked for each department.

The following image shows the allowed and blocked website lists configured for IT, HR, and Finance.

![Department Website Policies](images/Department_Website_Policies.png)

**IT Department**
- **Allowed:** GitHub, Stack Overflow, LinkedIn, Microsoft.
- **Blocked:** TradingView, Investing, Indeed, Bayt.

**HR Department**
- **Allowed:** Microsoft, LinkedIn, Indeed, Bayt.
- **Blocked:** GitHub, Stack Overflow, TradingView, Investing.

**Finance Department**
- **Allowed:** TradingView, Investing, Microsoft.
- **Blocked:** GitHub, Stack Overflow, LinkedIn, Indeed, Bayt.

### 2. IT Department – Ahmed

The IT employee was configured to use the dedicated proxy port `3129`.

**Access Policy Tests:**

- GitHub: Allowed.
- TradingView: Blocked.

The browser tests confirmed the expected access behavior.

![GitHub Allowed](images/IT/Ahmed_03_Allowed_GitHub.png)

![TradingView Blocked](images/IT/Ahmed_04_Blocked_TradingView.png)

Splunk logs confirmed the results through `TCP_TUNNEL/200` for GitHub and `TCP_DENIED/403` for TradingView.

![IT Splunk Verification](images/IT/Ahmed_05_Splunk_Allowed_vs_Blocked.png)

### 3. HR Department – Sara

The HR employee was configured to use the dedicated proxy port `3130`.

**Access Policy Tests:**

- LinkedIn: Allowed.
- GitHub: Blocked.

The browser tests confirmed the expected access behavior.

![LinkedIn Allowed](images/HR/Sara_01_Allowed_LinkedIn.png)

![GitHub Blocked](images/HR/Sara_02_Blocked_GitHub.png)

Splunk logs confirmed the results through `TCP_TUNNEL/200` for LinkedIn and `TCP_DENIED/403` for GitHub.

![HR Splunk Verification](images/HR/Sara_04_Splunk_Allowed_vs_Blocked.png)

### 4. Finance Department – Faisal

The Finance employee was configured to use the dedicated proxy port `3131`.

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
