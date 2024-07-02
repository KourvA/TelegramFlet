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
        "page_bg_color" : "#0e1621",
        "main_fg_color" : "#ffffff",
        "app_bar_color" : "#17212b",
        "subtitle_color": "#aaaaaa",
        "icon_bg_color" : "#5b6677",
        "status_color"  : "#00ff00",
        "check_color"   : "#2f6ea5",
        "avatar_color"  : "#55aaff",
        "avatar_color2" : "#aaaa7f",
        "avatar_color3" : "#ff7386"
    }

    # Page alignments setup
    type CrossAxis = ft.CrossAxisAlignment
    page.horizontal_alignment: CrossAxis = ft.CrossAxisAlignment.CENTER

    # Page theme setup (Defaults to Dark)
    page.theme_mode = ft.ThemeMode.DARK

    # Main app bar setup
    page.bgcolor = palette["page_bg_color"]
    page.padding = 0
    page.appbar = ft.AppBar(
        # Leading section
        leading_width=40,
        leading=ft.IconButton(
            icon="menu"
        ),
        
        # Title section
        center_title=False,
        bgcolor=palette["app_bar_color"],
        title=ft.Text(
            value="Connecting..."
        ),
        # Trailing actions
        actions=[
            ft.IconButton(
                icon="search"
            ),
        ]
    )

    # Story section setup
    page.add(
        ft.Container(
            bgcolor=palette["app_bar_color"],
            content=ft.Row(
                spacing=25,
                height=80,
                controls=[
                    # Empty space
                    ft.Text(),
                    # User story (My story)
                    ft.Stack(
                        width=40,
                        height=40,
                        controls=[
                            ft.CircleAvatar(
                                content=ft.Column(
                                    spacing=0,
                                    controls=[
                                        ft.CircleAvatar(
                                            content=ft.Text(
                                                value="K"
                                            ),
                                        ),
                                        ft.Text(
                                            value="My story",
                                            size=10,
                                            color=["icon_bg_color"],
                                            width=100,
                                            text_align=ft.TextAlign.CENTER,
                                        )
                                    ]
                                )
                            ),
                            ft.Container(
                                alignment=ft.alignment.bottom_right,
                                content=ft.CircleAvatar(
                                    content=ft.Icon(
                                        name="add", 
                                        size=19
                                    ),
                                    radius=5
                                )
                            )
                        ]
                    ),
                    # Other's story
                    ft.CircleAvatar(
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.CircleAvatar(
                                    content=ft.Text(
                                        value="B"
                                    ),
                                ),
                                ft.Text(
                                    value="Bob",
                                    size=10,
                                    color=["icon_bg_color"],
                                    text_align=ft.TextAlign.CENTER,
                                    width=100
                                )
                            ]
                        )
                    ),
                    # Other's story
                    ft.CircleAvatar(
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.CircleAvatar(
                                    content=ft.Text(
                                        value="A"
                                    ),
                                ),
                                ft.Text(
                                    value="Alex",
                                    size=10,
                                    color=["icon_bg_color"],
                                    width=100,
                                    text_align=ft.TextAlign.CENTER,
                                )
                            ]
                        )
                    )
                ]
            )
        )
    )

    # Chat dialogs setup
    page.add(
        # Chat number 1
        ft.ListTile(
            # Leading section
            leading=ft.Stack(
                width=40,
                height=40,
                controls=[
                    ft.CircleAvatar(
                        ft.Text(
                            value="K", 
                            size=20
                        ),
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
            # Title section (with mute icon)
            title=ft.Row(
                spacing=5, 
                controls=[
                    ft.Text(
                        value="Kourva", 
                        size=20
                    ),
                    ft.Icon(
                        name="volume_off", 
                        size=15, 
                        color=palette["icon_bg_color"]
                    )
                ]
            ),
            # Subtitle section
            subtitle=ft.Text(
                value="Hey did you see my car??",
                color=palette["subtitle_color"]
            ),
            # Trailing section
            trailing=ft.Column(
                controls=[
                    ft.Text(
                        value="2:16AM", 
                        size=10, 
                        color=palette["subtitle_color"],
                        text_align=ft.TextAlign.RIGHT
                    ),
                    ft.Icon(
                        name="done_all",
                        color=palette["check_color"]
                    )
                ]
            )
        ),
        # Chat number 2
        ft.ListTile(
            # Leading section
            leading=ft.Stack(
                width=40,
                height=40,
                controls=[
                    ft.CircleAvatar(
                        ft.Text(
                            value="L", 
                            size=20
                        ),
                        bgcolor=palette["avatar_color2"]
                    ),
                ]
            ),
            # Title section (with mute icon)
            title=ft.Row(
                spacing=5, 
                controls=[
                    ft.Text(
                        value="Leo", 
                        size=20
                    ),
                    ft.Icon(
                        name="volume_off", 
                        size=15, 
                        color=palette["icon_bg_color"]
                    )
                ]
            ),
            # Subtitle section
            subtitle=ft.Text(
                value="I can't wait to see it!", 
                color="#aaaaaa"
            ),
            # Trailing section
            trailing=ft.Column(
                controls=[
                    ft.Text(
                        value="7:12PM",
                        size=10, 
                        color=palette["subtitle_color"],
                        text_align=ft.TextAlign.RIGHT
                    ),                    
                    ft.CircleAvatar(
                        ft.Text(
                            value="4", 
                            size=15
                        ),
                        bgcolor="#3e546a",
                        width=25,
                        height=25
                    )
                ]
            )
        ),
        # Chat number 3
        ft.ListTile(
            # Leading section
            leading=ft.Stack(
                width=40,
                height=40,
                controls=[
                    ft.CircleAvatar(
                        ft.Text(
                            value="M", 
                            size=20
                        ),
                        bgcolor=palette["avatar_color3"]
                    ),
                ]
            ),
            # Title section ( without mute icon)
            title=ft.Row(
                spacing=5, 
                controls=[
                    ft.Text(
                        value="Marry", 
                        size=20
                    ),
                ]
            ),
            # Subtitle section
            subtitle=ft.Text(
                value="Wows that's awesome!!!", 
                color=palette["subtitle_color"]
            ),
            # Trailing section
            trailing=ft.Column(
                controls=[
                    ft.Text(
                        value="9:49AM", 
                        size=10, 
                        color=palette["subtitle_color"],
                        text_align=ft.TextAlign.RIGHT
                    ),
                    ft.CircleAvatar(
                        ft.Text(
                            value="9", 
                            size=15
                        ),
                        bgcolor="#2f6ea5",
                        width=25,
                        height=25
                    )
                ]
            )
        )
    )

    # Bottom story floating button
    page.add(
        ft.FloatingActionButton(
            icon="photo_camera", 
            bgcolor="#2f6ea5",
            shape=ft.CircleBorder()
        )
    )

# Run the Flet app
if __name__ == "__main__":
    ft.app(
        target=main, 
        assets_dir="./assets"
    )
