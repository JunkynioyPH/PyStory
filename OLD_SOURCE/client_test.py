import App.CrossAppComms as Comms

audioEngine = Comms.ClientObj("127.0.2.1",2222,"Game")

audioEngine.send("audioIndex:add:audio:./Assets/Audio/Music/mainMenu.ogg")
audioEngine.send("listDevices")
audioEngine.send("toggle:audioLoop")
audioEngine.send("play:audio:mainMenu")