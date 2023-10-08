from flask import Blueprint, render_template
from mapping_tools.create_map import *
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
@views.route('/safety')
def safety():
    return render_template("safety.html")
@views.route('/map')
def map():
    ip=get_ip()
    region=get_region_by_ip(ip)
    code,region=country_code_prep(region)
    data,region=prepare_data(code,region)
    create_map(data,region)
    return render_template("map.html")