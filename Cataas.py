from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

Allowed_tags = ["Fierce","Fluffy","Friends","Fulgencio","Funny","Going shopping?","Gray","GreenEyes","Grey","Grumpy",
                "Gustav","Halloween","HandInHand","Happy","Hemingway","Hidden","Hides","Hiding","Hitler","Hugs",
                "If-fits-I-sits","Julijana","KingCat","KitKat","Kitten","Lay","Long","Luz","Maine Coon","Maine coon",
                "Male","Maskcat","Meme","Mimi","Moomoo","My cat(Mamay(мамай)) bebrik.xyz","NSFW","Nazi","New Year",
                "NorthenCat","Norwegian","Norwegian Forest Cat","OG","OnTheNotebook","Orange","Oreo","Oriental","Outside",
                "Peekaboo","Polysson","PopcornTrap","Quantico","Ragdoll","Relaxed","Rex","Roar","SWS","Sad","Scout","Screaming",
                "Shhhsh","Shi","Shiloh","Shoes","Siamese","Sigma Ohio cat very skibidi","Silly","Sillykitty","Simba","Sink",
                "Sleep","Sleeping","Sleepy","Smol","Sniper","Spots","Steve jobs","Summer","Tabby","Tabby  cute","Tabbycat",
                "Tassilo","Teeth","Tent","Tired cat","TorWorld Cat","Torte","Torte Tabby","Trippy","Tuxedo","TwoCats",
                "Village","VoIP","Wafer","Waif","Waits","Weegie","Wet","White","Wide","Wide mouth","X-MAS","Yeet",
                "Zathras","Zoomies","a","achievement","acq","action","adult","advent-calendar-2016","afraid","air_bed",
                "airpods","alarming","alcoholic","aldris","algebra","alien","ange","angel","angry","angry cat","annilou91",
                "annoyed","anoyed","anstrengend","apple","approaching","arm","arrogant","art","artist","asking","asleep",
                "attack","attention","attentive","attitude","ava","avatar","awake","babby","baby","babycat","back",
                "background","backpack","bad_photoshop","baker","baking","ball","bamgu","bang","banker","banzai",
                "basin","basket","bath","beautiful","bed","beer","beg","begging","bella","belly","belly rubs","bengal",
                "bent","berlin","best","bestcat","big","big eyes","big floof","big-eyes","bigfloppa","binky","bird",
                "birthday","biscuit","bitting","black","black & white","black an white","black and white","black cat",
                "black scotish","blackandwhite","blanket","blep","blini","blink","blonde","blue","blue eyes","blueeyes",
                "blur","blurred","blurry","bobba eyes","boi","bombay","bonus dog","boop","boot","bored","bossy","boty",
                "bow","box","boxe","brasileira","brazilian","brazilian cat","bread","breast","british","british shorthair",
                "british-shorthair","broken","brothers","brown","bubble","bucket","bun","bunny","burnt","burrito",
                "burrito-cat","business","buubly","bw","cables","cake","calico","calvin","camera","candle","candy corn",
                "car","caracal","carrier","carrot","cars","cartoon","cash","cat","cat eyes","cat face","cat kneading",
                "cat meowing","cat n frog","cat on table","cat wallpaper","cat1","cat_winston","catcooking","cats",
                "catstickerss","catto","caughtsnacking","ceiling","chair","chaos","check","chicken","chill","chipi",
                "chocked","chonker","christmas","chunky","cinnamon roll","circle","clangen","clawing","cleaning",
                "climb","close","close-up","closed","closed eyes","closeup","clothes","coat","color","colorful",
                "comfy","computer","confident","confused","console","content","cook","cooking","cool","costume",
                "couch","couple","cow","cowboy","cozy","crazy","crazy russian pussycat","cream","creation","creep",
                "crown","cry","crying","cryptid","cucumber","cuddle","cuddles","cup","curl","curled","curled up",
                "cut","cute","cute cat","cutie","daisy","dance","dancing","dark","dark brown","dark vador","darth",
                "darth vader","dash","davie412","days","dead","decorating","deflate","depressed","derp","desk","detective"]


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600,480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка {e}')
        return None


def open_new_window():
    tag = tag_combobox.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котиком')
        new_window.geometry('600x480')
        label = Label(new_window, image=img)
        label.pack()
        label.image = img



def exit():
    window.destroy()

window = Tk()
window.title('Cats')
window.geometry('600x520')

load_Button = Button(text='Загрузить по тегу', command=open_new_window)
load_Button.pack()


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Файл', menu=file_menu)
file_menu.add_command(label='Загрузить фото', command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label='Выход', command=exit)

url = 'https://cataas.com/cat'

tag_label = Label(text='Выбери тег')
tag_label.pack()

tag_combobox = ttk.Combobox(values=Allowed_tags)
tag_combobox.pack()

window.mainloop()
