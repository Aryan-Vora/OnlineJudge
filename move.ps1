# Get the path of the directory where the script is located
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition

# Change directory to the script's location
Set-Location $scriptPath

# Get all PDF files in the current directory
$pdfFiles = Get-ChildItem -Path . -Filter *.pdf

foreach ($pdf in $pdfFiles) {
    # Extract the base name without the extension and keep only numbers
    $folderName = [System.IO.Path]::GetFileNameWithoutExtension($pdf.Name) -replace '\D', ''

    if (-not [string]::IsNullOrWhiteSpace($folderName)) {
        # Create a directory with the extracted name if it doesn't exist
        $folderPath = Join-Path -Path $scriptPath -ChildPath $folderName
        New-Item -ItemType Directory -Path $folderPath -Force | Out-Null

        # Move the PDF file to the created directory
        Move-Item -Path $pdf.FullName -Destination $folderPath

        # Create a main.py file in the directory
        $mainPyPath = Join-Path -Path $folderPath -ChildPath "main.py"
        New-Item -ItemType File -Path $mainPyPath -Force | Out-Null

        # Create an input.txt file in the directory
        $inputTxtPath = Join-Path -Path $folderPath -ChildPath "input.txt"
        New-Item -ItemType File -Path $inputTxtPath -Force | Out-Null
    }
}