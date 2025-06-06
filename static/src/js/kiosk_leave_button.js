odoo.define('custom_hr_kiosk_leave_request.kiosk_leave_button', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');

    publicWidget.registry.KioskLeaveRequest = publicWidget.Widget.extend({
        selector: '.o_hr_attendance_kiosk_mode',
        events: {
            'click .o_kiosk_leave_request': '_onLeaveRequestClick',
        },

        _onLeaveRequestClick: function () {
            alert("Заявката е изпратена успешно!");
        },
    });
});
