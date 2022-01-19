from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
from apps.models.LoanModel import Loan

SALT = PARAMS.SALT.salt


class ControllerLoan(object):
    @classmethod
    def get_loan_by_cif(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = Loan.where('cif', '=', input_data.cif).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = encoder_app(ResponseCIF(**{"cif_list": data}).json(), SALT)
                Log.info(result.message)
            else:
                e = "cif not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result

    @classmethod
    def get_loan_by_cif_debug(cls, input_data=None):
        input_data = RequestCIF(**input_data)
        result = BaseResponse()
        result.status = 400

        try:
            if input_data.cif is not None:
                data = Loan.where('cif', '=', input_data.cif).get().serialize()
                result.status = 200
                result.message = "Success"
                result.data = ResponseCIF(**{"cif_list": data})
                Log.info(result.message)
            else:
                e = "cif not found!"
                Log.error(e)
                result.status = 404
                result.message = str(e)
        except Exception as e:
            Log.error(e)
            result.status = 400
            result.message = str(e)

        return result
    
    @classmethod
    def get_total_by_feature(cls, gender, marital_status):
        result = BaseResponse()
        result.status = 400
        
        data = Loan.all().count()
        
        if gender:
            loan = Loan.where('gender', '=', gender) 
            data = loan.count()
       
        if marital_status:
            loan = loan.where('marital_status', '=', marital_status)
            data = loan.count()
        
        result.status = 200
        result.message = "Success"
        result.data = { "count_lount": data }
        return result