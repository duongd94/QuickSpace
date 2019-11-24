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

# opens cmd window to run python script
Run('C:\Windows\System32\cmd.exe')
_WinWaitActivate("C:\Windows\System32\cmd.exe","")

# TODO: change the file path to your own.
	#The first file should be wherever your python.exe is located.
		#If you have python in your PATH then you can just put python
	#The second file should be wherever your combined_gui1.py is located
Send("C:\Users\burri\AppData\Local\Programs\Python\Python37-32\python.exe D:\Projects\QuickSpace\combined_gui1.py{ENTER}")
_WinWaitActivate("Quick-Space","")
MouseClick("left",258,460,1)
MouseClick("left",246,252,1)

# ------ Set the length and height of the warehouse here (length {tab} height)---------
Send("12345{TAB}54321")
MouseClick("left",255,438,1)
#--------------------------------------------------------------------------------------

# click on add item on menu screen
MouseClick("left",258,291,1)
# click on item name input
MouseClick("left",235,256,1)

# this will add items, follows this format Send("Name of item {tab} length {tab} width")
Send("Adding item 1{TAB}123{TAB}321")

# --------- Copy and paste these 'MouseClicks' to add another item --------
#clicks on 'ok'
MouseClick("left",266,503,1)
#clicks on 'yes' to add another
MouseClick("left",184,399,1)
#these 3 clicks selects the input of the item name so that they will be overwritten
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)
# -----------------------------------------------------------------------------

Send("Adding item 3{TAB}456{TAB}654")

MouseClick("left",266,503,1)
MouseClick("left",184,399,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)

Send("Adding another item from script 1 {TAB}987{TAB}65")

MouseClick("left",266,503,1)
MouseClick("left",184,399,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)

Send("Adding another item from script 2 {TAB}987{TAB}65")

MouseClick("left",266,503,1)
MouseClick("left",184,399,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)

Send("Adding another item from script 3 {TAB}987{TAB}65")

MouseClick("left",266,503,1)
MouseClick("left",184,399,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)
MouseClick("left",296,252,1)

Send("Adding another item from script 4 {TAB}987{TAB}65")

#----------run this to stop adding items and display warehouse.---------
# press 'ok' to add current item
MouseClick("left",256,504,1)
# select no to 'Add another item?' window
MouseClick("left",316,400,1)
#-----------------------------------------------------------------------

# open warehouse info when menu is open
MouseClick("left",275,394,1)
# to refresh warehouse, when warehouseinfo is open
MouseClick("left",389,338,1)

# go back to menu from warehouse info window
#MouseClick("left",252,636,1)

#endregion --- Au3Recorder generated code End ---
