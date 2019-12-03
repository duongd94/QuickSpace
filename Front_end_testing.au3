#region --- Au3Recorder generated code Start (v3.3.9.5 KeyboardLayout=00000409)  ---

#region --- Internal functions Au3Recorder Start ---
Func _Au3RecordSetup()
Opt('WinWaitDelay',100)
Opt('WinDetectHiddenText',1)
Opt('MouseCoordMode',0)
Local $aResult = DllCall('User32.dll', 'int', 'GetKeyboardLayoutNameW', 'wstr', '')
If $aResult[1] <> '00000409' Then
  MsgBox(64, 'Warning', 'Recording has been done under a different Keyboard layout' & @CRLF & '(00000409->' & $aResult[1] & ')')
EndIf

EndFunc

Func _WinWaitActivate($title,$text,$timeout=0)
	WinWait($title,$text,$timeout)
	If Not WinActive($title,$text) Then WinActivate($title,$text)
	WinWaitActive($title,$text,$timeout)
EndFunc

_AU3RecordSetup()
#endregion --- Internal functions Au3Recorder End ---


Run('C:\Windows\System32\cmd.exe')
_WinWaitActivate("C:\Windows\System32\cmd.exe","")
Send("D:{ENTER}chdir Projects/QuickSpace/{ENTER}python combined_gui1.py{ENTER}")
_WinWaitActivate("Quick-Space","")
# Continue
MouseClick("left",230,457,1)

# Click on Warehouse Name
MouseClick("left",220,239,1)
#input Warehouse name
Send("Front-End Test{TAB}")
# input length then tab to input width
Send("3000{TAB}7000")
# click ok
MouseClick("left",230,533,1)
#click add item
MouseClick("left",236,254,1)
#click on item name
MouseClick("left",236,254,1)
#input item name then tab to length then width
Send("Paper{TAB}567{TAB}987")
#click add
MouseClick("left",256,510,1)
#click yes to add another
MouseClick("left",178,398,1)
#triple click inputbox to delete it all
MouseClick("left",287,251,1)
MouseClick("left",287,251,1)
MouseClick("left",287,251,1)
#input item name then tab to
Send("{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}{BACKSPACE}Stapler{TAB}111{TAB}222")
# add item
MouseClick("left",256,522,1)
# dont add another item
MouseClick("left",326,403,1)
# view warehouse
MouseClick("left",281,359,1)
MouseMove(76,540)
MouseDown("left")
MouseMove(44,542)
MouseUp("left")
# ok to back out
MouseClick("left",242,640,1)
# load another warehouse
MouseClick("left",266,514,1)
# click dropdown
MouseClick("left",253,441,1)
# click Main Warehouse
MouseClick("left",242,488,1)
#click ok
MouseClick("left",236,530,1)
# Click view warehouse
MouseClick("left",233,362,1)
#endregion --- Au3Recorder generated code End ---
