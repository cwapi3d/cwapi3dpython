from src.cadwork.bim_team_upload_result_code import bim_team_upload_result_code


class bim_team_upload_result:
    """bim team upload result
    """

    def __init__(self):
        """
        Instance of the bim_team_upload_result class.

        Attributes:
            upload_result_code (bim_team_upload_result_code): The result code of the upload.
            share_link (str): The share link for the uploaded BIM team result.
        """
        self.upload_result_code = bim_team_upload_result_code.ok
        self.share_link = ""
