import sys

def error_message_detail(error,error_detail:sys):
    exc_type,exc_value,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in Python script name [{0}] line number [{1}] error message [{2}] exception type [{3}] and exception value [{4}]".format(
        file_name,exc_tb.tb_lineno,str(error),exc_type,exc_value
    )