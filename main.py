from website import create_app

app = create_app()

if __name__ == '__main__':  
    #this line says only if we run this file, not if we import this file
    app.run(debug = True) # this will run our flask application
    #the reason we want this line is because you were to import main.py from another file 
    # and you didnt have the above line then it would run the web server and you dont want that to happen. 
    # You only want to run the web server if you run this file directly. So thats what the above __name line means.   
    # so main.py will execute this line"""
