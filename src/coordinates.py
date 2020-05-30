from win32api import GetSystemMetrics
clientWidth=1024
clientHeight=576
gameWidth=1024
gameHeight=768
computerWidth=GetSystemMetrics(0)
computerHeight=GetSystemMetrics(1)
taskbarHeight=36
clientCoords=(int((computerWidth-clientWidth)/2),int((computerHeight-clientHeight-taskbarHeight)/2))
gameCoords=(int((computerWidth-gameWidth)/2),int((computerHeight-gameHeight)/2))
class client:
    playButton=545-clientCoords[0],324-clientCoords[1]
    coopButton=567-clientCoords[0],372-clientCoords[1]
    introButton=813-clientCoords[0],691-clientCoords[1]
    beginnerButton=813-clientCoords[0],713-clientCoords[1]
    intermediateButton=813-clientCoords[0],739-clientCoords[1]
    confirmButton=874-clientCoords[0],844-clientCoords[1]
    findMatchButton=872-clientCoords[0],841-clientCoords[1]
    acceptButton=958-clientCoords[0],734-clientCoords[1]
    searchButton=1063-clientCoords[0],376-clientCoords[1]
    champButton=754-clientCoords[0],426-clientCoords[1]
    lockInButton=962-clientCoords[0],778-clientCoords[1]
    xButton=802-clientCoords[0],840-clientCoords[1]

class game:
    tower=(1330-gameCoords[0],886-gameCoords[1])
    base=(1245-gameCoords[0],965-gameCoords[1])
    searchShop=(661-gameCoords[0],367-gameCoords[1])
    item1=(634-gameCoords[0],637-gameCoords[1])
    item2=(634-gameCoords[0],532-gameCoords[1])
    item3=(684-gameCoords[0],532-gameCoords[1])
    item4=(734-gameCoords[0],532-gameCoords[1])
    item5=(684-gameCoords[0],637-gameCoords[1])
    item6=(734-gameCoords[0],637-gameCoords[1])
    item7=(634-gameCoords[0],732-gameCoords[1])
    item8=(684-gameCoords[0],732-gameCoords[1])
    item9=(734-gameCoords[0],732-gameCoords[1])
