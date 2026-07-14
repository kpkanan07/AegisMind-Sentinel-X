class SplunkConnector:
    

    def connect(self):

        return {

            "status":
            "Connected",

            "source":
            "Splunk"

        }


    def fetch_logs(self):

        return [

            {

            "event":
            "login_failure",

            "count":
            15

            }

        ]