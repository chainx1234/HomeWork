from pygame import mixer

mixer.init()
mixer.music.load('G:\\Media\\coiBaoDong.mp3')
mixer.music.play()

import playsound
playsound.playsound('G:\\Media\\coiBaoDong.mp3', True)