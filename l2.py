# -*- coding: utf-8 -*-
# @Author: 25500
# @Date:   2019-11-29 17:18:02
# @Last Modified by:   25500
# @Last Modified time: 2019-11-29 17:18:57
from ryu.base import app_manager
class L2Switch(app_manager.RyuApp):
	def __init__(self, *args, **kwargs):
		super(L2Switch, self).__init__(*args, **kwargs)