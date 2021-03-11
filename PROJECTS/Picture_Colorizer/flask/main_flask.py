def dsd():
    return 2
if __name__ == '__main__':
    from flask import Flask, request, render_template
    from utils.functions import read_json
    import os

    # Mandatory
    app = Flask(__name__)  # __name__ --> __main__  

    # ---------- Flask functions ----------
    @app.route("/")  # @ --> esto representa el decorador de la función
    def home():
        """ Default path """
        return app.send_static_file('option.html')

    @app.route("/option")
    def option():
        option = request.args.get('option')
        if option == '0' or option == '1':
            return render_template('amount.html', option=option)
        else:
            return 'Please select one of the options valid (0 or 1)'

    @app.route("/amount")
    def amount():
        amount = request.args.get('amount')
        return render_template('format.html', amount=amount)


    @app.route("/format")
    def format():
        format = request.args.get('format')
        return render_template('brief.html', format=format)



    
    # ---------- Other functions ----------

    def main():
        print("---------STARTING PROCESS---------")
        print(__file__)
        
        # Get the settings fullpath
        # \\ --> WINDOWS
        # / --> UNIX
        settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
        print(settings_file)
        # Load json from file
        json_readed = read_json(fullpath=settings_file)
        
        # Load variables from jsons
        SERVER_RUNNING = json_readed["server_running"]
        print("SERVER_RUNNING", SERVER_RUNNING)
        if SERVER_RUNNING:
            DEBUG = json_readed["debug"]
            HOST = json_readed["host"]
            PORT_NUM = json_readed["port"]
            app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
        else:
            print("Server settings.json doesn't allow to start server. " + 
                "Please, allow it to run it.")

if __name__ == "__main__":
    main()