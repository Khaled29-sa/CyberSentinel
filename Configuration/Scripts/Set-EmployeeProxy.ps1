$email = (whoami /upn).Trim().ToLower()

$policy = Invoke-RestMethod "http://192.168.50.1:5000/get-policy?email=$email"

$proxy = "192.168.50.1:$($policy.port)"

Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name ProxyEnable -Value 1
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings" -Name ProxyServer -Value $proxy

Write-Host "User: $email"
Write-Host "Department: $($policy.group)"
Write-Host "Proxy: $proxy"