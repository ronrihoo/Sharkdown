from util.constants import AppConstants

"""UI Config

For the sake of translations and ease of configuration, this is always worth it.

Nothing is returned here.
"""


def setup(main_window):

    # MENU - FILE - SET TEXT
    main_window.actionNew.setText(AppConstants.data['actions']['new'])
    main_window.actionLoad.setText(AppConstants.data['actions']['open'])
    main_window.actionSave.setText(AppConstants.data['actions']['save'])
    main_window.actionSave_As.setText(AppConstants.data['actions']['save_as'])
    main_window.actionExit.setText(AppConstants.data['actions']['exit'])

    # MENU - FILE - TRIGGERED
    main_window.actionNew.triggered.connect(main_window.new_file)
    main_window.actionLoad.triggered.connect(main_window.load_file)
    main_window.actionSave.triggered.connect(main_window.save_file)
    main_window.actionSave_As.triggered.connect(main_window.save_as_file)
    main_window.actionExit.triggered.connect(main_window.exit_program)

    # MENU - EDIT - TRIGGERED
    main_window.actionSkip.triggered.connect(main_window.skip_action)

    # MENU - VIEW - SET TEXT
    main_window.actionEditor_Viewer.setText(AppConstants.data['actions']['editor_viewer'])
    main_window.actionEditor_Only.setText(AppConstants.data['actions']['editor_only'])
    main_window.actionViewer_Only.setText(AppConstants.data['actions']['viewer_only'])

    # MENU - VIEW - TRIGGERED
    main_window.actionEditor_Viewer.triggered.connect(main_window.split_view)
    main_window.actionEditor_Only.triggered.connect(main_window.editor_only)
    main_window.actionViewer_Only.triggered.connect(main_window.viewer_only)

    # MENU - FORMAT - SET TITLE (CONTAINER ITEMS)
    main_window.menuCommand.setTitle(AppConstants.data['menu_title']['command'])
    main_window.menuVariable.setTitle(AppConstants.data['menu_title']['variable'])
    main_window.menuCode.setTitle(AppConstants.data['menu_title']['code'])

    # MENU - FORMAT - SET TEXT
    main_window.actionH1.setText(AppConstants.data['format']['h1'])
    main_window.actionH2.setText(AppConstants.data['format']['h2'])
    main_window.actionH3.setText(AppConstants.data['format']['h3'])
    main_window.actionBold.setText(AppConstants.data['format']['bold'])
    main_window.actionItalic.setText(AppConstants.data['format']['italic'])
    main_window.actionList.setText(AppConstants.data['format']['bullet'])
    main_window.actionInline_Code.setText(AppConstants.data['format']['inline_code'])
    main_window.actionCode_Block.setText(AppConstants.data['format']['code_block'])
    main_window.actionLabeled_Code.setText(AppConstants.data['format']['labeled_code'])
    main_window.actionSecondary_Label_Code.setText(AppConstants.data['format']['secondary_labeled_code'])
    main_window.actionVariable_2.setText(AppConstants.data['format']['variable'])
    main_window.actionInline_Variable.setText(AppConstants.data['format']['inline_code_variable'])
    main_window.actionCommand_Nonroot.setText(AppConstants.data['format']['nonroot_command'])
    main_window.actionCommand_Root.setText(AppConstants.data['format']['root_command'])
    main_window.actionCommand_Custom.setText(AppConstants.data['format']['custom_command'])
    main_window.actionNote_Block.setText(AppConstants.data['format']['note'])
    main_window.actionWarning_Block.setText(AppConstants.data['format']['warning'])
    main_window.actionURL.setText(AppConstants.data['format']['url'])
    main_window.actionImage.setText(AppConstants.data['format']['image'])
    main_window.actionEm_Dash.setText(AppConstants.data['format']['em_dash'])

    # MENU - FORMAT - SET ICON TEXT
    main_window.actionH1.setIconText(AppConstants.data['icon_text']['h1'])
    main_window.actionH2.setIconText(AppConstants.data['icon_text']['h2'])
    main_window.actionH3.setIconText(AppConstants.data['icon_text']['h3'])
    main_window.actionBold.setIconText(AppConstants.data['icon_text']['bold'])
    main_window.actionItalic.setIconText(AppConstants.data['icon_text']['italic'])
    main_window.actionList.setIconText(AppConstants.data['icon_text']['bullet'])
    main_window.actionInline_Code.setIconText(AppConstants.data['icon_text']['inline_code'])
    main_window.actionCode_Block.setIconText(AppConstants.data['icon_text']['code_block'])
    main_window.actionLabeled_Code.setIconText(AppConstants.data['icon_text']['labeled_code'])
    main_window.actionSecondary_Label_Code.setIconText(AppConstants.data['icon_text']['secondary_labeled_code'])
    main_window.actionVariable_2.setIconText(AppConstants.data['icon_text']['variable'])
    main_window.actionInline_Variable.setIconText(AppConstants.data['icon_text']['inline_code_variable'])
    main_window.actionCommand_Nonroot.setIconText(AppConstants.data['icon_text']['nonroot_command'])
    main_window.actionCommand_Root.setIconText(AppConstants.data['icon_text']['root_command'])
    main_window.actionCommand_Custom.setIconText(AppConstants.data['icon_text']['custom_command'])
    main_window.actionNote_Block.setIconText(AppConstants.data['icon_text']['note'])
    main_window.actionWarning_Block.setIconText(AppConstants.data['icon_text']['warning'])
    main_window.actionURL.setIconText(AppConstants.data['icon_text']['url'])
    main_window.actionImage.setIconText(AppConstants.data['icon_text']['image'])
    main_window.actionEm_Dash.setIconText(AppConstants.data['icon_text']['em_dash'])

    # MENU - FORMAT - SET TOOLTIP
    main_window.actionH1.setToolTip(AppConstants.data['tooltip']['h1'])
    main_window.actionH2.setToolTip(AppConstants.data['tooltip']['h2'])
    main_window.actionH3.setToolTip(AppConstants.data['tooltip']['h3'])
    main_window.actionBold.setToolTip(AppConstants.data['tooltip']['bold'])
    main_window.actionItalic.setToolTip(AppConstants.data['tooltip']['italic'])
    main_window.actionList.setToolTip(AppConstants.data['tooltip']['bullet'])
    main_window.actionInline_Code.setToolTip(AppConstants.data['tooltip']['inline_code'])
    main_window.actionCode_Block.setToolTip(AppConstants.data['tooltip']['code_block'])
    main_window.actionLabeled_Code.setToolTip(AppConstants.data['tooltip']['labeled_code'])
    main_window.actionSecondary_Label_Code.setToolTip(AppConstants.data['tooltip']['secondary_labeled_code'])
    main_window.actionVariable_2.setToolTip(AppConstants.data['tooltip']['variable'])
    main_window.actionInline_Variable.setToolTip(AppConstants.data['tooltip']['inline_code_variable'])
    main_window.actionCommand_Nonroot.setToolTip(AppConstants.data['tooltip']['nonroot_command'])
    main_window.actionCommand_Root.setToolTip(AppConstants.data['tooltip']['root_command'])
    main_window.actionCommand_Custom.setToolTip(AppConstants.data['tooltip']['custom_command'])
    main_window.actionNote_Block.setToolTip(AppConstants.data['tooltip']['note'])
    main_window.actionWarning_Block.setToolTip(AppConstants.data['tooltip']['warning'])
    main_window.actionURL.setToolTip(AppConstants.data['tooltip']['url'])
    main_window.actionImage.setToolTip(AppConstants.data['tooltip']['image'])
    main_window.actionEm_Dash.setToolTip(AppConstants.data['tooltip']['em_dash'])

    # MENU - FORMAT - TRIGGERED
    main_window.actionH1.triggered.connect(main_window.h1_action)
    main_window.actionH2.triggered.connect(main_window.h2_action)
    main_window.actionH3.triggered.connect(main_window.h3_action)
    main_window.actionBold.triggered.connect(main_window.bold_action)
    main_window.actionItalic.triggered.connect(main_window.italic_action)
    main_window.actionList.triggered.connect(main_window.list_action)
    main_window.actionInline_Code.triggered.connect(main_window.inline_code_action)
    main_window.actionCode_Block.triggered.connect(main_window.code_block_action)
    main_window.actionLabeled_Code.triggered.connect(main_window.label_code_action)
    main_window.actionSecondary_Label_Code.triggered.connect(main_window.secondary_label_action)
    main_window.actionVariable_2.triggered.connect(main_window.variable_action)
    main_window.actionInline_Variable.triggered.connect(main_window.inline_variable_action)
    main_window.actionCommand_Nonroot.triggered.connect(main_window.nonroot_action)
    main_window.actionCommand_Root.triggered.connect(main_window.root_action)
    main_window.actionCommand_Custom.triggered.connect(main_window.custom_action)
    main_window.actionNote_Block.triggered.connect(main_window.note_action)
    main_window.actionWarning_Block.triggered.connect(main_window.warning_action)
    main_window.actionURL.triggered.connect(main_window.url_action)
    main_window.actionImage.triggered.connect(main_window.image_action)
    main_window.actionEm_Dash.triggered.connect(main_window.em_dash_action)

    # MENU - HELP
    main_window.actionDocs.setText(AppConstants.data['actions']['docs'])
    main_window.actionAbout.setText(AppConstants.data['actions']['about'])
    main_window.actionDocs.triggered.connect(main_window.send_to_docs)
    main_window.actionAbout.triggered.connect(main_window.about_popup)
