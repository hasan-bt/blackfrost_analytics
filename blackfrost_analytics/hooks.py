# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "blackfrost_analytics"
app_title = "Blackfrost Analytics"
app_publisher = "Hasan Raza"
app_description = "Blackfrost Analytics"
app_icon = "octicon octicon-file-directory"
app_color = "black"
app_email = "hasan.raza@blackfrosttechnologies.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/blackfrost_analytics/css/blackfrost_analytics.css"
# app_include_js = "/assets/blackfrost_analytics/js/blackfrost_analytics.js"

# include js, css files in header of web template
# web_include_css = "/assets/blackfrost_analytics/css/blackfrost_analytics.css"
# web_include_js = "/assets/blackfrost_analytics/js/blackfrost_analytics.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "blackfrost_analytics.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "blackfrost_analytics.install.before_install"
# after_install = "blackfrost_analytics.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "blackfrost_analytics.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"blackfrost_analytics.tasks.all"
# 	],
# 	"daily": [
# 		"blackfrost_analytics.tasks.daily"
# 	],
# 	"hourly": [
# 		"blackfrost_analytics.tasks.hourly"
# 	],
# 	"weekly": [
# 		"blackfrost_analytics.tasks.weekly"
# 	]
# 	"monthly": [
# 		"blackfrost_analytics.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "blackfrost_analytics.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "blackfrost_analytics.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "blackfrost_analytics.task.get_dashboard_data"
# }

