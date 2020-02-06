import speech_recognition as sr

r =sr.Recognizer()

audio = 'rr.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)
    print('Done!')

# with sr.Microphone() as source:
#     print("Listening......")
#     audio = r.listen(source)
#     print("Listened..")
#

try:
    print("Recognizing......")
    text = r.recognize_google(audio)
    print("DATA: "+text)
    r2=[]
    # r= text.split(" ")
    # print(r)
    # r1= input()


    #         break
    #     # else:
    #     #     print("data not found...")
    # print(r2)

except Exception as e:
    print(e)