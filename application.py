import tkinter as tk
import tkinter.simpledialog as tksd
import topic
import pickle

class Application:
    def __init__(self):
        '''
        start by setting some intial variables
        create a list to store the topics that will be tracked
        create a variable to hightlight a position in the list of topics
        create a variable that will hold the topic object that is in the highlighted position
        '''
        self.__topics = []
        self.__selected_index = -1
        self.__selected_topic = None

        '''
        build the gui for the application and title it Class Manager
        '''
        self.__window = tk.Tk()
        self.__window.title('Class Manager')

        '''
        add drop down menus for the application
        create tkinter menu and link it to the GUI using config
        '''
        self.__menu = tk.Menu(self.__window)
        self.__window.config(menu=self.__menu)

        '''
        create File submenu with Load and Save commands
        '''
        self.__submenu = tk.Menu(self.__menu)
        self.__menu.add_cascade(label='File', menu=self.__submenu)
        self.__submenu.add_command(label='Save Topics', command=self.save_info) 
        self.__submenu.add_command(label='Load Topics', command=self.load_info)

        '''
        create Topic submenu with Create and Delete commands
        '''
        self.__submenu = tk.Menu(self.__menu)
        self.__menu.add_cascade(label='Topic', menu=self.__submenu)
        self.__submenu.add_command(label='Create New Topic', command=self.add_new_topic)
        self.__submenu.add_command(label='Start New Week', command=self.start_new_week)
        self.__submenu.add_command(label='Delete Topic', command=self.delete_topic)
        
        '''
        create Session submenu with Start and Stop commands
        '''
        self.__submenu = tk.Menu(self.__menu)
        self.__menu.add_cascade(label='Session', menu=self.__submenu)
        self.__submenu.add_command(label='Start Session', command=self.start_session)
        self.__submenu.add_command(label='Stop Session', command=self.stop_session)
        self.__submenu.add_command(label='Manually Enter Session', command=self.enter_session)

        '''
        add entry textbox to allow user to enter new topic
        create a control variable to hold user input
        create tkinter frame to hold topic entry widget
        create label for topic entry widget
        create entry textbox
        create submit button for widget
        pack all contents into frame and pack frame
        '''
        
        self.__name = tk.StringVar()
        frame = tk.Frame(self.__window)
        label = tk.Label(frame, text="Class Name", width=15, anchor=tk.W)
        entry = tk.Entry(frame, textvariable=self.__name, width=30)
        self.__add_button = tk.Button(frame, text='Add Class', anchor=tk.W, command=self.add_topic)

        label.pack(side='left')
        self.__add_button.pack(side='right')
        entry.pack(side='right')
        frame.pack()
        

        '''
        create Listbox to display topic list
        create tkinter frame to hold listbox
        specify functionality of listbox
        pack listbox to frame and pack frame
        '''
        frame = tk.Frame(self.__window)
        self.__topic_list = tk.Listbox(frame, width=120, selectmode=tk.SINGLE)
        self.__topic_list.bind('<<ListboxSelect>>', self.on_select)
        self.__topic_list.pack()
        frame.pack()

        '''
        create a bar of buttons at the bottom of the gui to start and stop sessions
        create tkinter frame to hold bar of buttons
        create buttons
        pack buttons to frame
        pack frame
        '''
        frame = tk.Frame(self.__window)
        subframe = tk.Frame(frame)
        self.__new_week_button = tk.Button(
            subframe, text='Start New Week', state='disabled', anchor=tk.W, command=self.start_new_week)
        #self.__delete_button = tkinter.Button(
 #           frame, text='Delete Class', state='disabled', anchor=tk.W, command=self.delete_topic)
        self.__start_button = tk.Button(
            frame, text='Start Session', state='disabled', anchor=tk.W, command=self.start_session)
        self.__stop_button = tk.Button(
            frame, text='Stop Session', state='disabled', anchor=tk.W, command=self.stop_session)
        self.__new_week_button.pack()
        subframe.pack()
 #       self.__delete_button.pack(side='left')
        self.__start_button.pack(side='right')
        self.__stop_button.pack(side='right')
        frame.pack()

    def on_select(self, e):
        self.__selected_index = int(self.__topic_list.curselection()[0])
        self.__selected_topic = self.__topics[self.__selected_index]
 #       self.__delete_button['state'] = 'normal'
        self.__start_button['state'] = 'normal'
        self.__new_week_button['state'] = 'normal'

    def add_topic(self):
        t = topic.Topic(self.__name.get())
        self.__topics.append(t)
        self.__topic_list.insert(tk.END, str(t))
        self.__name.set("")

    def add_new_topic(self):
        name = tksd.askstring('New Class', 'Enter Class Name')
        t = topic.Topic(name)
        self.__topics.append(t)
        self.__topic_list.insert(tk.END, str(t))
        self.__name.set("")


    def delete_topic(self):
        self.__topic_list.delete(self.__selected_index)
        del self.__topics[self.__selected_index]
 #       self.__delete_button['state'] = 'disable'
        self.__start_button['state'] = 'disable'

    def start_session(self):
        self.__selected_topic.start_new_session()
        self.__start_button['state'] = 'disable'
        self.__stop_button['state'] = 'normal'

    def stop_session(self):
        self.__selected_topic.end_session()
        self.__start_button['state'] = 'normal'
        self.__stop_button['state'] = 'disable'
        self.__topic_list.delete(self.__selected_index)
        self.__topic_list.insert(self.__selected_index, self.__selected_topic)

    def enter_session(self):
        minutes = tksd.askinteger('New Session', 'Enter Session Time In Minutes')
        self.__selected_topic.start_new_session(minutes)
        self.__topic_list.delete(self.__selected_index)
        self.__topic_list.insert(self.__selected_index, self.__selected_topic)

    def start_new_week(self):
        self.__selected_topic.start_new_week()
        self.__topic_list.delete(self.__selected_index)
        self.__topic_list.insert(self.__selected_index, self.__selected_topic)

    def save_info(self):
        file = open('file.dat', 'wb')
        pickle.dump(self.__topics, file)
        file.close()

    def load_info(self):
        try:
            file = open('file.dat', 'rb')
            self.__topics = pickle.load(file)
            file.close()
            for topic in self.__topics:
                self.__topic_list.insert(tk.END, str(topic))
            
        except:
            print("file error")

    def start(self):
        tkinter.mainloop()

def main():
    app = Application()
    app.start


main()
