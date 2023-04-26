// Copyright (c) 2023, Nour and contributors
// For license information, please see license.txt

frappe.ui.form.on('Filling Request', {
	// refresh: function(frm) {
		download_file: function(frm) {
			frm.doc.cows = []
			frappe.call({
				doc: frm.doc,
				method: "download_file",
				callback: function(r) {
					frm.refresh_fields();
					frm.refresh();
				}
			});
		}
	// }
});
