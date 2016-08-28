class AppConstants:

    def __init__(self):
        self.__init__()

    data = dict(
        properties=dict(
            title='Sharkdown'),
        actions=dict(
            copy='Copy',
            paste='Paste',
            undo='Undo',
            redo='Redo',
            new='New',
            load='Open',
            save='Save',
            save_as='Save As',
            exit='Exit',
            editor_viewer='Editor - Viewer',
            editor_only='Editor Only',
            viewer_only='Viewer Only',
            docs='Documentation',
            about='About'),
        images=dict(
            icon='img/icon.png',
            clear='img/clear.png',
            bold='img/bold.png',
            italic='img/italic.png',
            strike_thru='img/strike_thru.png',
            code_block='img/code_block.png',
            quotation='img/quotation.png'),
        shortcuts=dict(
            select_all='Ctrl+A',
            copy='Ctrl+C',
            paste='Ctrl+P',
            new='Ctrl+N',
            undo='Ctrl+Z',
            redo='Ctrl+Shift+Z',
            exit='Ctrl+Q',
            load='Ctrl+O',
            save='Ctrl+S',
            editor_viewer='Alt+1',
            editor='Alt+2',
            viewer='ALt+3')
    )
