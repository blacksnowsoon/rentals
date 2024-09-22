# Copyright (c) 2024, Gharieb Khalifa and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters: dict | None = None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accepts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	return columns, data


def get_columns() -> list[dict]:
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("Make"),
			"fieldname": "make",
			"fieldtype": "Data",
		},
		{
			"label": _("Total Revenue"),
			"fieldname": "total_revenue",
			"fieldtype": "Currency",
			"options": "EGP"
		},
	]


def get_data() -> list[list]:
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return frappe.get_all("Ride Booking", 
					   fields= ["SUM(total_amount) AS total_revenue", "vehicle.make"], 
					   filters={"docstatus":("<", 2)}, group_by="make")
	


#frappe.get_all("Ride Booking", fields= ["SUM(total_amount) AS total_revenue", "vehicle.make"], filte
  #  ...: rs={"docstatus":("<", 2)}, group_by="make")