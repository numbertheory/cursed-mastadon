#! /usr/bin/env python3
from dashport.dash import Dashport, Info
from dashport.run import wrap


def info(app):
    return Info(app)


def quit(app):
    exit(0)


def scroll_down(app):
    app.screen.scroll(1)


def dashport(stdscr):
    app = Dashport(stdscr, scroll=True)
    app.add_control("q", quit)
    rows, cols = app.screen.getmaxyx()
    app.widget("title_bar", text=f"Title {app.cursor_x},{app.cursor_y}",
               align="top", color=256)
    app.layout("split_screen_columns", border=True, scroll=True)
    
    for i in range(0, 1000):
        app.print(content=f"Line: {i}", x=1, y=i, panel="layout.0")

    while True:
        app.refresh()


if __name__ == '__main__':
    wrap(dashport, info)