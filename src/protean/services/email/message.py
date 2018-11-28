""" Define Email message objects that are used by the backends """
from protean.conf import active_config


class EmailMessage:
    """A container for email information."""

    def __init__(self, subject='', body='', from_email=None, to=None, bcc=None,
                 cc=None, reply_to=None, **kwargs):
        """
        Initialize a single email message (which can be sent to multiple
        recipients).
        """
        if to:
            if isinstance(to, str):
                raise TypeError('"to" argument must be a list or tuple')
            self.to = list(to)
        else:
            self.to = []
        if cc:
            if isinstance(cc, str):
                raise TypeError('"cc" argument must be a list or tuple')
            self.cc = list(cc)
        else:
            self.cc = []
        if bcc:
            if isinstance(bcc, str):
                raise TypeError('"bcc" argument must be a list or tuple')
            self.bcc = list(bcc)
        else:
            self.bcc = []
        if reply_to:
            if isinstance(reply_to, str):
                raise TypeError('"reply_to" argument must be a list or tuple')
            self.reply_to = list(reply_to)
        else:
            self.reply_to = []
        self.from_email = from_email or active_config.DEFAULT_FROM_EMAIL
        self.subject = subject
        self.body = body or ''
        self.kwargs = kwargs

    def message(self):
        """ Convert the message to a mime compliant email string """
        return '\n'.join(
            [self.from_email, str(self.to), self.subject, self.body])
