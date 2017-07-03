# Run langcheck on all language files
[CmdletBinding()]
param (
    [Parameter(Mandatory = $false)]
    [switch]$Rebuild = $false
)

$ErrorActionPreference = "Stop"

# Build langcheck
$langcheckPath = ".\langcheck\bin\Release\netcoreapp1.1\langcheck.dll"
if (-not (Test-Path -PathType Leaf $langcheckPath) -or $Rebuild)
{
    pushd ".\langcheck"
        dotnet restore -v m
        dotnet build -c Release
    popd
}

# Grab en-GB from main repository
$languagePath = ".\data\language"
$basePack     = "$languagePath\en-GB.txt"
if (-not (Test-Path -PathType Leaf $basePack))
{
    $url = "https://raw.githubusercontent.com/OpenRCT2/OpenRCT2/develop/data/language/en-GB.txt"
    Invoke-WebRequest $url -OutFile $basePack
}

$languageFiles = Get-ChildItem $languagePath
$result = $true

# Check en-GB for errors
dotnet $langcheckPath $basePack $translationPack
if ($LASTEXITCODE -ne 0)
{
    $result = $false
}

# Check all language files against en-GB
foreach ($languageFile in $languageFiles)
{
    if ($languageFile.Name -eq "en-GB.txt")
    {
        continue;
    }

    $translationPack = "$languagePath\$($languageFile.Name)"

    $sw = [Diagnostics.Stopwatch]::StartNew()
    dotnet $langcheckPath $basePack $translationPack | ForEach-Object {
        if ($env:APPVEYOR -and $_.StartsWith("  info: "))
        {
            $message = $($languageFile.BaseName) + ": " + $_.Substring(8)
            Add-AppveyorMessage $message
        }
        $_
    }
    $sw.Stop()
    $testDuration = $sw.ElapsedMilliseconds

    if ($LASTEXITCODE -ne 0)
    {
        if ($env:APPVEYOR)
        {
            $testName = $languageFile.Name
            Add-AppveyorTest $testName -Outcome Failed -Duration $testDuration
        }
        $result = $false
    }
    else
    {
        if ($env:APPVEYOR)
        {
            $testName = $languageFile.Name
            Add-AppveyorTest $testName -Outcome Passed -Duration $testDuration
        }
    }
}

# Exit code
if ($result)
{
    exit 0
}
else
{
    throw "Some languages contained errors or warnings."
}
