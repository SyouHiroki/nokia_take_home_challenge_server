# # Make sure work with nokia_take_home_challenge_client.

* # How to use:
  ```
  git clone https://github.com/SyouHiroki/nokia_take_home_challenge_server.git
  cd nokia_take_home_challenge_server
  ```
  ## Then:
    * Execute the script at `sql_script/nokia_take_home_challenge.sql`
    * config mysql at `databases/connect.py`

  ## Then:

  ```
  pip install flask
  pip install flask_socketio
  pip install pymysql
  python ./main.py
  ```

* ## python version:
  * 3.11.1
* ## mysql version:
  * 8.0.31