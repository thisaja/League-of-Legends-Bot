import win32api
clientWidth=1024
clientHeight=576
gameWidth=1024
gameHeight=768
computerWidth=win32api.GetSystemMetrics(0)
computerHeight=win32api.GetSystemMetrics(1)
taskbarHeight=36
clientCoords=(int((computerWidth-clientWidth)/2),int((computerHeight-clientHeight-taskbarHeight)/2))
gameCoords=(int((computerWidth-gameWidth)/2),int((computerHeight-gameHeight)/2))
class client:
    playButton=545-448+clientCoords[0],324-294+clientCoords[1]
    coopButton=567-448+clientCoords[0],372-294+clientCoords[1]
    introButton=813-448+clientCoords[0],691-294+clientCoords[1]
    beginnerButton=813-448+clientCoords[0],713-294+clientCoords[1]
    intermediateButton=813-448+clientCoords[0],739-294+clientCoords[1]
    confirmButton=874-448+clientCoords[0],844-294+clientCoords[1]
    findMatchButton=872-448+clientCoords[0],841-294+clientCoords[1]
    acceptButton=958-448+clientCoords[0],734-294+clientCoords[1]
    searchButton=1063-448+clientCoords[0],376-294+clientCoords[1]
    champButton=754-448+clientCoords[0],426-294+clientCoords[1]
    lockInButton=962-448+clientCoords[0],778-294+clientCoords[1]
    xButton=802-448+clientCoords[0],840-294+clientCoords[1]
    honorButton=736-448+clientCoords[0],551-294+clientCoords[1]
    chatButton=525-448+clientCoords[0],837-294+clientCoords[1]
    dailyPlayButton=956-448+clientCoords[0],603-294+clientCoords[1]

class game:
    tower=(1330-448+gameCoords[0],886-216+gameCoords[1])
    base=(1245-448+gameCoords[0],965-216+gameCoords[1])
    searchShop=(661-448+gameCoords[0],367-216+gameCoords[1])
    item1=(634-448+gameCoords[0],637-216+gameCoords[1])
    item2=(634-448+gameCoords[0],532-216+gameCoords[1])
    item3=(684-448+gameCoords[0],532-216+gameCoords[1])
    item4=(734-448+gameCoords[0],532-216+gameCoords[1])
    item5=(684-448+gameCoords[0],637-216+gameCoords[1])
    item6=(734-448+gameCoords[0],637-216+gameCoords[1])
    item7=(634-448+gameCoords[0],732-216+gameCoords[1])
    item8=(684-448+gameCoords[0],732-216+gameCoords[1])
    item9=(734-448+gameCoords[0],732-216+gameCoords[1])
    dBlade=(634-448+gameCoords[0],437-216+gameCoords[1])
    potion=(684-448+gameCoords[0],437-216+gameCoords[1])
    healthBar=(950-448+gameCoords[0],955-216+gameCoords[1])
    recallButton=(1197-448+gameCoords[0],940-216+gameCoords[1])
