#these are the auth information
from settings import ai,ak,sk

voice_path = '..//'
import aip
from aip import AipSpeech

'''
initiate a Aip object
using auth information
'''
asp = AipSpeech(ai,ak,sk)

'''
content including comma, period question mark and different sentence structure. It can be sensed that current model
is not good at handling these features

based on the test of content[4,5,6]
system can handle chinese, english, chinese mixing english
it handles english very well, handle API as A  P   I
Wavenet as wavenet
But test on content6 demonstrates that this system cant not handle Unicode characters in other language 
like Korea, Russian and Japanese
Cantonese?? : )   
'''

content1='轻轻的我走了，正如我轻轻的来。 我挥一挥衣袖，不带走一片云彩。 难道说这河里的水不清澈吗？那河畔的金柳是夕阳中的新娘，波光里的艳影在我心头荡漾，在康河的柔波里，我甘心做一条水草。'
'''
Expriment show that, in connection and coherent part of a sentence, both synthesis and recognition are struggling get
things straight.
That could be a AI problem where it doesn't focus, and failed to handle things with attention on tricky part
And clearly, when it comes to the less frequent word, model failed. It shows similar weak point to the statistical machine
learning based methods. It still reflecting the statistical distribution of the training datasets.

On the other hand, human beings can easily handle the low freqency problem and can make a better use of context.
I doubt the recognition accuracy metrics that concluded this system out-performed human beings. It is biased
Human beings are much better on handling the tricky and rare situation and get the meaning better and understand context better. 


Another observation is that when we run this code twice, it gives slightly different result, it's more like a NLP problem of
cutting the sentence

when we change the person, we can see the emotional personnel profile[3,4] are harder to recognize than
standard personnel[1,2]
'''
content2='浸会大学异构计算实验室深度学习评测系统'
content3='浸会大学异构计算实验室'
content4='百度语音    API'
content5='谷歌Wavenet Bonjour'
content6='안녕하세요,Доброе утро,おはようございます'
content7='API'
content8='撑着油纸伞，独自。彷徨在悠长、悠长。又寂寥的雨巷。我希望逢着。一个丁香一样地。结着愁怨的姑娘。她是有。丁香一样的颜色。丁香一样的芬芳。丁香一样的忧愁。在雨中哀怨。哀怨又彷徨。她彷徨在这寂寥的雨巷。撑着油纸伞。像我一样。像我一样地。默默彳亍着。冷漠、凄清，又惆怅。她默默地走近。走近，又投出。太息一般的眼光。她飘过。像梦一般地。像梦一般地凄婉迷茫。像梦中飘过。一枝丁香地。我身旁飘过这女郎。她静默地远了、远了。到了颓圮的篱墙。走尽这雨巷。在雨的哀曲里。消了她的颜色。散了她的芬芳。消散了，甚至她的。太息般的眼光。丁香般的惆怅。撑着油纸伞，独自。彷徨在悠长、悠长。又寂寥的雨巷。我希望飘过。一个丁香一样地。结着愁怨的姑娘。'
'''
zh is the lang, currently only support chinese
vol is the volume, [0,10]
spd is the speed [0,10]
cuid the user number, can be used to trace the usage user by user
pit
per the personel, [0,4], different voice style
'''

ans = asp.synthesis(content8,'zh',1,{'vol':5,'per' : 2, 'pit' : 6,'spd' : 6,'cuid':123})
if not isinstance(ans, dict):
    with open(voice_path + 'audio.mp3','wb') as f:
        f.write(ans)
# in case of error , print the error json
'''
if isinstance(ans,dict) :
    print ans

from pydub import AudioSegment
song = AudioSegment.from_mp3(voice_path + "audio.mp3")
audioFile = song.export(voice_path + "audio.pcm",format="wav")

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

ans1 = asp.asr(get_file_content(voice_path + 'audio.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})

import codecs

fout1 = codecs.open('seg1.txt','wb','utf-8')

print ans1
for ch in ans1[u'result']:
    print ch
    fout1.write(ch)




#fout1.write(ans1[u'result'])
fout1.close()
'''