# Define parameters
$vmNames = @("vm-loadtesting-westus-001", "vm-loadtesting-westus-002")
$adminUsername = "loadtestadmin"
$adminPassword = "h$PH92mUR@1DTLyj"
$newUsername = "pugazhendhi.r"
$newPassword = "Q)2T,CHn843@`PG_"
$groupName = "Remote Desktop Users"

foreach ($vmName in $vmNames) {
    Write-Host "Configuring $vmName..."

    # Create local user
    Invoke-Command -ComputerName $vmName -Credential (New-Object PSCredential -ArgumentList ($adminUsername, (ConvertTo-SecureString -AsPlainText -Force $adminPassword))) -ScriptBlock {
        net user $using:newUsername $using:newPassword /add
    }

    # Add user to group
    Invoke-Command -ComputerName $vmName -Credential (New-Object PSCredential -ArgumentList ($adminUsername, (ConvertTo-SecureString -AsPlainText -Force $adminPassword))) -ScriptBlock {
        net localgroup $using:groupName $using:newUsername /add
    }

    Write-Host "Configuration for $vmName completed."
}
