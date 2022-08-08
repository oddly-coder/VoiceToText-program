import speech_recognition as speech

def main():
    
    running = True

    while running:
        r = speech.Recognizer()
        with speech.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('say something...')

            audio = r.listen(source)

            message = r.recognize_google(audio) 
            text = open('./bible.txt')
            for line in text:
                if message in line:
                    print(line)
                elif speech.UnknownValueError:
                    print('Could not catch that')
                else:
                    print('Something went wrong')
                
                



if __name__ == "__main__":
    main()