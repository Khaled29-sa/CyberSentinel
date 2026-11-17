## Evidence & Analysis

### 1. Initial Log Review
**SOC_01_Initial_Log_Review.png**

Started by reviewing the incoming Squid Proxy logs in Splunk to verify that web traffic events were being collected and indexed successfully.

This provided the initial visibility needed to begin analyzing employee web activity.

### 2. Event Status Analysis
**SOC_02_Event_Status_Analysis.png**

After confirming successful log collection, the next step was to examine proxy event statuses and distinguish between permitted and denied web requests.

This helped establish how Squid Proxy handled employee traffic.

### 3. User Activity Overview
**SOC_03_User_Activity_Overview.png**

Analyzed web requests associated with individual employees to understand their browsing activity and identify how users interacted with the proxy.

### 4. Blocked Destinations Analysis
**SOC_04_Blocked_Destinations_Analysis.png**

Examined blocked web destinations to identify which websites were denied by the configured access policies.

### 5. User and Destination Analysis
**SOC_05_User_Destination_Analysis.png**

Correlated employee activity with requested destinations to understand which users attempted to access specific websites and how those requests were handled.

### 6. Access Policy Investigation
**SOC_06_Access_Policy_Investigation.png**

Investigated proxy events to examine access decisions and verify whether requests were handled according to the configured security policies.

### 7. Department Policy Validation
**SOC_07_Department_Policy_Validation.png**

Compared web access activity across IT, HR, and Finance to validate the differences in access behavior between departments.

### 8. Repeated Blocked Access Detection
**SOC_08_Repeated_Blocked_Access_Detection.png**

Finally, examined repeated blocked access attempts to identify recurring patterns that could require further security investigation.

This analysis provided a foundation for the next stage, where monitoring results would be presented through dashboards and security alerts.
