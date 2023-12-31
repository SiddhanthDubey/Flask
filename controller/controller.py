from app import app
from flask import request, send_file, make_response
import logging
from controller.error_controller import AppLogger
# Configure the logging settings


from model.customer_model import Customer
from model.agent_model import Agent

# Configure the logging settings

# Create a logger instance for your module or script
logger_controller = AppLogger()

customer = Customer()
agent = Agent()

@app.route("/user/getall")
def user_getall_controller():
    try:
        return customer.user_getall_model()
    except Exception as e:
        logger_controller.log_error(f"Error in user_getList_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/user/addone", methods=["POST"])
def user_addone_controller():
    try:
        return customer.user_addone_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_addone_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/user/update", methods=["PUT"])
def user_update_controller():
    try:
        return customer.user_update_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_update_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/user/delete", methods=["DELETE"])
def user_delete_controller():
    try:
        return customer.user_delete_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in user_delete_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/agent/getall")
def agent_getall_controller():
    try:
        return agent.agent_getall_model()
    except Exception as e:
        logger_controller.log_error(f"Error in agent_getall_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/agent/apply", methods=["PUT"])
def agent_apply_controller():
    try:
        return agent.agent_apply_model(request.form)
    except Exception as e:
        logger_controller.log_error(f"Error in agent_apply_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)

@app.route("/agent/apply_history", methods=["GET"])
def agent_apply_history_controller():
    try:
        return agent.agent_apply_history_model()
    except Exception as e:
        logger_controller.log_error(f"Error in agent_apply_history_controller: {e}")
        return make_response({"message": "An error occurred while processing your request"}, 500)
