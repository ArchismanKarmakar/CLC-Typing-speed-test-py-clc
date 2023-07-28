from tkinter import *
import ctypes
import random
import tkinter
 
# For a sharper window
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# Setup
root = Tk()
root.title('Type Speed Test')

# Setting the starting window dimensions
root.geometry('700x700')

# Setting the Font for all Labels and Buttons
root.option_add("*Label.Font", "consolas 30")
root.option_add("*Button.Font", "consolas 30")


# functions
def keyPress(event=None):
    try:
        if event.char.lower() == labelRight.cget('text')[0].lower():
            # Deleting one from the right side.
            labelRight.configure(text=labelRight.cget('text')[1:])
            # Deleting one from the right side.
            labelLeft.configure(text=labelLeft.cget('text') + event.char.lower())
            #set the next Letter Lavbel
            currentLetterLabel.configure(text=labelRight.cget('text')[0])
    except tkinter.TclError:
        pass


def resetWritingLabels():
    # Text List
    possibleTexts = [
        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quaerat illo quia quos culpa nesciunt quam ratione consectetur deleniti obcaecati cum eaque nihil atque natus expedita illum tenetur soluta, dolores numquam.',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia ab praesentium numquam ullam, excepturi culpa nemo, laborum minima sint illo assumenda voluptatem, quibusdam perferendis nam molestias expedita amet? Dolorem nulla odit reiciendis dolorum amet recusandae!',
        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum ab molestias quod officia voluptatibus consectetur officiis quasi excepturi mollitia, tenetur velit, aliquid dignissimos aperiam sit repudiandae nesciunt delectus id. Cum rerum soluta quo accusantium corrupti inventore culpa commodi facilis, odio sint eligendi illo qui vitae beatae possimus consequatur natus recusandae, saepe quidem repellat molestiae excepturi reprehenderit magni architecto. Dolorem, soluta ad. Quasi porro velit pariatur aperiam. Rem saepe distinctio architecto nostrum, totam mollitia iste dicta nisi ducimus doloremque, aspernatur quidem corporis minima, eos iure incidunt cumque expedita perspiciatis accusantium accusamus corrupti libero. Similique officiis a doloribus dolores sit in et blanditiis nesciunt accusantium cupiditate eligendi quod quas tempora repellendus porro dolorum magni quae eaque, aut fugit, iure id excepturi. Nemo?',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sit, id magni. Ipsam rem, voluptates, nostrum aliquam consequuntur, repudiandae laboriosam provident beatae fuga nisi soluta totam illum aut! Laudantium, accusamus repudiandae.',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis atque cum ab sequi quo, cupiditate illum debitis. Eligendi facilis tenetur nostrum incidunt explicabo odit quas accusamus molestiae atque laborum? Impedit labore ea ducimus earum necessitatibus non amet minus laborum cupiditate quidem velit ab iste natus, rem porro libero architecto esse.',
        'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae, architecto. Consequuntur cumque dolore eveniet id eos laboriosam facilis accusamus voluptatum labore esse reprehenderit unde neque recusandae, earum accusantium impedit beatae soluta nemo sapiente ex dignissimos animi inventore libero! Fuga, nemo?',
        'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nihil, eaque.',
        'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima illum, quibusdam eligendi alias repellendus ullam rem, tempora corrupti qui non hic quidem, tenetur error numquam? Omnis est illo itaque ut?',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti dolorum, vero, corporis amet vel provident sed tempora repudiandae explicabo reiciendis officiis dolore placeat itaque quis at suscipit deserunt. Accusantium, non?',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quis aspernatur natus incidunt ad dolore velit molestias, facilis illo earum culpa quam vel minima sint magnam eum fugit quas eius cum.',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Laudantium dicta animi sunt nihil recusandae placeat sint architecto nam impedit voluptatem ab vero, tenetur eligendi pariatur, repudiandae quam. Quasi, sapiente fugiat?',
        'Lorem, ipsum dolor sit amet consectetur adipisicing elit. Facere dignissimos consectetur quos dolorem perferendis vero laboriosam dolore ratione et. Corporis beatae magni aspernatur placeat, dignissimos maxime voluptates ab rem tempora.',
        'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Hic aliquid reprehenderit quaerat rem deserunt laudantium, soluta id deleniti ratione voluptatibus delectus molestiae consectetur. Veniam, nulla! At ab ipsum ducimus qui, deleniti ipsam itaque fuga iste. Error earum ea nobis ab quas qui mollitia reiciendis cum maiores illo, debitis sint, consectetur nisi, eaque pariatur vero.',
        'Lorem ipsum dolor, sit amet consectetur adipisicing elit. Minima esse, est aliquam consequatur iste eos ratione ducimus aut sapiente odio aperiam. Molestiae aut sit laborum, pariatur fuga amet voluptatibus repellat ab eos perferendis architecto accusantium ipsam, nobis saepe dignissimos! Modi, quod error unde ex fugiat autem asperiores iusto voluptate dicta consequuntur vero deleniti, placeat, eaque repudiandae nam quisquam nisi cum incidunt ea totam esse quasi minus tenetur. Odit facilis non, ipsum praesentium ducimus qui odio est iure esse, dignissimos magni fugit optio quod quae numquam repellat minus modi repellendus quis aperiam, saepe nobis? Reprehenderit sunt obcaecati perferendis officia, temporibus ipsum.',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Impedit a pariatur, qui inventore nisi quasi sequi suscipit in officia eum quaerat quos quo distinctio nesciunt dicta ad perspiciatis laboriosam illum similique totam labore cumque. Blanditiis libero enim laudantium dolore rem modi quia nulla voluptate aspernatur aperiam, corporis qui assumenda sit accusantium quam? Ut praesentium quam, libero, consequuntur repellat modi consectetur dolores vitae nulla ipsam neque animi eos esse sint mollitia cum reprehenderit velit quis. Ratione nulla praesentium omnis exercitationem accusamus illo ex fuga dignissimos corrupti culpa magni dolorem sit suscipit natus, aliquid minima vero facilis. Cumque corporis beatae doloribus quos consectetur explicabo tenetur maiores dolores aut! Quia, aspernatur dolore optio molestias repellat est, culpa fuga ratione commodi sapiente modi doloribus minus eos ea earum amet pariatur quae doloremque eveniet! Explicabo amet aperiam et dignissimos veritatis minus placeat repellendus ducimus ex, animi voluptas, qui consectetur autem ipsam, optio cum reprehenderit quos ratione aliquid laborum excepturi praesentium ea. Quas tenetur sapiente at quaerat reprehenderit placeat aspernatur nihil aliquam cum harum maiores laudantium hic saepe qui, in fugit natus exercitationem consequuntur, deleniti vel! Vitae assumenda quia reiciendis blanditiis, laudantium quidem officia ab, fugit, dolores quas provident? Consequatur, perspiciatis officia quod assumenda ea inventore?',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptate reiciendis dicta asperiores repudiandae veritatis unde odio adipisci obcaecati, deleniti, laudantium libero culpa velit ab laboriosam illum provident error nisi repellendus officiis aperiam quibusdam recusandae. Repellendus ab qui tenetur, ex nobis architecto distinctio veniam. Non assumenda illo ullam velit molestiae delectus reprehenderit dolorem architecto corrupti. Eius possimus ad necessitatibus nemo cumque cupiditate deserunt eligendi totam nulla a ducimus distinctio, libero velit alias recusandae quaerat doloremque incidunt quasi error, asperiores quas sint mollitia, fugiat enim! Quia temporibus soluta iure maxime asperiores corporis quasi nostrum, quaerat recusandae. Magnam, et eligendi suscipit officia laudantium, temporibus laborum cupiditate debitis ea iste, assumenda nesciunt beatae est? Omnis velit illum libero atque ab, ipsa esse enim ducimus!',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis, ipsam! Corporis ratione rerum, soluta asperiores repudiandae optio accusantium atque aliquam dolor rem quo aperiam neque perspiciatis molestiae natus saepe nemo?',
        'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Doloribus fugiat nihil nesciunt, officiis dicta facere corrupti sit sequi. At alias exercitationem ut excepturi quam dolores, eum nobis delectus deserunt fugiat.',
        'Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde minima reprehenderit nisi, voluptates aliquid consequuntur delectus magni cupiditate nam a voluptatibus rerum amet tempore quo maxime, perspiciatis, praesentium possimus. Et.',
    ]
    # Chosing one of the texts randomly with the choice function
    text = random.choice(possibleTexts).lower()
    # defining where the text is split
    splitPoint = 0
    # This is where the text is that is already written
    global labelLeft
    labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
    labelLeft.place(relx=0.5, rely=0.5, anchor=E)

    # Here is the text which will be written
    global labelRight
    labelRight = Label(root, text=text[splitPoint:])
    labelRight.place(relx=0.5, rely=0.5, anchor=W)

    # This label shows the user which letter he now has to press
    global currentLetterLabel
    currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
    currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)

    # this label shows the user how much time has gone by
    global timeleftLabel
    timeleftLabel = Label(root, text=f'0 Seconds', fg='grey')
    timeleftLabel.place(relx=0.5, rely=0.4, anchor=S)

    global writeAble
    writeAble = True
    root.bind('<Key>', keyPress)

    global passedSeconds
    passedSeconds = 0

    # Binding callbacks to functions after a certain amount of time.
    root.after(60000, stopTest)
    root.after(1000, addSecond)

def stopTest():
    global writeAble
    writeAble = False
    
    # Calculating the amount of words
    amountWords = len(labelLeft.cget('text').split(' '))
    
    # Destroy all unwanted widgets.
    timeleftLabel.destroy()
    currentLetterLabel.destroy()
    labelRight.destroy()
    labelLeft.destroy()

    # Display the test results with a formatted string
    global ResultLabel
    ResultLabel = Label(root, text=f'Words per Minute: {amountWords}', fg='black')
    ResultLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

    # Display a button to restart the game
    global ResultButton
    ResultButton = Button(root, text=f'Retry', command=restart)
    ResultButton.place(relx=0.5, rely=0.6, anchor=CENTER)

def restart():
    # Destry result widgets
    ResultLabel.destroy()
    ResultButton.destroy()

    # re-setup writing labels.
    resetWritingLabels()

def addSecond():
    # Add a second to the counter.

    global passedSeconds
    passedSeconds += 1
    timeleftLabel.configure(text=f'{passedSeconds} Seconds')

    # call this function again after one second if the time is not over.
    if writeAble:
        root.after(1000, addSecond)

# This will start the Test
resetWritingLabels()

# Start the mainloop
root.mainloop()