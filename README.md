## 🚀 Usage

- Make sure you have [Xampp](https://www.apachefriends.org/) installed (`Xampp` is shipped by default since xamp `8.15`)
- Create Database on `Xamp` `Php Admin` `MySql` with name "cinema"
- Check the connection.
- Make sure you have [Python](https://www.python.org/) (require version 3.1+, in my project using python 3.7)

## ✨ Installation/Demo Front End

1. Clone the repo
   ```sh
   git clone https://github.com/Lqlam2102/cinema_mobile_be.git
   ```
2. Move to the project
   ```
   cd cinema_mobile_be
   ```
3. Install module from requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
4. Migrate Models
   ```sh
   py manage.py makemigrations
   py manage.py migrate
   ```
5. Run server
    ```sh
    py manage.py runserver
    ```

- [Front-End](https://github.com/Lqlam2102/cinema_app_react-native) make with React Native


## 📝 License

Copyright © 2022 [Lqlam2102](https://github.com/Lqlam2102).<br />
This project is [Django](https://github.com/Lqlam2102/cinema_mobile_be/README.md) licensed.