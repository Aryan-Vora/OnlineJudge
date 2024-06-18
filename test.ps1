# Run the python script with input.txt and redirect the output to a temporary file
Get-Content input.txt | python main.py > temp.txt

# Compare the temporary file with output.txt
$diff = Compare-Object (Get-Content temp.txt) (Get-Content output.txt)

# If there is a difference print
if ($diff -eq $null)
{
    Write-Host "Test Passed"
}
else
{
    Write-Host "Test Failed"
    Write-Host "Differences:"
    $diff | Format-Table
}

# Remove the temporary file
Remove-Item temp.txt
