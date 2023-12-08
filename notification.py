def user_notification_handler(data, user_data,label_3,widget,timeNotificacion):
    user_name = user_data.get("username", "Usuario")

    movie_title = data.get('nombre', 'Película Desconocida')
    label_3.setText(f"¡Hola {user_name}, hay una nueva película disponible: {movie_title}!")
    widget.show()
    print(f"¡Hola {user_name}, hay una nueva película disponible: {movie_title}!")
    timeNotificacion.start(3000)