#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports
from typing import NoReturn, Dict

# Third-party library imports 
import flet as ft


def main(page: ft.Page) -> NoReturn:
    """
    Main function of our app

    :params: Flet page layout
    :return: None
    """
    # Color properties
    palette: Dict[str,str] = {
        "page_bg_color": "#0e1621",
        "main_fg_color": "#ffffff",
        "app_bar_color": "#17212b",
        "status_text"  : "#436f95",
        "icon_bg_color": "#5b6677",
        "status_color" : "#00ff00",
        "avatar_color" : "#55aaff"
    }

    # Page alignments setup
    type CrossAxis = ft.CrossAxisAlignment
    type MainAxis = ft.MainAxisAlignment
    page.horizontal_alignment: CrossAxis = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment: MainAxis = ft.MainAxisAlignment.CENTER

    # Page theme setup (Defaults to Dark)
    page.theme_mode = ft.ThemeMode.DARK

    # Main app bar setup
    page.bgcolor = palette["page_bg_color"]
    page.padding = 0
    page.appbar = ft.AppBar(
        # Leading Section
        leading_width=40,
        leading=ft.IconButton(
            icon="arrow_back"
        ),
        # Title Section
        bgcolor=palette["app_bar_color"],
        center_title=False,
        title=ft.Row(
            controls=[
                # Profile picture
                ft.Stack(
                    width=40,
                    height=40,
                    controls=[
                        ft.CircleAvatar(
                            content=ft.Text(
                                value="K"
                            ),
                            color=palette["main_fg_color"],
                            bgcolor=palette["avatar_color"]
                        ),
                        ft.Container(
                            alignment=ft.alignment.bottom_right,
                            content=ft.CircleAvatar(
                                bgcolor=palette["status_color"], 
                                radius=5
                            )
                        )
                    ]
                ),
                # Profile name & status
                ft.Column(
                    spacing=1,
                    controls=[
                        ft.Text(
                            value="Kourva"
                        ),
                        ft.Text(
                            value="Online", 
                            size=14, 
                            color=palette["status_text"]
                        )
                    ]
                )
            ]
        ),
        # Trailing actions
        actions=[
            ft.IconButton(
                icon="call"
            ),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon="volume_off",
                        text="Mute"
                    ),
                    ft.PopupMenuItem(
                        icon="search",
                        text="Search"
                    ),
                    ft.PopupMenuItem(
                        icon="video_call",
                        text="Video Call"
                    ),
                    ft.PopupMenuItem(
                        icon="contacts",
                        text="Add to contacts"
                    ),
                    ft.PopupMenuItem(
                        icon="wallpaper",
                        text="Change Wallpaper"
                    ),
                    ft.PopupMenuItem(
                        icon="clear_all",
                        text="Clear History"
                    ),
                    ft.PopupMenuItem(
                        icon="delete",
                        text="Delete chat"
                    )
                ]
            )
        ]
    )

    # Chat History setup (Assuming it's empty)
    page.add(
        ft.Container(
            margin=10,
            padding=16,
            alignment=ft.alignment.center,
            bgcolor="#1e2c3a",
            width=230,
            height=300,
            border_radius=10,
            content=ft.Column(
                controls=[
                    # Header text
                    ft.Text(
                        value="No messages here yet...", 
                        text_align="center",
                        size=17,
                        weight="BOLD"
                    ),
                    # Body text
                    ft.Text(
                        value="Send a message or click on the greeting below",
                        text_align="center",
                        size=14,
                    ),
                    # Lottie animation
                    ft.Lottie(
                        src="/greeting.json",
                        animate=True,
                        repeat=True,
                        fit=ft.ImageFit.FIT_HEIGHT
                    )
                ]
            )
        )
    )

    # Bottom app bar setup
    page.add(
        ft.BottomAppBar(
            bgcolor=palette["app_bar_color"],
            shape=ft.NotchShape.CIRCULAR,
            height=60,
            content=ft.Row(
                spacing=2,
                controls=[
                    # Emoji icon
                    ft.IconButton(
                        icon="sentiment_satisfied", 
                        icon_color=palette["icon_bg_color"]
                    ),
                    # Input text field
                    ft.CupertinoTextField(
                        placeholder_text="Message...",
                        placeholder_style=ft.TextStyle(
                            color=palette["icon_bg_color"]
                        ),
                        expand=True,
                        bgcolor=ft.colors.TRANSPARENT,
                        multiline=True,
                        color=palette["main_fg_color"],
                        border=ft.border.only(
                            bottom=ft.border.BorderSide(
                                width=0, 
                                color=ft.colors.TRANSPARENT
                            )
                        )
                    ),
                    # File attach icon
                    ft.IconButton(
                        icon="attach_file", 
                        icon_color=palette["icon_bg_color"]
                    ),
                    # Send voice icon
                    ft.IconButton(
                        icon="settings_voice", 
                        icon_color=palette["icon_bg_color"]
                    )
                ]
            )
        )
    )

# Run the Flet app
if __name__ == "__main__":
    ft.app(
        target=main, 
        assets_dir="./assets"
    )
