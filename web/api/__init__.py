from flask import Blueprint

bp = Blueprint("api",__name__)

# 一定要把需要依赖的导入，不导入就无法生效
from . import Api