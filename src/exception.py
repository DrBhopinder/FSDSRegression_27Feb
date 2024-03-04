import sys #sys is a system library, whenever there is an error that are there, what we do is we create a function error_messege_detail.
from src.logger import logging

def error_message_detail(error,error_detail:sys):   #This is for displaying error
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):   #Exception is parent exception class
    
    def __init__(self, error_message, error_detail:sys):  #sys is system error
        super().__init__(error_message)   #here inheriting error messege from parent class
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message    
    
'''

if __name__=="__main__":
    logging.info("Logging has started")

    try:
        a=1/0
    except Exception as e:
        logging.info('Dicision by zero') 
        raise CustomException(e,sys)
'''