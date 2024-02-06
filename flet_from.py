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
    page.update()

    # Форма
    headline = ft.Text(value='Заявка на техническое обслуживание',
                       size=25)
    # Название Организации
    Name_Organization = ft.TextField(label='Название Организации',
                                     border_color='#fefff9',
                                     dense=True)
    # Номер Телефона
    Nomber = ft.TextField(label='Номер телефона',
                          border_color='#fefff9',
                          dense=True,
                          keyboard_type=ft.KeyboardType.PHONE,
                          input_filter=ft.NumbersOnlyInputFilter(),
                          prefix_text='8 ',
                          max_length=10)
    form = ft.Column(
        controls=[
            ft.Container(
                content=headline,
                padding=10,
                margin=5,
            ),
            ft.Container(
                content=Name_Organization,
                padding=10,
                margin=5,
            ),
            ft.Container(
                content=Nomber,
                padding=10,
                margin=5,
            )
        ]
    )


    # Название Организации
    Name_Organization = ft.TextField(label='Название Организации',
                                     border_color='#fefff9',
                                     dense=True)




    prog_bars: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    upload_button = Ref[ElevatedButton]()

    def file_picker_result(e: FilePickerResultEvent):
        upload_button.current.disabled = True if e.files is None else False
        prog_bars.clear()
        files.current.controls.clear()
        if e.files is not None:
            for f in e.files:
                prog = ProgressRing(value=0, bgcolor="#eeeeee", width=20, height=20)
                prog_bars[f.name] = prog
                files.current.controls.append(Row([prog, Text(f.name)]))
        page.update()

    def on_upload_progress(e: FilePickerUploadEvent):
        prog_bars[e.file_name].value = e.progress
        prog_bars[e.file_name].update()

    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)

    def upload_files(e):
        uf = []
        if file_picker.result is not None and file_picker.result.files is not None:
            for f in file_picker.result.files:
                uf.append(
                    FilePickerUploadFile(
                        f.name,
                        upload_url=page.get_upload_url(f.name, 600),
                    )
                )
            file_picker.upload(uf)

    # hide dialog in a overlay
    page.overlay.append(file_picker)
    # Добавление всех элементов на страницу
    page.add(
        form,
        Row(
            [ElevatedButton(
                "Select files...",
                icon=icons.FOLDER_OPEN,
                on_click=lambda _: file_picker.pick_files(allow_multiple=True)
            ),
            Column(
                ref=files
            )]
        ),
    )


ft.app(target=main, port=5905, assets_dir='assets', upload_dir="uploads")
