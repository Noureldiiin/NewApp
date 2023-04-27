# Copyright (c) 2023, Nour and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from docx import Document as docx
from docxtpl import DocxTemplate
from frappe.utils import get_site_name 
import os
import json

class FillingRequest(Document):
	pass

@frappe.whitelist()
def download_file(doc):
	print(doc)
	doc = json.loads(doc)
	get_template = frappe.db.sql(f"""
			select * from `tabTemplate`
			join `tabTemplate Table` on `tabTemplate`.name = `tabTemplate Table`.parent
			where `tabTemplate Table`.doctype_name = '{doc['doctype']}'
			and `tabTemplate Table`.template_file IS NOT NULL
	""",as_dict = 1)
	if get_template is None:
		frappe.throw("There is no such template for this doctype")
	try:
		current_working_directory = os.getcwd()
		filee = frappe.get_doc("File", get_template[0].template_file)
		template = DocxTemplate(filee.get_full_path())
		to_fill_in = doc
		template.render(to_fill_in)

		# save the modified document
		template.save(current_working_directory + '/filling_request.docx')
		
		frappe.msgprint("Downloaded!")
	except:
		frappe.throw("Something went wrong")


