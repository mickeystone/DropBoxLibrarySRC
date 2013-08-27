#Embedded file name: ui/common/screenshots.py
from .strings import UIStrings

class ScreenshotsStrings(UIStrings):
    _strings = dict(splash_title=u'Share Your Screenshots Using Dropbox', splash_cancel_button=u'Cancel', always_move_screenshots=u'Save Screenshots to Dropbox', never_move_screenshots=u'No, Thanks', splash_message=u"Whenever you take a screenshot, we'll save it to your Dropbox and copy a link to your clipboard so you can quickly share it.", splash_message_for_win=u"Whenever you take a screenshot, we'll save it to your Dropbox.\nOr use <b>CTRL + PRINT SCREEN</b> to take a screenshot and copy a link to your clipboard so you can quickly share it.", quota_heading=u'Share your screenshots in a snap', file_name=u'Screenshot %(local_time)s.%(ext)s', file_created_bubble_title=u'Screenshot Added', file_created_bubble_message=u'A screenshot was added to your Dropbox folder.', mbox_save=(u'Save to your:', 'Message that asks the user to select which account (Personal or Business) to use.'), error_caption=(u"Couldn't save screenshot in Dropbox", u'abbreviation for "We couldn\'t move your screenshot to Dropbox". SHORT'), error_connection=u'Dropbox is unable to connect to the Internet. Please check your connection.', error_generic=u"Something went wrong. We're working to fix it.")
    _platform_overrides = dict(win=dict())