:orphan:

Privacy policy
==============

*Last updated: 2026-11-25*

pygcal is a command-line program that runs on your own computer. It uses
Google's OAuth to access your Google Calendar, with this permission:

- ``https://www.googleapis.com/auth/calendar`` (see, edit, share and delete your calendars)

What it does with your data
---------------------------

- Your your Google Calendar is read and changed only on your computer, by the commands you
  run. Nothing is sent to the author of pygcal or to anyone else; there is no
  pygcal server.
- The OAuth token Google issues is stored on your computer (in your pass(1)
  store or under ``~/.config/google_tokens/``) and is used only to talk to
  Google's API. Delete it, or revoke access at
  https://myaccount.google.com/permissions, to stop pygcal using your account.
- pygcal does not collect analytics, does not share, sell or transfer data, and
  does not use Google user data to train AI or machine-learning models.

pygcal's use of information received from Google APIs adheres to the
`Google API Services User Data Policy
<https://developers.google.com/terms/api-services-user-data-policy>`_,
including the Limited Use requirements.

Contact
-------

Mark Veltzer, mark.veltzer@gmail.com. Source code:
https://github.com/veltzer/pygcal
