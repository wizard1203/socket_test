#these are the auth information
from settings import ai,ak,sk

voice_path = 'c://pic//aiReport//'
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
content2='浸会大学异构计算实验室深度学习评测系统'
content3='浸会大学异构计算实验室'
content4='百度语音API'
content5='谷歌Wavenet Bonjour'
content6='안녕하세요,Доброе утро,おはようございます'
'''
zh is the lang, currently only support chinese
vol is the volume, [0,10]
spd is the speed [0,10]
cuid the user number, can be used to trace the usage user by user
pit
per the personel, [0,4], different voice style
'''

ans = asp.synthesis(content4,'zh',1,{'vol':5,'per' : 2, 'pit' : 6,'spd' : 6,'cuid':123})


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

ans1 = asp.asr(get_file_content(voice_path + 'audio.pcm'), 'pcm', 16000, {
    'lan': 'zh',
})

print ans1[u'result']

'''
TODO: see the error situation
'''