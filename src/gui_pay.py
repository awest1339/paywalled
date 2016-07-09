#!/usr/bin/env python
from tkinter import *
from tkinter import ttk


url = ''
proxy = ''
no_check_certificate = False


def make_request(*args):
    print url
    print proxy
    return True


def main():
    global url
    global proxy
    global no_check_certificate
    
    root = Tk()
    root.title("Paywalled GUI Application")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    """
    url = ''
    proxy = ''
    no_check_certificate = False
    """
    ttk.Label(mainframe, text="Enter URL:").grid(column=1, row=1, sticky=W)
    url_entry = ttk.Entry(mainframe, width=50, textvariable=url)
    url_entry.grid(column=2, row=1, sticky=(W, E))
    
    proxy_entry = ttk.Entry(mainframe, width=50, textvariable=proxy)
    proxy_entry.grid(column=2, row=2, sticky=(W, E))

    ttk.Label(mainframe, text="Proxy:").grid(column=1, row=2, sticky=W)
    ttk.Checkbutton(mainframe, text="Disable certificate verification", variable=no_check_certificate).grid(column=2, row=3, sticky=W) 

    ttk.Button(mainframe, text="Open page!", command=make_request).grid(column=3, row=1, sticky=W)


    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    url_entry.focus()
    root.bind('<Return>', make_request)

    root.mainloop()

    
if __name__ == '__main__':
    main()