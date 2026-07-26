import sys
import logging

#method for padronized error messages 
def error_message_detail(error,error_detail:sys):
    exc_type,exc_value,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}] exception type [{3}] and exception value [{4}]".format(
        file_name,exc_tb.tb_lineno,str(error),exc_type,exc_value
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
    #like a getter method
    def __str__(self):
        return self.error_message



if __name__=="__main__":
    try:
        a = 1/0

    except Exception as e:
        logging.info("divided by zero")
        raise CustomException(e,sys)
