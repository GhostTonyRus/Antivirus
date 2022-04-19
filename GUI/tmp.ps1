$driveEject = New-Object -comObject Shell.Application
$driveEject.Namespace(17).ParseName("F:").InvokeVerb("Eject")