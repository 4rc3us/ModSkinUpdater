$sourceFileLocation = "$Home\modskin\"

$sourceFileLocation += Get-ChildItem $sourceFileLocation -Filter *.exe -Name

Write-Host $sourceFileLocation

$ShortcutLocation = "$Home\Documents\+\ModSkin.lnk"

$WScriptShell = New-Object -ComObject WScript.Shell

$Shortcut = $WScriptShell.CreateShortcut($ShortcutLocation)
 
$Shortcut.TargetPath = $SourceFileLocation
 
$Shortcut.Save()

Write-Host 'Shortcut created'