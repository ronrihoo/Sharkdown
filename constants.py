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
            load='Load',
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
            copy='Ctrl+C',
            paste='Ctrl+P',
            new='Ctrl+N',
            undo='Ctrl+Z',
            redo='Ctrl+Shift+Z',
            quit='Ctrl+Q',
            editor_viewer='Ctrl+1',
            editor='Ctrl+2',
            viewer='Ctrl+3')
    )
