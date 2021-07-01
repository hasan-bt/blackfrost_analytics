# Copyright (c) 2013, Hasan Raza and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
	data = frappe.db.sql("""
		SELECT
			sales.posting_date AS date,
			sales.name         AS document,
			sales.customer,
			c.territory,
			steam.sales_person,
			item.item_code,
			item.item_name,
			im.item_group,
			im.brand,
			item.stock_qty * ifnull(steam.allocated_percentage, 100) / 100 as stock_qty,
			item.alt_uom_qty * ifnull(steam.allocated_percentage, 100) / 100 as alt_uom_qty,
			item.net_amount * ifnull(steam.allocated_percentage, 100) / 100 as net_amount
		
		FROM `tabSales Invoice` AS sales
		INNER JOIN `tabSales Invoice Item` AS item ON item.parent = sales.name
		INNER JOIN `tabCustomer` AS c ON c.name = sales.customer
		INNER JOIN `tabItem` AS im ON im.name = item.item_code
		LEFT JOIN `tabSales Team` AS steam on steam.parent = sales.name and steam.parenttype = 'Sales Invoice'
		
		WHERE sales.docstatus = 1 AND sales.is_opening != 'Yes'
		
		ORDER BY sales.posting_date DESC
	""", as_dict=1)

	columns = [{'fieldname': k, 'label': k} for k in data[0].keys()] if data else []

	return columns, data
