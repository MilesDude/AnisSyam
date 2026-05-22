@echo off
powershell -Command "Get-ChildItem -Path 'D:\download\Wedding HTML\Songs' -Filter *.mp3 | ForEach-Object { 'Songs/' + $_.Name } | ConvertTo-Json | Set-Content -Path 'D:\download\Wedding HTML\playlist.json' -Encoding UTF8"
echo Done! playlist.json created.
pause