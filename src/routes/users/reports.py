""""
Handles reports/cases uploaded by citizens

"""
import mimetypes
import enum
import uuid
import json
from datetime import datetime
from config import db
from Logic_objects import location as loc
from ML_workspace import model, CovidCT, CovidXray, Tuber
# from Logic_objects import file_server
from flask import Blueprint, request, make_response, jsonify

from routes.users import token_required
from routes import API_required


file = Blueprint('file', __name__)


@file.route("/new-CovidCT",  methods=['POST'])
@token_required
@API_required
def new_CovidCT(current_user):
    if not current_user:
        return make_response(jsonify({
            'message': 'unable to find user '
        }), 400)
    try:
        if not request or not request.json:
            return make_response(jsonify(error="Requirements Missing REQUIRED"), 400)
        resp = dict(request.json)
        ImgID = resp.get("ImgID")
        Covid = CovidCT.CovidCT(ImgID)
        response = Covid.Predict()
        newObj = db.users.update_one({"_id": current_user["_id"]}, {
            "$set": {"Services": current_user["Services"]["CovidCT"].append(
                {
                    "date": str(datetime.now()),
                    "result": response,
                    "ImgFile": ImgID
                }
            )}
        })
        return make_response(jsonify(success=True), 200)
    except Exception as e:
        print(e,  e.__traceback__.tb_lineno)
        return make_response(jsonify(uploaded="fail", file_id=None, error=e), 403)


@file.route("/new-CovidXray",  methods=['POST'])
@token_required
@API_required
def new_CovidXray(current_user):
    if not current_user:
        return make_response(jsonify({
            'message': 'unable to find user'
        }), 400)
    try:
        if not request or not request.json:
            return make_response(jsonify(error="Requirements Missing REQUIRED"), 400)
        resp = dict(request.json)
        ImgID = resp.get("ImgID")
        Covid = CovidXray.CovidXray(ImgID)
        response = Covid.Predict()
        newObj = db.users.update_one({"_id": current_user["_id"]}, {
            "$set": {"Services": current_user["Services"]["CovidXray"].append(
                {
                    "date": str(datetime.now()),
                    "result": response,
                    "ImgFile": ImgID
                }
            )}
        })
        return make_response(jsonify(success=True), 200)
    except Exception as e:
        print(e,  e.__traceback__.tb_lineno)
        return make_response(jsonify(uploaded="fail", file_id=None, error=e), 403)


@file.route("/new-Tuber",  methods=['POST'])
@token_required
@API_required
def new_Tuber(current_user):
    if not current_user:
        return make_response(jsonify({
            'message': 'unable to find user '
        }), 400)
    try:
        if not request or not request.json:
            return make_response(jsonify(error="Requirements Missing REQUIRED"), 400)
        resp = dict(request.json)
        ImgID = resp.get("ImgID")
        Covid = Tuber.Tuber(ImgID)
        response = Covid.Predict()
        newObj = db.users.update_one({"_id": current_user["_id"]}, {
            "$set": {"Services": current_user["Services"]["Tuber"].append(
                {
                    "date": str(datetime.now()),
                    "result": response,
                    "ImgFile": ImgID
                }
            )}
        })
        return make_response(jsonify(success=True), 200)
    except Exception as e:
        print(e,  e.__traceback__.tb_lineno)
        return make_response(jsonify(uploaded="fail", file_id=None, error=e), 403)
