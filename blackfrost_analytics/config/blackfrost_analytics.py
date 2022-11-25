from frappe import _


def get_data():
	return [
		{
			"label": _("Dashboards"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "page",
					"label": _("Sales Dashboard"),
					"name": "sales-dashboard"
				},
				{
					"type": "page",
					"label": _("Gross Profit Dashboard"),
					"name": "gross-profit-dashboard"
				},
				{
					"type": "page",
					"label": _("Accounts Receivable Dashboard"),
					"name": "accounts-receivable-dashboard"
				},
				{
					"type": "page",
					"label": _("Bank & Cash Balance Dashboard"),
					"name": "bank-cash-balance-dashboard"
				},
			]
		},
		{
			"label": _("Settings"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"label": _("Blackfrost Analytics Settings"),
					"name": "Blackfrost Analytics Settings"
				},
			]
		},
	]