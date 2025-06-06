{
    'name': 'Kiosk Leave Request Button',
    'version': '0.1',
    'author': 'Vladi',
    'category': 'Human Resources',
    'summary': 'Добавя бутон за заявка на отпуска в Kiosk режима',
    'depends': ['hr_attendance'],
    'assets': {
        'web.assets_backend': [
            'custom_hr_kiosk_leave_request/static/src/js/kiosk_leave_button.js',
        ],
    },
    'data': [
        'views/assets.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}