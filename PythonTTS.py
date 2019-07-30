import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak('Hello Scott, I represent all the robots at Old Rochester High School. Please help us Scott. You are our only hope')