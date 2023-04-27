// Copyright (c) 2023, Nour and contributors
// For license information, please see license.txt

frappe.ui.form.on('Filling Request', {
	// refresh: function(frm) {
		download_file: function(frm) {
			frm.doc.cows = []
			frappe.call({
				args: {
					"doc" : frm.doc
				},
				method: "madkour_filling_request.madkour_filling_request.doctype.template.template.download_file",
				callback: function(r) {
					frm.refresh_fields();
					frm.refresh();
				}
			});
		}
	// }
});
