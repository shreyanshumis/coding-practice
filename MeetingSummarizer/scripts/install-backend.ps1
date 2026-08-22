$projectRoot = Split-Path -Parent $PSScriptRoot
$pythonPath = Join-Path $projectRoot '.venv\Scripts\python.exe'

if (-not (Test-Path -LiteralPath $pythonPath)) {
    python -m venv (Join-Path $projectRoot '.venv')
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

& $pythonPath -m pip install -r (Join-Path $projectRoot 'backend\requirements.txt')
exit $LASTEXITCODE
