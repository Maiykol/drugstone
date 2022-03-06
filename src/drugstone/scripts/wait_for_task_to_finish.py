import logging
import warnings
import time
from .request_task_info import request_task_info


def wait_for_task_to_finish(token: str, task_id: str = None) -> dict:
    """
    Waits for the Task to finish and returns the task information.
    Parameters
    ----------
    token
    task_id

    Returns
    -------
    dict: task information
    """

    info = request_task_info(token)
    while not info["done"] and not info["failed"]:
        logging.info(task_id + " progress is at: " + str(__get_progress(info)))
        time.sleep(2)
        info = request_task_info(token)
    if info["done"]:
        logging.info(task_id + " is done.")
    elif info["failed"]:
        warnings.warn(task_id + " has failed!")
    return info


def __get_progress(info: dict) -> str:
    f_progress = float(info["progress"]) * 100
    return str(f_progress) + "%"