# RPC over HTTP

This is a simple JavaScript library for promised RPC over HTTP implemented with python Backend.
  - Easy to use.
  - Eases Frontend development.

# Installation

  - Add [`server.js`] to Frontend directory.
  - Aad [`app.py`] to Backend directory.
  - Create a file called `api.py` in your Backend directory and add some functions:
    ```py
    def login(username, password, request):
        if username == 'foo' and password == 'bar':
            return 'correct credentials'
        return 'forbidden'
    ```
    the `request` object is passed to the evey function by `app.py`.
(For more examples see [`api.py`])
  - Add [`populate.py`] to your scripts directory and change any relevant paths inside it.

# Usage
- Every time you add a new function to `api.py`, run [`populate.py`] so you could use it in your Frontend code.
- Once populated, import server:
    ```js
    import server from 'server'
    ```
    then call one of your server functions:
    ```js
    server.login('foo', 'bar');
    ```
    or if the function returns something:
    ```js
    server.get_some_data().then(response =>{
        console.log(response.data);
    });
    ```
    (For more examples see [`index.js`].)
- Because the functions are populated, most IDEs will suggest the arguments every function takes, which minimizes mistakes:
![screenshot](https://i.imgur.com/tXoClep.png)

#Dependencies
- [axios]

 **Enjoy! 😃**

[`api.py`]: <https://github.com/idomoz/rpc-over-http/blob/master/api.py>
[`server.js`]: <https://github.com/idomoz/rpc-over-http/blob/master/server.js>
[`app.py`]: <https://github.com/idomoz/rpc-over-http/blob/master/app.py>
[`populate.py`]: <https://github.com/idomoz/rpc-over-http/blob/master/populate.py>
[`index.js`]: <https://github.com/idomoz/rpc-over-http/blob/master/index.js>
[axios]: <https://github.com/axios/axios>
