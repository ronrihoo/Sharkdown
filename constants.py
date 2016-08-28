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
            open='Open',
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
            open='Ctrl+O',
            save='Ctrl+S',
            editor_viewer='Alt+1',
            editor='Alt+2',
            viewer='ALt+3')
    )
    style = dict(
        layout=dict(
            bold='****',
            italics='__',
            Em_Dash='—',
            Link='[](https://)',    # cursor goes in between brackets
            note='<$>[note]\n**Note:** \n<$>\n',
            warning='<$>[warning]\n**Warning:** \n<$>\n',
            H1='# ',
            H2='## ',
            H3='### ',
            Bullet='- ',
            Inline_Code='``',   # cursor needs to be placed in the middle of it, ready for typing
            Code_Block='```\n\n```\n',      # in fact, the cursor needs to go in the right place for each one
            Labeled_Code='```\n[label ]\n\n```\n',
            Secondary_Labeled_Code='```\n[secondary_label ]\n\n```\n',
            Variable='<^><^>',
            Inline_Code_Variable='`<^><^>`',
            Nonroot_Command='```command\n\n```',
            Root_Command='```super_user\n\n```',
            Custom_Command='```custom_prefix()\n\n```',
            Image='![Alt text for screen readers]\n(https://www. )\n'
        )
    )
