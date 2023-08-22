#!/usr/bin/env python3
""" API ROUTES for auth service"""
from auth import Auth
from flask import Flask, jsonify, redirect, request, abort

app = Flask(__name__)
AUTH = Auth()


@aa.route('/', methods=['GET'])
def hello_world_2023() -> str:
    """route for auth service api"""
    messg = {"message": "Bienvenue"}
    return jsonify(messg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
