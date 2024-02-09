import flet as ft
from typing import Dict
import flet_material as fm
from flet import (
    Column,
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerUploadEvent,
    FilePickerUploadFile,
    Page,
    ProgressRing,
    Ref,
    Row,
    Text,
    icons,
)

fm.Theme.set_theme(theme="blue")


def main(page: Page):
    page.title = "Заявка"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = fm.Theme.bgcolor
    page.fonts = {'OpenSansCondensed-Bold': 'fonts/OpenSansCondensed-Bold.ttf'}
    page.theme = ft.Theme(font_family='OpenSansCondensed-Bold')

    # Убрать , не работает в web
    page.window_height = 1280
    page.window_width = 720

    page.update()

    # Форма
    headline = ft.Text(value='Заявка на техническое обслуживание',
                       size=25)
    # Название Организации
    Name_Organization = ft.TextField(label='Название Организации',
                                     border_color='#fefff9',
                                     dense=True,
                                     icon=ft.icons.STORE)
    # Имя пользователя
    Name_User = ft.TextField(label='Имя',
                             border_color='#fefff9',
                             dense=True,
                             icon=ft.icons.ACCOUNT_CIRCLE)

    # Номер Телефона
    Nomber = ft.TextField(label='Номер телефона',
                          border_color='#fefff9',
                          dense=True,
                          keyboard_type=ft.KeyboardType.PHONE,
                          prefix_text='8 ',
                          max_length=10,
                          icon=ft.icons.PHONE)

    # Суть проблемы
    Problem = ft.TextField(label='Суть проблемы',
                           border_color='#fefff9',
                           dense=True,
                           multiline=True,
                           icon=ft.icons.REPORT_PROBLEM)

    form = ft.Column(
        controls=[
            ft.Container(
                content=headline,
                padding=20
            ),
            ft.Container(
                content=Name_Organization,
                padding=3,
                margin=5,
            ),
            ft.Container(
                content=Name_User,
                padding=3,
                margin=5,
            ),
            ft.Container(
                content=Nomber,
                padding=3,
                margin=5,
            ),
            ft.Container(
                content=Problem,
                padding=3,
                margin=5,
            )
        ]
    )

    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", \n".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    def upload_files(e):
        upload_list = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                upload_list.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(upload_list)

    # Загрузка файлов
    file_picker = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()

    page.overlay.append(file_picker)


    # Добавление всех элементов на страницу
    page.add(
        form,
        Row([
            selected_files,
            ft.ElevatedButton(
                "Загрузить фото...",
                icon=ft.icons.UPLOAD_FILE,
                on_click=lambda _: file_picker.pick_files(
                    allow_multiple=True,
                    file_type=ft.FilePickerFileType.IMAGE
                ),
            )
        ],
            alignment=ft.MainAxisAlignment.END),


    )


ft.app(target=main, port=5905, assets_dir='assets', upload_dir="uploads")
