#learn from: https://hackersandslackers.com/plotly-dash-with-flask/


from plotlyflask import init_app

app = init_app() #initialize app

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) #run the app





