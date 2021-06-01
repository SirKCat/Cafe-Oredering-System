from Items import Items
from Receipt import Receipt
import speech_recognition as sr
from gtts import gTTS
import playsound, random, os


# Parent class Order
class Order:
    order = []

    def __del__(self):
        print('Order Confirmed')

    # The input methodology
    def input(self, order=None):
        pass

    # Adds the customer's order to the list of orders
    def addItem(self, num, count):  # Add item
        item = Items.retrieve(num)
        self.order.append([item, count])
        print(count, "item (" + item.name + ") was added")

    # Deletes the latest Item from the order list
    def deleteItem(self):
        print("latest item (" + self.order[-1][0].name + ") is deleted")
        del self.order[-1]

    # Cancel the order
    def cancel(self):
        self.order = []
        print("Order has canceled")
        print(self.order)

    # Sends the order list to the Receipt class to print the receipt
    def deliver(self):
        Receipt.calculateTotal(self.order)
        self.order = []
        del self


# Child class with input() polymorphism. Adds items via clicking on the UI
class OrderByClick(Order):

    def input(self, order=None):
        print("Please chose your drinks")
        _itemNumber, _count = order
        _item = Items.retrieve(_itemNumber)
        self.order.append([_item, count])


# Child class with input() polymorphism. Adds items Orally using voice recognition
class OrderByVoice(Order):

    def input(self, order=None):
        OrderByVoice.speaker("what's your order?")
        while 1:
            voice_data = OrderByVoice.record_audio()
            print(voice_data)
            OrderByVoice.response(voice_data)

# Records the microphone input and sends it to google's recognizer to store the text output in voice_data
    def record_audio(ask=False):
        with sr.Microphone() as source:
            if ask:
                OrderByVoice.speaker(ask)
            audio = recorder.listen(source)
            voice_data = ''
            try:
                voice_data = recorder.recognize_google(audio)
            except sr.UnknownValueError:
                OrderByVoice.speaker('Sorry, I did not understand that')
            except sr.RequestError:
                OrderByVoice.speaker('Sorry, the server is not working')

            return voice_data

# play the audio to the user
    def speaker(audio_string):
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 1000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)

# The logic of voice recognition and ordering
    def response(voice_data):
        cups = [['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6],
                ['7', 7], ['8', 8], ['9', 9], ['10', 10]]
        cups2 = [['two',2],['three',3],['four',4],['five',5],['six',6],
                 ['seven',7],['eight',8],['nine',9],['for',4],['to',2]]

        for i in cups:
            if i[0].lower() in voice_data.lower():
                count = i[1]
                break
            else:
                count = 1


        for i in cups2:
            if i[0].lower() in voice_data.lower():
                count = i[1]
                break



        for item in Items.retrieveAll():

            if item.name.lower() in voice_data.lower():
                OrderByVoice.speaker("you ordered " + str(count) + " of " + item.name)
                order1.order.append([item, count])
                OrderByVoice.speaker("Are you done with your order?")

        if 'yes' in voice_data:
            OrderByVoice.speaker('thank you for ordering')
            OrderByVoice.deliver(order1)
            exit()

        elif 'no' in voice_data:
            pass

        elif 'exit' in voice_data.lower():
            OrderByVoice.speaker('exiting now,.. have a nice day')
            exit()


# Main Function

option = int(input("Enter 1 for by click process, or 2 for voice."))

if option == 1:
    order1 = OrderByClick()
    while True:
        counter = 2
        for item in Items.retrieveAll():
            print(f"{item.ID}- {item.name} ({item.price}SA) --- {item.description} ")
            counter += 1
        print(f"Enter {counter} to stop ordering process")

        itemNumber = int(input("Enter item ID:"))
        if itemNumber >= counter:
            break
        count = int(input("Enter count:"))
        if count == 0:
            continue
        order1.input((itemNumber, count))
        print("----------------------------------")
        print()
elif option == 2:
    order1 = OrderByVoice()
    recorder = sr.Recognizer()
    order1.input((0))
    print("----------------------------------")
    print()

Order.deliver(order1)
